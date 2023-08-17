my_lists=[]
number=int(input("enter number of gigits"))
for i in range(number):
    digits=int(input(f"rnter digit {i+1} "))
    my_lists.append(digits)
print("diferance :",max(my_lists)-min(my_lists))