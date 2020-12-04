import requests

r = requests.get('https://shanchengzhiyuanzhe.lingxi360.com/login', auth=('2484253186@qq.com', 'xmf253186'))
print(r.status_code)
url='https://shanchengzhiyuanzhe.lingxi360.com/Form/detail/LXEn74EEwLO0d9ua?page=2#form_contact'

print(r.text)
