countries =list(input("Insert as many countries as you can ").split(" "))

countries =list (set(countries)) #"set" takes repeated countries out of the list
countries.sort()

print(countries)

