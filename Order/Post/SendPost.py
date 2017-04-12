import re
import requests
import Post.ConfigParser as pc

url = pc.getOrderInfoURL('urlorder')
AutoVBKdata = pc.getOrderInfoData('dataAutoVBKorder').encode('UTF-8')
MannualVBKdata = pc.getOrderInfoData('dataManualVBK').encode('UTF-8')
DJdata=pc.getOrderInfoData('dataDJ').encode('UTF-8')
DataNormal=pc.getOrderInfoData('dataNormal').encode('UTF-8')
headers = {"SOA20-Client-AppId": "100001174"}

def sendPost(data):
    rp = requests.post(url=url, data=data, headers=headers)
    print(rp.text)
    print(re.findall(r'"OrderID":(.*)"ExternalNo"', rp.text))
    return (re.findall(r'"OrderID":(.*)"ExternalNo"', rp.text))


def sendAutoVBKPost():
    return  sendPost(AutoVBKdata)

def sendManVBKPost():
    return  sendPost(MannualVBKdata)

def sendNormalPost():
    return  sendPost(DataNormal)

def sendDJdata():
    return sendPost(DJdata)