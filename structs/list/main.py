from list import List

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

# Test is_empty()
assert my_list.is_empty() == False
my_list2 = List()
assert my_list2.is_empty() == True
print("PASS List.is_empty()")

print("SUCCESS")
