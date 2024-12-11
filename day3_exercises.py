movies = ["Star Wars","Titanic","Gladiator","Batman","King Kong"]
movies.append("Dumb and Dumber")
movies.remove("Titanic")
numbers = [10, 20, 30, 40, 50]
colors = ["red", "green","blue"]
colors.insert(1,"yellow")
colors.append("purple")

dimensions = (70,10,50)
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
fruits = ('apple', 'banana')
vegetables = ('carrot', 'lettuce')
#print(fruits + vegetables)

book = {'title': "New Day", 'author': "Sam Pam", 'age': 30}

profile = {'name': 'Frank Ocean', 'age':22, 'city': 'New York'}
profile['city'] = "Bronz"

student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
student.pop("subject")

fruits = {"pear", "banana", "grape"}
fruits.add("orange")
fruits.remove("banana")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_x = {'cat', 'dog', 'fish'}
set_y = {'dog', 'bird'}
#print(set_x.difference(set_y))

#EXERCISE 1: Creating a Grocery List with Tuples
cheeses_tuple = ("America cheese", 2.25, 50)
milk_tuple = ("2% milk", 1.99, 2)
bread_tuple = ("Whole wheat", 1.20, 2)

grocery_list = []
grocery_list.append(cheeses_tuple)
grocery_list.append(milk_tuple)
grocery_list.append(bread_tuple)

# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[2])

# print(f"Total cost of {grocery_list[0][0]} is {grocery_list[0][1] * grocery_list[0][2]}")
# print(f"Total cost of {grocery_list[1][0]} is {grocery_list[1][1] * grocery_list[1][2]}")
# print(f"Total cost of {grocery_list[2][0]} is {grocery_list[2][1] * grocery_list[2][2]}")

#EXERCISE 2: Working with Dictionaries

eggs_dict = {'name':'egg', "price": 1.25, "quanity": 11}
eggs_dict['total_cost'] = eggs_dict['price'] * eggs_dict['quanity'] 
print(f"The total cost of eggs is  ${round(eggs_dict['total_cost'],2)}")

jello_dict = {'name':'jello', "price": 0.53, "quanity": 16}
jello_dict['total_cost'] = jello_dict['price'] * jello_dict['quanity'] 
print(f"The total cost of jello is  ${round(jello_dict['total_cost'],2)}")

hot_dogs_dict = {'name': 'hot dog', "price": 3.07, "quanity": 2}
hot_dogs_dict['total_cost'] = hot_dogs_dict['price'] * hot_dogs_dict['quanity'] 
print(f"The total cost of hotdogs is  ${round(hot_dogs_dict['total_cost'],2)}")

#EXERCISE 3: Slicing and Sorting a List

num_list = [16, 47, 1, 3, 5, 9, 15, 2]

print(num_list[1:])
print(num_list[:4])
print(num_list[-3])
num_list.sort(reverse=True)
print(num_list)
print(len(num_list))

#EXERCISE 4: Sets Operations
dairy_set = {'milk', 'bread', 'cream', 'yogurt', 'cheese'}
desserts_set = {'jello', 'chocolate', 'caandy', 'cookies', 'muffins'}
dairy_set.add('ice_cream')
desserts_set.add('ice_cream')
dairy_set.remove('milk')
desserts_set.remove('muffins')
print(dairy_set.intersection(desserts_set))