# import requests
#
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'Cookie': '_zap=e6c767d3-adbd-4582-a566-5183206a8318; d_c0="AABU23WoHRGPTvNygVxG2ISIyq1a9EfUVHU=|1586828094"; _ga=GA1.2.1034196286.1586828097; q_c1=5e430ceed6c743b090d6969951783386|1602220100000|1589254519000; _xsrf=dly2ab4bqy9Nrlb59EEqSQViZTsTydcb; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604551448,1604551644,1604762399,1605926794; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1605926794; capsion_ticket="2|1:0|10:1605926793|14:capsion_ticket|44:ZTExZGY1OTFjYTFkNGQ5MDg0OTQxYmY5YjE1ZWRjMTQ=|05a2058ceda3ee2828bf72064dadaaa06b7c7a063c772a5346a9d04b666fbd41"; l_n_c=1; r_cap_id="OWRlYTYzNjRjN2FiNDUxNGI0MzI3YjVmZWM0ZDBkMzk=|1605926808|f467e9b6ebc2449a6da974aaf319facee6318230"; cap_id="ZDkyNzcxMmM5NTVjNDU3Nzg2MjdjZmUzY2Q4NzcxYWY=|1605926808|c1685cd4b9a241edf0d6fa85d8a45cc6bceb8735"; l_cap_id="YzIwNTRmMjI4MDdmNGI5NWEzNDVjYjFiZDlmMDljZGQ=|1605926808|1edb6d189a400d6260d1d98ee7e1308494342c24"; n_c=1; z_c0=Mi4xR1NERERBQUFBQUFBQUZUYmRhZ2RFUmNBQUFCaEFsVk5uczJsWUFDSDNTenRfR0xwcEZGNHRaNTlmaVJXdXJkOWZR|1605926814|7d9b5d3281cb52d1142902c94034585690b7ba4c; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1605926848|1605926777',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text('utf-8'))