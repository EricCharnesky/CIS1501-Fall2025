name = input("Enter your name")

print("the first letter of your name is:", name[0])
print("There are", len(name), "letters in your name")
print("There are " + str(len(name)) + " letters in your name")
print("the last letter of your name is:", name[len(name)-1])
print("the last letter of your name is:", name[-1])

# can only read, not change individual letters
# name[0] = "A"

# change the entire string
name = "Bob"
print(name)

print(f"The first letter in Bob's name is {name[0]}")
print(f"There are {len(name)} letters in your name")

# will round at the last decimal
print(f'1/3 is {7/8:.4f}')

# mutable - changeable list of values
some_list = [ "cats", "chairs", "cars", "ceiling" ]

print(some_list[0])
print(some_list[-1])

some_list[1] = 'coffee'

print(some_list)

some_list.append("cookies")
some_list.append("cars")
print(some_list)

#removes by value - 1st instance only
some_list.remove("cars")
# can't remove items that don't exist
# some_list.remove("CARS")

print(some_list)

# removes by index
some_list.pop(2)

print(some_list)

# removes the last item
some_list.pop()

print(some_list)

# inserts the new item to become the requested index
some_list.insert(1, "computer")

print(some_list)

print(min(some_list))

some_list.append(20)

some_list.append(4.2)

print(some_list)

# gets a little weird with lists inside of lists
some_list.append([1,2,3])
print(some_list)


grades = []

grades.append(int(input("Enter a grade")))
grades.append(int(input("Enter a grade")))
grades.append(int(input("Enter a grade")))
grades.append(int(input("Enter a grade")))
grades.append(int(input("Enter a grade")))

print(f'The lowest grade is {min(grades)}')
print(f'The highest grade is {max(grades)}')
print(f'The mean grade is {sum(grades) / len(grades)}')

number_of_grades = len(grades)
# integer result only - drops the decimal
middle_index = number_of_grades // 2
# sorted makes a new list
# only works with odd for now and we're sad about it
print(f'The median value is {sorted(grades)[middle_index]}')

print(grades)

# changes the order in the list
grades.sort()

print(grades)



# tuples are NOT mutable - collection, where order matters
some_tuple = ( 5, "strings", "phone")
print(some_tuple[0])
# can't change individual values
# some_tuple[0] = 42

some_set = set([1,2,3])

# looks like a dictionary without values
some_other_set = { 1, 2, 3 }

some_set.add(5)
# doesn't crash, but doesn't change the set if given a duplicate
some_set.add(3)

some_set.remove(3)

print(some_set)

# key-value pairs, key : value
some_dictionary = { "Eric" : 100, "Jeb" : 85, "Journey" : 90 }

# adds
some_dictionary['Vivi'] = 75

# update
some_dictionary['Journey'] = 95

# reads the values associated with the key
print(some_dictionary['Journey'])

print(some_dictionary)

print(some_dictionary.keys())
print(some_dictionary.values())

print(some_dictionary.items())


# del some_dictionary['Eric']
# pop finds a key with the given value
some_dictionary.pop("Eric")
print(some_dictionary)