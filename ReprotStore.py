#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: jiangfei 20190510
# 作用: 为了对代码覆盖率报告清零之前，做一个备份,支持按时间目录设置保存
import os
import sys
import requests
import datetime
from requests.auth import HTTPBasicAuth
# 远程Jenkins的地址
# job 名
# print(sys.argv[1])
#   组名
# print(sys.argv[2])

# paramNum ==2时候是只有job名  ==3时候 最后一个参数是group name名字
paramNum = len(sys.argv)
print(paramNum)
jobName = sys.argv[1]

# 3 参数带group name
if paramNum == 3:
   groupName = sys.argv[2]

#  groupName为空
if paramNum == 2:
    urlFile = 'http://jenkins-test.你的jenkins域名.com/job/'+jobName+'/HTML_20Report/*zip*/HTML_20Report.zip'
elif paramNum == 3:
    urlFile = 'http://jenkins-test.你的jenkins域名.com/view/' + groupName + '/job/' + jobName + '/HTML_20Report/*zip*/HTML_20Report.zip'

# 用户名
user_id = 'jiangfei'
# 用户的token值(每个user有对应的token)
api_token = 'yourtoken'

auth = HTTPBasicAuth(user_id, api_token)
res = requests.get(url=urlFile, auth=auth)

nowTime = str(datetime.datetime.now()). replace(':', "").replace(' ', "-").replace('.', "")
print(nowTime)


# 文件获得后存放在自己工程在jenkins的工作空间里面
fileReportPath = "/data/test_jenkins/workspace/" + jobName
# 也可以放在jenkins服务的一个具体路径下面 比如
# fileReportPath = "/qa/reportHistory/" + jobName

if not os.path.exists(fileReportPath):
    os.makedirs(fileReportPath)

with open(fileReportPath + "/" + jobName + nowTime+".zip", "wb") as code:
    code.write(res.content)

