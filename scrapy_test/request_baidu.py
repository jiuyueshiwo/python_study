# coding=utf-8
import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

params = {"wd":"try"}

url_temp = "https://www.baidu.com/s?"

response = requests.get(url_temp, headers=headers, params=params)

print(response.status_code)

#print(response.)