# -*- coding:UTF-8 -*-

#n秒输出完成
import time
n = int(input('输入时间：'))
count = 0
while (count < n):
    time.sleep(1)
    print('the count is:',count +1)
    count += 1
print('Good bye!')
    
