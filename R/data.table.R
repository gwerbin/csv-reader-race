#! /usr/bin/env Rscript

time <- system.time(x <- data.table::fread("big-iris.csv"))['elapsed']
print(time)
