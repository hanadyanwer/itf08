my_mark = []


number_studunt = int(input("Enter number of student :"))
for i in range(0,number_studunt):
    num_mark = int(input(f"Enter number of  {i+1} student mark :"))
    sum = 0
    for i in range(0,num_mark):
        mark = int(input(f"Enter mark {i + 1} : "))
        my_mark.append(mark)
        sum += my_mark[i]
    print("student mark :",my_mark)
    print("average = ",round(sum/len(my_mark),2))
    print("max = ",max(my_mark))
    print("min =",min(my_mark))