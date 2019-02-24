import psutil

print('CPU逻辑数量:', psutil.cpu_count())

print('CPU物理核心:', psutil.cpu_count(logical=False))

print('统计CPU的用户／系统／空闲时间:', psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计3次
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))

#物理内存
print(psutil.virtual_memory())
#交换内存
print(psutil.swap_memory())

# 获取网络读写字节／包的个数
print(psutil.net_io_counters())