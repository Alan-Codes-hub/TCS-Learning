#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from decimal import *

a=Decimal('.1')
b=Decimal('.3')
x = a+a+a-b
print(x)
print(type(x))
