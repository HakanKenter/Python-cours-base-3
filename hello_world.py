#!/usr/bin/env/python3

def fline(x , m =1 , b =0): # f ( x) = m* x + b
    return m *x + b
for i in range (5):
    print ( fline (i ) , end = " " )
# f or c e newl i ne
print ()

for i in range (5):
    print ( fline (i , -1 ,1) , end = " " )