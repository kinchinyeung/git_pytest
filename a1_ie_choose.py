
#coding:utf-8
import webbrowser as web #对导入的库进行重命名
import os
import time
 
#默认浏览器
def run_to_use_default_browser_open_url(url):
	web.open_new_tab(url)
	print ('run_to_use_default_browser_open_url  open url ending ....')
	
#firefox浏览器	
def use_firefox_open_url(url):
	browser_path=r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe'
	#这里的‘firefox’只是一个浏览器的代号，可以命名为自己认识的名字，只要浏览器路径正确
	web.register('firefox', web.Mozilla('mozilla'), web.BackgroundBrowser(browser_path))
	#web.get('firefox').open(url,new=1,autoraise=True)
	web.get('firefox').open_new_tab(url)
	print ('use_firefox_open_url  open url ending ....')
 
#谷歌浏览器
def use_chrome_open_url(url):
	browser_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
	web.register('chrome', None,web.BackgroundBrowser(browser_path))
	web.get('chrome').open_new_tab(url)
	print ('use_chrome_open_url  open url ending ....')
 
# #Opera浏览器
# def use_opera_open_url(url):
# 	browser_path=r'C:\Program Files (x86)\Opera\launcher.exe'
# 	web.register('opera', None,web.BackgroundBrowser(browser_path))
# 	web.get('chrome').open_new_tab(url)
# 	print 'use_opera_open_url  open url ending ....'
#
# #千影浏览器
# def use_qianying_open_url(url):
# 	browser_path=r'C:\Users\Administrator\AppData\Roaming\qianying\qianying.exe'
# 	web.register('qianying', None,web.BackgroundBrowser(browser_path))
# 	web.get('qianying').open_new_tab(url)
# 	print 'use_qianying_open_url  open url ending ....'
#
# #115浏览器
# def use_115_open_url(url):
# 	browser_path=r'C:\Users\Administrator\AppData\Local\115Chrome\Application\115chrome.exe'
# 	web.register('115', None,web.BackgroundBrowser(browser_path))
# 	web.get('115').open_new_tab(url)
# 	print 'use_115_open_url  open url ending ....'
	
#IE浏览器	
def use_IE_open_url(url):
	browser_path=r'C:\Program Files\Internet Explorer\iexplore.exe'
	web.register('IE', None,web.BackgroundBrowser(browser_path))
	web.get('IE').open_new_tab(url)
	print ('use_IE_open_url  open url ending ....')
	
#搜狗浏览器
def use_sougou_open_url(url):
	browser_path=r'C:\Users\Administrator\AppData\Local\SogouExplorer\SogouExplorer.exe'
	web.register('sougou', None,web.BackgroundBrowser(browser_path))
	web.get('sougou').open_new_tab(url)
	print ('use_sougou_open_url  open url ending ....')
	
#浏览器关闭任务	
def close_broswer():
	os.system('taskkill /f /IM SogouExplorer.exe') 
	print ('kill SogouExplorer.exe')
	os.system('taskkill /f /IM firefox.exe') 
	print ('kill firefox.exe')
	os.system('taskkill /f /IM Chrome.exe') 
	print ('kill Chrome.exe')
	# os.system('taskkill /f /IM launcher.exe')
	# print 'kill launcher.exe'
	# os.system('taskkill /f /IM qianying.exe')
	# print 'kill qianying.exe'
	# os.system('taskkill /f /IM 115chrome.exe')
	# print ('kill 115chrome.exe')
	# os.system('taskkill /f /IM iexplore.exe')
	print ('kill iexplore.exe')
	
#测试运行主程序
def broswer_test():	
	url='https://www.baidu.com'	
	run_to_use_default_browser_open_url(url)
	use_firefox_open_url(url)
	use_chrome_open_url(url)
	# use_qianying_open_url(url)
	# use_115_open_url(url)
	use_IE_open_url(url)
	use_sougou_open_url(url)
	time.sleep(20)#给浏览器打开网页一些反应时间
	close_broswer()
if __name__ == '__main__':  
	print ('''''
            *****************************************  
            **   Welcome to python of browser      **  
            **      Created on 2017-05-07          **  
            **      @author: Jimy _Fengqi          **  
            ***************************************** 
	''' )
	# use_sougou_open_url('https://www.baidu.com')
	broswer_test()
