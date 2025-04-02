import time

# 获取当前时间戳
timestamp = time.time()
print("当前时间戳:", timestamp)

# 将时间戳转换为本地时间元组
local_time = time.localtime(timestamp)
print("\n本地时间元组:")
print("年:", local_time.tm_year)
print("月:", local_time.tm_mon)
print("日:", local_time.tm_mday)
print("时:", local_time.tm_hour)
print("分:", local_time.tm_min)
print("秒:", local_time.tm_sec)

# 格式化时间输出
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("\n格式化时间:", formatted_time)

# 暂停执行2秒
print("\n开始暂停2秒...")
time.sleep(2)
print("暂停结束")

# 显示另一个时间格式
print("\n另一种时间格式:", time.strftime("%A, %d %B %Y", local_time))