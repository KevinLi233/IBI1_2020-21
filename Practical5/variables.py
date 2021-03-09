a = 310301
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
if d > e:
	print("d is greater")
elif d == e:
	print("d is same to e")
else:
	print("e is greater")

X = True
Y = False
Z = (X and not Y) or (Y and not X)

if Z:
	print("Z is True")
else:
	print("Z is False")

W = X != Y
if W == Z:
	print("W and Z are same")
else:
	print("W and Z are not same")
