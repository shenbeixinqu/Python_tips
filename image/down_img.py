import requests
import os

url = "http://10.1.1.6/s/u/52/photo.jpg"
path = os.getcwd()
print(path)

users = [17041,17397,16728,17801,18280,16733,16990,17070,17071,17158,17384,17660,17695,18270,16734,16736,17104,17587,17589,17590]
for user in users:
    url = "{}/s/u/{}/photo.jpg".format("http://10.1.1.6", user)
    r = requests.request('get', url)  # 获取网页
    with open('./'+str(user)+'.jpg', 'wb') as f:  # 打开写入到path路径里-二进制文件，返回的句柄名为f
        f.write(r.content)  # 往f里写入r对象的二进制文件
    f.close()
