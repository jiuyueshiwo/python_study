# -*- coding:utf-8 -*-  
import os
import subprocess
import zipfile
import string

rg = string.digits + string.ascii_letters + string.punctuation

def _brutecrack(rg):
	for a in rg:
		for b in rg:
			for c in rg:
				for d in rg:
					for e in rg:
						for f in rg:
							passwd=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
							command='c:\\Program Files\\7Zip\\7z.exe -p'+passwd+' t C:/Users/Administrator/Desktop/genxi.zip'  #t 表示test，不进行实际解压，只测试密码
							os.system("cls")
							print("\r尝试密码为："+passwd, end="")
							child=subprocess.call(command)
							#os.popen(command)#这个也可以用,但是不好监控解压状态
							if child==0:
								print(child)
								print("密码为："+passwd)
								return True
	return False

def brutecrack():
	rg_temp = string.digits
	if _brutecrack(rg_temp):
		return 
	rg_temp = string.ascii_lowercase
	if _brutecrack(rg_temp):
		return
	rg_temp = rg 
	_brutecrack(rg_temp)
	
if __name__ == '__main__':
	brutecrack()