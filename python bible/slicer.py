#get user email adress
email = input("What is your email adress?: ").strip()

#slice out user name
user = email[:email.index("@")]

#slice domain name
domain = email[email.index("@") + 1:]

#format message
output = "your username is {} and your domain name is {}".format(user,domain)

#dispaly output message
print(output)
