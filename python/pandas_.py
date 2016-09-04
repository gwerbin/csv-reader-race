#! /usr/bin/env python3

import pandas
import time

time1 = time.perf_counter()
data = pandas.read_csv("big-iris.csv")
time2 = time.perf_counter()

print(time2 - time1)
