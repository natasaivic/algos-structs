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
    if new_list == [0, 0]:
        return None
    return new_list 

lista = [10,20,30,40,50,60,70,80,90]
num_list = [-10, 90, 15, 43]
print(count_low_high(lista))