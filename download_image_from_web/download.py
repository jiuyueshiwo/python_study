#-*- coding: UTF-8 -*- 
import urllib.request
import gevent
import os
import re
import zlib


name_index = 1


def download(img_url):
    global name_index

    req = urllib.request.urlopen(img_url)
    img_content = req.read()

    img_name = str(name_index) + ".jpg"
    name_index += 1

    try:
        os.mkdir("image")
    except:
        pass
    with open("image/" + img_name, "wb") as f:
        f.write(img_content)


def get_url(img_url):
    req = urllib.request.urlopen(img_url)
    org_content = req.read()
    decompressed_data = zlib.decompress(org_content ,16+zlib.MAX_WBITS)
    with open("1.txt", "wb") as f:
        f.write(decompressed_data)
    content = decompressed_data.decode('utf8')
    #print(content)
    
    #with open("1.txt", "rb") as f:
        #content = str(f.read())
    content_list = re.findall(r"https[^\"]+\.jpg", content)
    
    for sub_str in content_list:
        print(sub_str)
        g = gevent.spawn(download, sub_str)
        g.join()   
        
   


def main():

    #img_url = input("请输入想要下载图片的网址：")
    #img_url = "https://" + img_url
    #get_url(img_url)
    get_url("https://www.douyu.com/g_xingyu")
    #req = urllib.request.urlopen("https://www.douyu.com/g_yz")






if __name__ == '__main__':
    main ()
