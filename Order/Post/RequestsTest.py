import requests
import re

url = "http://ws.order.ttd.uat.qa.nt.ctripcorp.com/Thingstodo-Order-OrderService/api/json/ReceivableNotice"
headers = {"SOA20-Client-AppId": "100001174"}
data = {"OrderId":2340058440,"DistributionChannelId":18,"ReceivableStatus":1}
def test():
    r = requests.post(url=url, json=data, headers=headers)
    print(re.findall(r'"Ack":"(.*)","Errors"',r.text))
    return (re.findall(r'"Ack":"(.*)","Errors"',r.text))


test()