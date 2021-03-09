#input r
#initialize n
#calculate the result
#output the result

r = float(input("Please enter the r number:"))
#gain the number r
n = 84
#set number of students
for i in range(1,5):
	n = n * (1 + r)
#calculate the total number of individuals infected after 5 generations.
#actually equal to n = n*(1+r)^5
s="After 5 generation, there will be "+str(n)+" infected individuals"
print("r number is:",r)
print(s)
#output the description and the result
