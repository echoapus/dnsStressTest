import random
import time
import os

while True:
    i = random.randint(0, 253)
    j = random.randint(0, 253)
    k = random.randint(0, 253)
    l = random.randint(0, 253)
    sp = random.randint(1024, 62535)
    fram1 = random.randint(1, 13)
    fram2 = random.randint(1, 19)
    l1 = random.randint(1, 100)
    l2 = random.randint(1, 76)
    ip = f"{i}.{j}.{k}.{l}"
    Lp1 = random.randint(1, 2)
    Lp2 = random.randint(1, 2)

    for i in range(Lp1):
        os.system(f"mz -c {fram1} -B TargetIP -A {ip} -t dns 'sp={sp},dp=53,q=www.google.com' -d 900u")

    time.sleep(1)

    for i in range(Lp2):
        os.system(f"mz -c {fram2} -B TargetIP -A {ip} -t dns 'sp={sp},dp=53,q=tw.yahoo.com' -d 700u")
