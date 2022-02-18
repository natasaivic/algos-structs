"""
You must implement the count_low_high() function. Its parameter is a list of numbers.
If a number is greater than 50 or divisible by 3, it will count as a high. 
If these conditions are not met, the number is considered a low.
At the end of the function, you must return a list that contains the number of lows and highs, in that order. 
In case the list is empty, you may return None.
"""

def count_low_high(num_list):
    if len(num_list) == 0:
        return None
    new_list = []
    count_high=0
    count_low=0
    for i in num_list:
        if num_list[i] > 50 or num_list[i] % 3 == 0:
            count_high += 1
        count_low += 1
    new_list.append(count_low)
    new_list.append(count_high)
    
    return new_list 


# Solution 2: Using filter and lambda
def count_low_high_2(num_list):
    if len(num_list == 0):
        return None
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]


# Solution 3: Using list comprehension
# Following the list comprehension syntax, specify the element to be inserted into the new list, 
# a for loop which iterates the current list, and a condition that needs to be fulfilled.
def count_low_high_3(num_list):
    if len(num_list == 0):
        return None
    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
    return [low_list, high_list]


lista = [10,20,30,40,50,60,70,80,90]
num_list = [-10, 90, 15, 43]
print(count_low_high(lista))