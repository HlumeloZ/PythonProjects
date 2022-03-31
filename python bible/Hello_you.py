#ask user for name

name = input("What is your name?: ")

#ask user for age
age = input("What is your age?: ")

#ask user for city
city = input("What city do you live in?: ")

#ask user what they enjoy
love = input ("what do you enjoy doing?: ")

#create output text

string = "Your name is {} and you are {} years old.You live in {} and you love {}"
output = string.format(name,age,city,love)
#print outout to screen

print(output)
