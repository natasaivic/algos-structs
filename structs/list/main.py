from list import List, Node

print("STARTING TEST")
my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Test expected value
assert my_list.__repr__() == "1 -> 2 -> 3 -> None"
print("PASS List.__repr__()")

# Test find() 
assert my_list.find(9) == False
assert my_list.find(2) == True
print("PASS List.find()")

# Test delete()
my_list.delete(1)
assert my_list.find(1) == False
print("PASS List.delete()")

# Test append()
assert my_list.find(4) == False
my_list.append(4)
assert my_list.find(4) == True
print("PASS List.append()")

# Test prepend()
my_list.prepend(6) 
my_list.prepend(5) 
assert my_list.__repr__() == "5 -> 6 -> 2 -> 3 -> 4 -> None"
print("PASS List.prepend()")

# Test find_nth()
assert my_list.find_nth(1) == 5
print("PASS List.find_nth()")

# Test find_nth_last()
assert my_list.find_nth_last(2) == 3
print("PASS List.find_nth_last()")

# Test find_middle()
assert my_list.find_middle() == 2
print("PASS List.find_middle()")

# Test replace()
my_list.replace(6,9) 
assert my_list.__repr__() == "5 -> 9 -> 2 -> 3 -> 4 -> None"
print("PASS List.replace()")

# Test suma()
my_list.suma() 
assert my_list.suma() == 23
print("PASS List.suma()")

# Test is_empty()
assert my_list.is_empty() == False
my_list2 = List()
assert my_list2.is_empty() == True
print("PASS List.is_empty()")

print("SUCCESS")
