def divide(divedend, divisor):
	if divisor == 0:
		raise ZeroDivisionError('Divisor cannot be 0.')

	return divedend / divisor


def calculate(*values, operator):
	return operator(*values) # syntaxs for calling a function


result = calculate(20, 4, operator = divide)
print(result)


# ########################################

def search(sequence , expected , finder):
	for elem in sequence:
		if finder(elem) == expected:
			return elem
	raise RuntimeError(f' could not find an element with {expected}.')

friends = [
	{'name': 'Rolf Smith', 'Age': 24},
	{'name': 'Adam Wool', 'Age': 30},
	{'name': 'Anne Pun', 'Age': 27},
]

# def get_friend_name(friend):
# 	return friend['name']

# print(search(friends,"Rolf Smith", get_friend_name))

# or

# print(search(friends,"Rolf Smith", lambda friend: friend['name']))

# or

from operator import itemgetter

print(search(friends, "Rolf Smith", itemgetter("name")))
