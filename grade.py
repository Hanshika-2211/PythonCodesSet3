answer = int(input("Enter the marks : "))

if(answer>=70):
    print("Distinction")
elif(answer<70 & answer>=60):
    print("First Class")
elif(answer<60 & answer>=50):
    print("Second Class")
elif(answer<50 & answer>=35):
    print("Pass")
else:
    print("Failed")