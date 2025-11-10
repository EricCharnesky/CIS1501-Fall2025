import os
import csv

my_file = open("test.txt")

lines = my_file.readlines()

my_file.close()

for line in lines:
    print(line, end="")

total = 0


# closes the file automatically when the block is done
with open("register.txt") as receipts:
    lines = receipts.readlines()
    for line in lines:
        total += float(line)

print(f"Total receipts in the register: ${total:.2f}" )

filename = input("Enter a filename to write to")

erase = 'y'

if os.path.exists(filename):
    erase = input("The already exists, do you want to erase it? y/n")

if erase == 'y':
    # be careful opening files - it deletes the contents
    test_file = open(filename, 'w')
else:
    # use 'a' to append to the file
    test_file = open(filename, 'a')



test_file.write("Hi there\n")
test_file.write("Happy Monday!\n")
test_file.close()


# bing "[python csv reader headers"
with open("customers-100.csv", "r") as csvfile:
    customers_reader = csv.DictReader(csvfile, delimiter=",")

    print("Headers:", customers_reader.fieldnames)
    for row in customers_reader:
        print(row)

