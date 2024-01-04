sum=0
counter=0
n1=int(input("Enter the start of a range :"))
n2=int(input("Enter the end of a range :"))

for i in range(n1,n2):
    sum+=i
    counter += 1
print("The sum of the first",counter,"numbers is",sum)
average = sum / counter
print("The average of the sum of first",counter,"numbers is", average)