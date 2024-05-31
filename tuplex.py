while True:
    Name=input("Enter the Name:")
    Age=int(input("Enter the Age:"))
    Gender=input("Enter the Gender:")
    m = [Name,Age,Gender]
    if m[1] >= 30:
        if m[2] == "male":
            print("Thiru",Name)
        else:
            print("Tmt",Name)
    else:
        if m[2] == "male":
            print("selvan", Name)
        else:
            print("Selvi", Name)
    choice = input("Are you want to continue:")
    if choice == "yes":
        continue
    else:
        break
