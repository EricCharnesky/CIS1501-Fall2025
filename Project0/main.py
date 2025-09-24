import math

number_of_people_to_feed = int(input("How many guests are coming to the party?"))
number_of_people_to_feed += 1

serving_options_and_amount_consumed_per_person = {
    "pizza" : 1/3,
    "salad" : 1/4,
    "pop" : 3/8 }

choice = input(f'What are you serving? {tuple(serving_options_and_amount_consumed_per_person.keys())}')

while choice.lower() not in serving_options_and_amount_consumed_per_person:
    print("invalid choice")
    choice = input(f'What are you serving? {tuple(serving_options_and_amount_consumed_per_person.keys())}')

#
# amount_of_item_per_person = 0
# if choice == 'pizza':
#     amount_of_item_per_person = 1 / 3
# elif choice == 'salad':
#     amount_of_item_per_person = 1 / 4
# else:
#     amount_of_item_per_person = .75 / 2

amount_of_items_to_buy = math.ceil((number_of_people_to_feed *
                          serving_options_and_amount_consumed_per_person[choice]))

cost_per_item = float(input(f"How much does it cost for 1 {choice}"))

print(f"To serve {choice} to {number_of_people_to_feed} people at your lame party"
      f" will cost about ${cost_per_item*amount_of_items_to_buy:.2f} to buy {amount_of_items_to_buy} {choice}")