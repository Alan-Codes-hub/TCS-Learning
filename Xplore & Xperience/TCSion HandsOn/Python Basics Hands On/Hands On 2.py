#!/bin/python3

import math
import os
import random
import re
import sys



class Student:
    def __init__(self,roll,name,marks_list):
        self.roll=roll
        self.name=name
        self.marks_list=marks_list
        self.percentage=0
    def calculate_percentage(self):
        s=sum(self.marks_list)
        n=len(self.marks_list)
        p=s//n
        self.percentage=p
        return p
    def find_grade(self):
        p=self.percentage
        if(p>=80):
            g='A'
        elif(p>=60):
            g='B'
        elif(p>=40):
            g='C'
        else:
            g='F'
        return g

if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())
