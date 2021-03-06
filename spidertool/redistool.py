#!/usr/bin/env pythen
# -*- coding: utf-8 -*-

import sys
import json,datetime

reload(sys)
sys.setdefaultencoding('utf-8')

#通过python操作redis缓存
redisinstance=None

try:
    if redisinstance is None:
        import redis
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
	# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
        redisinstance = redis.Redis(connection_pool=pool)
except Exception,e:
    print e

def getObject():
    return redisinstance

def expire(key,expiration):
    print "======================redistool::expire(%s)======================"%key
    if redisinstance is None:
        return None
    redisinstance.expire(key, expiration)

#from ip to location
def get(key):
    # content's md5 value; redisinstance获取链接的数据库db
    print "======================redistool::get(%s)======================"%key
    if redisinstance is None:
    	print "redisinstance is None."
        return None

    prev_topicList = None

    try:
        prev_topicList_redis = redisinstance.get(key)
        prev_topicList = prev_topicList_redis
#        print ("redistool::get(%s) prev_topicList_redis:%s "%(key, prev_topicList_redis))
        # 没有key，就是正常的关键词检索，非字典
        if prev_topicList_redis is None:
            return prev_topicList_redis
        # import pickle
        # prev_topicList = pickle.loads(prev_topicList_redis)
        prev_topicList = json.loads(prev_topicList_redis,encoding='utf-8')
        prev_topicList = debase64(prev_topicList)
    except Exception,e:
        print 'redis-get', e
        try:
            prev_topicList=eval(prev_topicList)
        except Exception,e:
            print 'eval(prev_topicList)', e
    return prev_topicList

def debase64(dic):
    return iterobj(dic, decode_base64)

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    import base64
    # print "redistool::decode_base64() before_data", data
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding) # bytes格式,=填充
    # print "redistool::decode_base64() after_data", data   #MA==
    return base64.decodestring(data)

def enbase64(dic):
    import base64
    return iterobj(dic,base64.b64encode)

def iterobj(dic, func):
    # print ("redistool::iterobj() dic:%s, func:%s"%(str(dic), str(func)))
    if dic == None:
        return None
    elif type(dic) == int:
        return dic
    elif type(dic) == float:
        return dic
    elif type(dic) ==long:
        return dic
    elif type(dic) == bool:
        return dic
    elif type(dic)==list:
        for i in xrange(len(dic)):
            dic[i]=iterobj(dic[i],func)
        return dic
    elif type(dic)==tuple:
        listitem=list(dic)
        for i in xrange(len(listitem)):
            listitem[i] = iterobj(listitem[i],func)
        dic=tuple(listitem)
        return dic
    elif type(dic)==dict:
        for i in dic.keys():
            dic[i] = iterobj(dic[i],func)
        return dic
    elif type(dic)==unicode or type(dic)==str:
        return func(str(dic))
    else:
        dic=iterobj(object2dict(dic),func)
        return dic

def set(key,value):
    print "======================redistool::set(%s)======================"%key
    if redisinstance is None:
        return
    import copy
    topicList_json = copy.deepcopy(value)
    # topicList_json=value
    try:
        # import pickle
        # topicList_json = pickle.dumps(value)
        topicList_json = json.dumps(enbase64(topicList_json), default=object2dict, indent=2, ensure_ascii=False).encode('utf-8','ignore')
    except Exception,e:
        print e,'redis-set'
        pass
    redisinstance.set(key, topicList_json)

def jdefault(o):
    if isinstance(o, datetime):
         return o.isoformat()

    return o.__dict__

def object2dict(obj):
	d = {}
	d['__class__'] = obj.__class__.__name__
	d['__module__'] = obj.__module__
	d.update(obj.__dict__)

	return d
