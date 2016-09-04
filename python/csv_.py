#! /usr/bin/env python3

import csv
import time

with open("big-iris.csv") as datafile:
    time1 = time.perf_counter()
    lines = list(csv.reader(datafile))
    time2 = time.perf_counter()

print(time2 - time1)
