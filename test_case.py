import datetime
import time
import calendar

# 获取此时的时间
print time.localtime()

# 获取当天的日期
print datetime.datetime.now()
print datetime.date.today()

# 获取昨天的日期
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print type(today)     # 查看获取到时间的类型
    print type(yesterday)
    return yesterday
yesterday = getYesterday()
print "昨天的时间：", yesterday