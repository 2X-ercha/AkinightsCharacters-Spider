import os
from bs4 import BeautifulSoup
import time
import requests

url = "http://prts.wiki/index.php?title=%E7%89%B9%E6%AE%8A:%E6%90%9C%E7%B4%A2&limit=500&offset=0&profile=images&search=%E7%AB%8B%E7%BB%98"

headers = {
    "Cookie": "arccount62298=c; arccount62019=c",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}

html = requests.get(url, headers=headers)
html.encoding = html.apparent_encoding
soup = BeautifulSoup(html.text, "html.parser")

list = soup.find_all(class_ = "searchResultImage")

try:
    os.mkdir("./Arknights")  ##  创建文件夹
except:
    pass

os.chdir("./Arknights")

try:
    os.mkdir("./skin")
except:
    pass

try:
    os.mkdir("./1")
except:
    pass

try:
    os.mkdir("./2")
except:
    pass

num=0

for s in list:
    string = str(s)

    namebegin = string.find('title="文件')
    nameend = string[namebegin:].find('png')

    # print(string[namebegin+7:namebegin+nameend+3])

    name = string[namebegin+10:namebegin+nameend+3]
    name = name.replace(" ","_")

    if name.find("b") != -1 or name.find("V") !=-1 or name.find('立绘A') != -1: continue

    urlbegin = string.find('data-src="/images/thumb/')
    urlend = string[urlbegin:].find('png')

    # print(string[urlbegin+24:urlbegin+urlend+3])

    imgurl = 'http://prts.wiki/images/' + string[urlbegin+24:urlbegin+urlend+3]

    # print(name, imgurl)

    if name.find("_skin") != -1: os.chdir('./skin')
    elif name.find("_1") != -1: os.chdir('./1')
    elif name.find("_2") != -1: os.chdir('./2')

    img = requests.get(imgurl, headers=headers).content
    with open(name, 'wb') as f:
        f.write(img)
        num+=1
        print("已爬取{}张,图片名称为：{}，链接为：{}".format(num,name,imgurl))

    os.chdir("..")

    time.sleep(1)
