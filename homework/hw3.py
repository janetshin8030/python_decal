#1
print("broken power rule")
result=1
a=int(input("name a:"))
b=int(input("input b:"))
while (b>0):
    result*=a
    b-=1
print(result)

#2
print("weather readings")
##HELP
readings = [15, 14, 17, 20, 23, 28, 20]
def temperature_range():
    high= int(min(readings))
    low=int(max(readings))
    print(low, high)
temperature_range()
##why doesn't this print?

#3
print("is today a weekday or weekend?")
x=int(input("what number day is it: "))
def weekdays():
    if x>=6:
        print("is weekend")
    elif 1<=x<=5:
        print ("is weekday")
    else:
        print("that's not a day")
weekdays()

#4
print("fuel efficiency calculator")
distance= float(input("distance:"))
fuel= float(input("gallons:"))
def fuel_efficiency():
    efficiency= distance/ fuel
    print(efficiency)
fuel_efficiency()

#5 WHY DIDN"T THIS WORK BEFORE
print("last digit to front")
def move_last_digit_to_front(x):
    last_digit= x%10
    remaining_sum= x // 10
    temp= remaining_sum
    digit_count= 0
    while temp >0:
        temp//=10
        digit_count +=1
    result=(last_digit*10**digit_count + remaining_sum)
    return result

x=int(input("enter number:"))
print(f"result: {move_last_digit_to_front(x)}")

#6
print("min/max finder")
nums = [2024, 98, 131, 2, 3, 72]
def find_minimum():
    minimum= nums[0]
    for num in nums:
        if num< minimum:
            minimum =num
    print(minimum)
find_minimum()
def find_maximum():
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum= num
    print(maximum)
find_maximum()

def whilefindmax():
    i=1
    while i < len(nums):
        maximum= nums[0]
        if nums[i] > maximum:
            maximum = nums[i]
    print(maximum)
whilefindmax()

def whilefindmin():
    t=1
    while t < len(nums):
        if nums[t] < minimum:
            minimum= nums[t]
    print(minimum)
whilefindmax()

#7
print("vowel/consonant count")
phrase= input("enter a phrase:")
vowel=["a","e","i","o","u"]
consonant= ["b","c",'d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def count_vowels(phrase):
    vowel_count=0
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in vowel:
                vowel_count+=1
    return vowel_count #why does this spacing matter??

def count_consonants(phrase):
    consonant_count= 0
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in consonant:
                consonant_count +=1
    return consonant_count
vowel_count= count_vowels(phrase)
consonant_count =count_consonants(phrase)

print(f"there are {vowel_count} vowels and {consonant_count} consonants in the phrase")

#8
print("calculate digital root")
num=input("enter number:")
my_num_list= []
for digit in num:
    if digit.isdigit():
        my_num_list.append(int(digit))
def adding_digits(my_num_list):
    starting_num = sum(my_num_list)
    return starting_num
starting_num=adding_digits(my_num_list)
print(starting_num)

     




    


