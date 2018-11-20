# coding=utf-8
import requests
import time
import random
import hashlib
import json


def md5value(s):
    '''
    tans the given word to md5 value
    '''
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


def trans(word):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = str(int(time.time()) + int(random.random() * 10))
    sign = 'fanyideskweb' + word + salt + 'sr_3(QOHT)L2dx#uuGR@r'
    sign = md5value(sign)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Referer': 'http://fanyi.youdao.com',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1049312097@116.247.120.86; OUTFOX_SEARCH_USER_ID_NCOO=518486992.9948139; _ntes_nnid=cd4dc2f54d9ae6b062d027223c85585d,1534339820281; _ga=GA1.2.1229275001.1534814386; fanyi-ad-id=52077; fanyi-ad-closed=1; JSESSIONID=aaaV5AS_2IynKfcqaiVCw; ___rl__test__cookies=1542683931712'
    }

    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "doctype": "json",
        "version": 2.1,
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    res = requests.post(url, data, headers=headers)
    return res.text


if __name__ == '__main__':
    r = trans('工作')
    rj = json.loads(r)

    print(rj['translateResult'][0][0]['tgt'])
    print(rj['smartResult'])
