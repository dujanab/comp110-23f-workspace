name: str = input("Name? ")

if len(name) > 6:
    print("Do you have a nickname?")
else:
    if name == "Dujana":
        print("Ok, cool.")
    else:
        print("Nice to meet you, " + name)
    
