#Introduction to Lists
#examples of lists
nums=[1,2,3,4,5,6,7,8,9,10]
planets=["mercury", "earhttps://bcourses.berkeley.edu/files/89895428/download?download_frd=1th"]
mixed= [1, "python", True, 3.14]
nested= [[1,2],[[3,4]]]
empty= []
print(nums[0])

# add elements at the end of a list with .append()
nums.append(11)
print(nums)

#add elements at the end of a list with index
planets.insert(1,"venus")
print(planets)

#modify/change at specific index
nums[1] = 222
print(nums)

#delete with the .remove()
#delete with the .pop()
planets.remove("mercury")
print(planets)
planets.pop(0)
print(planets)

# introduction to dictionaries
fourth_planet= {
    "name": "Mars",
    "moons": ["Phobos", "Deimos"],
    "Diameter_km": 6337,
    "atmosphere": False
}
print(fourth_planet["moons"])
#another way to get the same thing
print(fourth_planet.get("moons"))
#modify a dictionary
fourth_planet["atmosphere"] = True
print (fourth_planet)

#add to a dictionary
fourth_planet["color"] = "Red"

#remove from a dictionary
fourth_planet.pop("name")
print(fourth_planet)
del fourth_planet["moons"]
print(fourth_planet)

#Concatenating
list1=[1,2,3]
list2= [4,5,6]
list3= list1+list2
print(list3)
print(list1+list2)

#appending lists (you're nesting them)
list1.append(list2)
print(list1)

#slicing
numbers = [1,2,3,4,5,6,7]
print(numbers[1:5])
#doesn't count the last value

#striding
# [start:stop:step]
stride_nums = numbers[::2]
print(stride_nums)
reverse_nums= numbers[::-1]
print(reverse_nums)
funky_nums= numbers[2:7:2]
print(funky_nums)

#Enumerating
for index, value in enumerate(mixed):
    print(index, value)

#converting input to strings
my_string = "hello"
my_list = list(my_string)
print(my_list)

unsorted_list = [3,1,4,5,9]
unsorted_list.sort()
print(unsorted_list)

#example
desserts = ["cookie", "icecream", "brownie", "candy"]
c_words= []

for dessert in desserts:
    if dessert.startswith("c"):
        c_words.append(dessert.upper())
print(c_words)
#one line
words_c= [dessert.upper() for dessert in desserts if dessert.startswith("c")]
print(words_c)

#example dictionary questions
fav_num= {
    "Alice": [5,101,66],
    "Bob": [7,23,111],
    "Chuck": [26,82,84]
}

average_nums = {name: sum(num) / len(num)  for name, num in fav_num.items()}
print (average_nums)