import configparser
import os

def cfparser(configFile,option,value):
    os.chdir("E:/Order")
    cf = configparser.ConfigParser()
    cf.read(configFile)
    sec=cf.sections()
    return cf.get(option,value)

def getOrderInfoURL(url):
    return cfparser("orderinfo.ini","URL",url)

def getOrderInfoData(data):
    return cfparser("orderinfo.ini","DATA",data)

