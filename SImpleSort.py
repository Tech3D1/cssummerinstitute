#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:00:14 2018

@author: stem
"""
'''def import_file(y):
    List = open("Unsorted.txt").readlines()
    i=0
    List = [""]
    for Line in inFile:
        List[i]=Line.split(",")
        i+=1
    print(List)'''

lines_list = open('maxtemps.txt').read().splitlines()


#print("This program was designed to sort the list [3,2,4,5,8,7,6,1] it will print the outcome.")
# ^ runs to ensure that the program is running.\

def simple_sort(idx):
    for num in range(len(idx)-1, 0, -1):
        for number in range(num):
            if idx[number] > idx[number+1]:
                temp = idx[number]
                idx[number] = idx[number+1]
                idx[number+1] = temp
    
#lines_list = [3, 2, 4, 5, 8, 7, 6, 1]
simple_sort(lines_list)
print(lines_list)
print(" ")

print(len(lines_list))