name = input("Enter Your Name :")
age = input("Enter Your Age :")
birthday = input("Enter Your birthday :")
with open('itf8_txt',"w") as file :
    file.write(name)
    file.write(age)
    file.write(birthday)
    file.close()