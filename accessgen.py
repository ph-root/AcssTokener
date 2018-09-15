#! python3

import random
stra = 'asdfghjklqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM1234567890'

# print('EAAAAUaZA8jlABABSWaZBv9aiBUGDngZBaXP5IZB6YUQAZCTTDSF0ACyQwYUo6etIxobGvXS2WJN1OIPhlnQYsfbCJ59OvgwiwtlupFPPp0PM8gCZB1LlQrflLtROnzqotd2DvuO2CF4imRphYd00eiZAZB5CL8ogdfT1iLsaT2xaQgZDZD')

print('write the number of access tokens you want to generate !!')

print('num :>> ', end='')

num = int(input())
lenth = 164

start = 'EAAAAUaZA8jlAB'

line = ''

lines = []
print()
print('waiting ....')
print()
for ii in range(num):


	for i in range(165):
		x = stra[random.randint(0 , 61)]
		line += x
	
	lines.append(start + line)
	line = ''


file = open('access_tokens.txt' , 'w')
for i in lines:
	file.write(i+'\n')
file.close()
print()
print('access tokens have been saved in the file named [access_tokens.txt]')
print()
print('goodbye ... ')
