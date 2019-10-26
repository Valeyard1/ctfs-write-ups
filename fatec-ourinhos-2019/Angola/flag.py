#!/usr/bin/env python3

counter = 0

with open("pi_eb361a465966711f41d04a435e7a0596.txt") as file:
    lst = file.read().splitlines()

for line in lst:
    counter = counter + 1
    
    if line != "PI" and counter % 7 == 0:
        print(line)