from urllib.robotparser import RobotFileParser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))