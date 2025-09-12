name= input("Write you name: ")
Age= int(input("Tell your age: "))
Hab=(input("Do you have license? 1-Yes|2-No: "))

if Age >=18:
    print(f"{name} You have age")
    if Hab=="Yes":
        print(f"{name} You have license 😎😎😎")
    else:
         print(f"Sorry {name} but you don`t have license 😢😢😢")
else:
    print(f"Sorry {name} but you need wait more time 😢😢😢")
    