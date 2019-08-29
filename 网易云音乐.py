import requests
import re
import execjs

execjs.get().name

with open("wangyi_music.js", 'r') as f:
    ctx = execjs.compile(f.read())
    ddd = '{"ids":"[28111646]","level":"standard","encodeType":"aac","csrf_token":""}'
    e = "010001"
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    g = "0CoJUm6Qyw8W8jud"
    encdict = ctx.call("d", ddd, e, f, g)
    print(encdict)
    data = {
        'params': encdict['encText'],
        'encSecKey': encdict['encSecKey']
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    res = requests.post(url, data=data, headers=headers)

    print(res.text)
    regex = re.compile(r'http.*\.m4a')
    url_m4a = regex.findall(res.text)[0]
    print(url_m4a)