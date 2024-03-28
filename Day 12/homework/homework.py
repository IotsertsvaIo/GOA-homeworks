name = input("please eneter your name: ")
lastname = input("please enter your lastname: ")
age = int(input("please enter your age: "))
adress = input("please enter your adress: ")


personal_info.append(name)
personal_info.append(lastname)
personal_info.append(age)
personal_info.append(adress)

print(personal_info[0:2])
print(personal_info[1:3])


num = int(input("please enter negative number: "))

negative_number = []

for i in range(num,0):
    print(i)


film = ["avengers", "titanic", "ball", "spider-man"]

print(film[0:4])

film = ["avengers", "titanic", "ball", "spider-man"]
print(film[-1:-3])



