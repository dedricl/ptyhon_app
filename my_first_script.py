#Exercise-1

# apples = 2.50
# bread = 1.70
# cookies = 5.05
# total_cost =  apples + bread + cookies
#print(f"The total cost of your groceries is {total_cost}")

#Exercise-2

# Get input from user store response in a variable
#favorite_grocery_store = input("What is your favorite grocery store? ")

#Print message in the terminal with favorite_grocery_store variable.
#print("Welcome to " + favorite_grocery_store + "!")


#Exercise-3
milk = "3"
bread = 2.5
total = int(milk) + bread
#print("The total cost is: $" + str(total))


#Day 4
# num = int(input("Enter a number "))
# if num % 2 == 0:
#   print("even")
# else:
#   print("odd") 

# temp = float(input("Please enter a temperature in farenheit "))   
# if temp < 15:
#   print("Cold!")
# elif temp > 15 and temp < 25:
#   print("Warm")  
# else:
#   print("Hot")  

# 
# 
# groc = ['milk', 'apple', 'bread']
# # for item in groc:
# #   print(item) 
# item = input("Add a grocery item or type done when finish ") 

# while item != 'done':
#   groc.append(item)
#   item = input("Add a grocery item or type done when finish ") 
# print(groc)  

# groc_dict = [{'name': 'fish', 'cost': 1.12,}, {'name': 'milk', 'cost': 2.12}]
# for item in groc_dict:
#   print(f"Name is {item['name']} the cost is ${item['cost']}")

# groc_list = ['milk', 'cheese','paper', 'apple', 'paper', 'pear', 'paper', 'grape']
# not_groc = ['paper', 'pencil']
# new_list = []
# for item in groc_list:
#   if item  in not_groc:
    
#   else:
#     new_list.append(item)
# print(new_list)  
# num = input("please enter a num? ")
# try:
#    int(num)
#    print(num)
# except ValueError:
#    print("Error: please enter a valid number")

a = 10
b = 5

# Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
double_b = b * 2

# Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
total = a + double_b

# print("The total is:", total)

#EXERCISE 1
# food_items = ['chicken', 'candy', 'apples']
# non_food_items = ['toothpaste', 'soap', 'cups']
# groc_item = input("Please type in a grocery item! ")
# if groc_item in food_items:
#   print("It's a food item!")
# elif groc_item in non_food_items:
#   print("It's a household item")
# else:
#   print("Unknown item")  

#EXERCISE 2:, #EXERCISE 3:, #EXERCISE 4:, #EXERCISE 5:, #EXERCISE 6: 

items_list = [
    {"name": "onion rings", "cost":6.79, "amount": 1},
    {"name": "hot dogs", "cost":5.99, "amount": 1},
    {"name": "hot dog buns", "cost":3.99, "amount": 1},
    {"name": "mustard", "cost":1.50, "amount": 2},
    {"name": "american cheese", "cost":5.79, "amount": 1},
    {"name": "ketchup", "cost":2.47, "amount": 1},
    {"name": "onions", "cost":3.00, "amount": 1}
]


shopping_list = []
budget = 27.50
total_cost = 0
index = 0
while total_cost <= budget:
  try:
    item = items_list[index]
  except:
    print("The index must be an integer")
    break  
  shopping_list.append(item['name'])
  total_cost += item['cost'] * item['amount']
  index += 1
  for item in shopping_list:
    print(item)    
  if 'hot dog buns' in shopping_list and 'onion rings' in shopping_list and 'hot dogs' in shopping_list:  
    print("----------")
    print(f"We can make hotdogs and onion rings for {round(total_cost,2)}")
    break
  print("----------")  
print(shopping_list)  






    