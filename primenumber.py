number =int(input("write your number here: "))
counter = 0

number_list = list(range(1,11))

for item in number_list:
    if number%item ==0:
        counter = counter+1
    if number ==1:
        counter = 3

if counter >=3:
    print ("number is not prime")
else:
    print ("number is prime")






