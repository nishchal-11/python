marks1=int(input("enter no"))
marks2=int(input("enter no"))
marks3=int(input("enter no"))
total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("pass",total_percentage)
else:
    print("failed",total_percentage)


