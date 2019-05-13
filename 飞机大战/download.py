import urllib.request
import gevent
import os

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


def get_url():
    # req = urllib.request.urlopen(img_url)
    # content = req.read()
    with open("1.txt", "rb") as f:
        content = str(f.read())
    start = "https"
    end = ".jpg"
    start_index = content.find(start)
    while start_index != -1:
        end_index = content.find(end, start_index)
        sub_str = content[start_index:end_index + len(end)]
        start_index = content.find(start, end_index)
        print(sub_str)
        g = gevent.spawn(download, sub_str)
        g.join()


def main():

    #img_url = input("请输入想要下载图片的网址：")
    #img_url = "https://" + img_url
    #get_url(img_url)
    get_url()
    #req = urllib.request.urlopen("https://www.baidu.com")






if __name__ == '__main__':
    main ()