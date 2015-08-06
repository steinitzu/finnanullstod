#!/usr/bin/python
# -*- coding: utf-8 -*-


equation = raw_input("Settu inn margliðu sem jafngildir 0: ")
parsedequation = ""

for i, char in enumerate(equation):
    if char.isspace():
        continue
    if char.isalpha():
        if i>0 and equation[i-1].isdigit():
            parsedequation += "*"
    elif char == "^":
        parsedequation+="**"
        continue
    parsedequation += char


i = len(parsedequation) - 1


numericp = 0
while True:
    char = parsedequation[i]
    if char.isdigit():
        i -= 1
    elif char == "+" or char == "-":
        numericp = int(parsedequation[i:])
        break
    else:
        raise ValueError("Your equation is fucked")

# find numbers divisible by numericp
if numericp < 0:
    start = numericp
    end = (numericp*-1)+1
elif numericp > 0:
    start = numericp*-1
    end = numericp+1

zeros = []
for num in range(start,end):
    if num == 0:
        continue
    elif numericp % num == 0:
        x = num
        evaleq = eval(parsedequation)
        if evaleq == 0:
            print str(num)+": "+parsedequation +" = " +str(evaleq)
    else:
        continue
