#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 测试中文需要在头部制定编码
from queue import Queue

print("测试中文, World!")
print("Index not found.")

q = Queue(maxsize=10)

q.put([1, 2])
q.put([3, 4])
m = q.get()

curr_poccess = Queue()
curr_poccess.put([1, 2])
while not curr_poccess.empty():
    curr = curr_poccess.get()
    print(curr)