# -*- coding: utf-8 -*-
import urllib2
import json
import hashlib
from datetime import datetime

key = '20500'
url = "http://www.facebook-hashtag.com/search/hashtag/FuncashierChef?limit=49"
dir = "/root/sinopac_fun001_result"
#trans_url = "https://bank.sinopac.com/bsp/web15/fun/game/spg-chef/trans.html"
trans_url = "https://bank.sinopac.com/funap/FBPost.ashx"
urllib2_header = [
    ("Accept-Language", "en-US,en;q=0.5"),
    ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv,40.0) Gecko/20100101 Firefox/40.0"),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Connection", "keep-alive"),
]
opener = urllib2.build_opener()
opener.addheaders = urllib2_header


docs = urllib2.urlopen(url).read()

with open('%s/%s' % (dir, datetime.now().strftime('%s')), 'w') as file:
    file.write(docs)

result = json.loads(docs)
for item in result['result']:
    proj = 'fun001'
    p_no = item.get('postID')
    u_no = item.get('userID')
#    u_ming = item.get('user').replace(' ', '')
    u_ming = ''

    hashString = '%s%s%s%s%s' % (proj, u_no, u_ming, p_no, key)
    try:
        mac = hashlib.sha256(hashString.encode('utf-8')).hexdigest().upper()
    except:
        continue

    fullTrans = '%s?proj=%s&u_no=%s&p_no=%s&u_ming=%s&mac=%s' % (trans_url, proj, u_no, p_no, u_ming, mac)

    with open('%s/trans_url' % dir, 'ab') as file:
        # print '%s || %s || %s\n' % (datetime.now(), item.get('user'), fullTrans)
        record_string = '%s || https://www.facebook.com/%s || https://www.facebook.com/%s || %s\n' % (datetime.now(), u_no, p_no, fullTrans)
        file.write(record_string)

    try:
        transResult = opener.open(fullTrans)
        print transResult.read()
    except:pass
