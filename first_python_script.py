print("Please choose from the following options:")
print("1-Read and display names")
print("2-Add a new name")
print("3-Exit")

name_input = ""
names = ""
user_input = input()

while user_input != "3":

    if user_input == "1":
        print("These are the names inside the list:")
        with open("names.txt", "r") as file:
            names = file.read()
            print(names)
        break
    
    elif user_input == "2":
        print("What name do you want to add:")
        name_input = input()
        with open("names.txt", "a") as file:
            file.write(name_input + "\n")
        print (f"{name_input} has been added to the list.")

        break
    
    else:
        print("Option not valid please choose the correct one")
    

