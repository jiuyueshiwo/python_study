# coding=utf-8
import requests
import os

class BarSpider(object):
	def __init__(self, bar_name):
		self.bar_name = bar_name
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
		self.url_temp = "https://tieba.baidu.com/f?kw="+self.bar_name+"&ie=utf-8&pn={}"
		self.dir_path = "C:/Users/Administrator/Desktop/"+self.bar_name+"贴吧"
		self.path_name = self.dir_path+"/"+self.bar_name+"吧第{}页.html"
		

	def get_url_list(self):
		return [self.url_temp.format(i*50) for i in range(100)]

	def prase_url(self, url_temp):
		response = requests.get(url_temp, headers=self.headers)
		return response.content.decode()

	def save_html(self, content, page_num):
		file_path = self.path_name.format(page_num)
		with open(file_path, "w", encoding="utf-8") as f:
			f.write(content)
			print("sucess %s page" % page_num)

	def run(self):
		os.mkdir(self.dir_path)
		#合成URL
		url_list = self.get_url_list()
		for url_temp in url_list:
			#请求对应的网页内容
			content = self.prase_url(url_temp)
			#将网页内容保存为文件
			page_num = url_list.index(url_temp)+1
			self.save_html(content, page_num)
			


def main():
	bar_name = input("请输入想要下载的贴吧名字:")
	barspider = BarSpider(bar_name)
	barspider.run()


if __name__ == '__main__':
	main()