#set the initial the first and the second number
#repeat
#	calculate the next
#	output

a=1
b=1
#set the first two number
print(a)	#output first number
#get the second second digits to the thirteenth digits
for i in range(2,14,1):
	c=a+b	#calculate the next number
	a=b
	b=c
	print(a)	#output the next number
