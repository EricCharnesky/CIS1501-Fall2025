alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])

print(alphabet[0:3])
print(alphabet[11:16])
print(alphabet[:])
print(alphabet[:3])
print(alphabet[22:])
print(alphabet[22:-1])
print(alphabet[5:-10])

# stride - count by
print(alphabet[::2])
print(alphabet[1::2])

print(alphabet[25::-1])




def convert_phone_number(phone_number):
    letter_to_number = {'ABC' : "2", 'DEF' : "3", 'GHI' : '4',
                        'JKL' : '5', 'MNO' : '6', "PQRS" : '7',
                        'TUV' : '8', 'WXYZ' : '9' }

    for letters, number in letter_to_number.items():
        for letter in letters:
            phone_number = phone_number.replace(letter, number)

    return phone_number

phone_number = "1-800-CALL-SAM"
print(phone_number)
phone_number = convert_phone_number(phone_number)
print(phone_number)

def print_values_in_upper_case(some_list):
    for index in range(len(some_list)):
        some_list[index] = some_list[index].upper()
        print(some_list[index])

names = ['Eric', 'Jasmine', 'Jeb', 'Vivi' ]

# can also slice lists, it creates a copy
print_values_in_upper_case(names[:])
print(names)

