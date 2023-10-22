

def print_names(name, uppercase=True, lowercase=True):

    print(name)

    if uppercase:
        upper = name.upper()
        print(upper)
    
    if lowercase:
        lower = name.lower()
        print(lower)

    if name.strip() == "":
        print("Invalid command! Type your name.")

    

your_name = input("Enter your name:")

print_names(your_name)




