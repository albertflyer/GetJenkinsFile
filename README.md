# GetJenkinsFile

get file from jenkins service, like jacoco report is Integrated to jenkins 
for example like address below 
http://jenkins-test.yourjenkinsdomain.com/job/testjobName/HTML_20Report/*zip*/HTML_20Report.zip


在外部获得自己jenkins域名下的文件，比如集成到jenkins服务里面的代码覆盖率的报告，
由于直接url访问文件会被拒绝，需要验证token

通过python脚本实现

