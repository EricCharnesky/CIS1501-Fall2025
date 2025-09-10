temperature = int(input("What's the temperature?"))

# found how to lowercase input from http://.....
weather = input("What's the weather like? (sunny, rainy, cloudy)").lower()

if temperature > 60:
    print("You don't need a jacket")
    if weather == 'sunny':
        print("Dont forget the sun screen")
    elif weather == 'rainy':
        print("Bring your umbrella")
else:
    print("You should have a hoodie")
    print("more advice from dad")

print("have a great wednesday!")

score = int(input("Enter your score 1-100"))

if score > 93:
    print("A")
elif score >= 90:
    print("A-")
elif score > 86:
    print("B+")
elif score > 83:
    print("B")
else:
    print("F")

if score > 93:
    print('A')
if 90 < score <= 93:
    print("A-")
if 93 >= score >= 90:
    print("A-")
if score <= 93 and score >= 90:
    print("A-")

# true and true == true
# true and false == false
# false and true == false
# false and false == false

# true or true == true
# true or false == true
# false or true == true
# false or false == false


print("Hope you like your score")
