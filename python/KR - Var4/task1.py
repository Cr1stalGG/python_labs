try:
    s = input("Input name and surname in 1 line: ")
    name, surname = s.split()
    result = surname + " " + name

    print("Result is:", result)
except:
    print("Smth going wrong...")
