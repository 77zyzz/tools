# t00ls签到脚本

造轮子

利用t00ls接口完成签到，并通过bark(ios),server酱(android/ios)完成消息推送，手机可以获取签到结果

可以放到云服务器上，用计划任务每天执行一遍，我比较习惯每天7.30，醒了就能看到

```
crontab -e

添加下列计划任务
30 07 * * * /usr/bin/python3 /root/t00ls/t00ls.py
```