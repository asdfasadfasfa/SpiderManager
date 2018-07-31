#!/usr/bin/python
#coding:utf-8
import urllib2
import time
import re,json
import httplib

# urllib2 默认情况下会针对 HTTP 3XX 返回码自动进行 redirect 动作，无需人工配置, 但不想自动redirect，可以自己定义
class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self,req,fp,code,msg,headers):
		print '301问题'
	def http_error_302(self,req,fp,code,msg,headers):
		print '302问题'

def formatstring(str):
	return '\''+str+'\''

def setCookies(response, user, time):
	print "debug::setCookies() ", user, time
	response.set_cookie('islogin', user.islogin, time)
	response.set_cookie('username', user.username, time)
	response.set_cookie('role', user.role, time)
	response.set_cookie('power', user.power, time)

def delCookies(response):
	response.delete_cookie('islogin')
	response.delete_cookie('username')
	response.delete_cookie('role')
	response.delete_cookie('power')

#convert object to a dict
def object2dict(obj):
	d = {}
	d['__class__'] = obj.__class__.__name__
	d['__module__'] = obj.__module__
	d.update(obj.__dict__)

	return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst

def getlocaltime():
	return str(time.strftime("%Y-%m-%d %X", time.localtime()))

def getmicrosecondtime():
	import datetime
	return str(datetime.datetime.now())

def isip(ip):
 	if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip) != None:
#   		print 'IP!'
  		return True
  	else:
#   		print 'web'
  		return False

def getLocationinfo(ip):
	httpClient=None
	response_data={}
	try:
		httpClient = httplib.HTTPConnection('ip.taobao.com', 80, timeout=30)
		httpClient.request('GET', '/service/getIpInfo.php?ip='+ip)
 
        #response是HTTPResponse对象
		response = httpClient.getresponse()
		print response.status
		print response.reason
		response_data = response.read().strip() # 我理解数据应该存储到ip_maindata
#        {"code":0,"data":{"ip":"110.110.110.120","country":"\xe4\xb8\xad\xe5\x9b\xbd","area":"","region":"\xe9\xbb\x91\xe9\xbe\x99\xe6\xb1\x9f","city":"\xe5\x93\x88\xe5\xb0\x94\xe6\xbb\xa8","county":"XX","isp":"\xe9\x93\x81\xe9\x80\x9a","country_id":"CN","area_id":"","region_id":"230000","city_id":"230100","county_id":"xx","isp_id":"100020"}}
		
	except Exception, e:
		print '接受的数据出现异常'+str(e)
	finally:
		if httpClient:
			httpClient.close()
		try:
			return json.loads(response_data)
		except Exception,e:
			print response_data
			print str(e)+'json error'
			return {}

def md5(str):
	import hashlib
	m = hashlib.md5()   
	m.update(str)
	return m.hexdigest()
