from list import List

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Test expected value
assert my_list.__repr__() == "1 -> 2 -> 3 -> None"

# Test find() 
assert my_list.find(9) == False
assert my_list.find(2) == True

# Test delete()
my_list.delete(1)
assert my_list.find(1) == False

# Test append()
assert my_list.find(4) == False
my_list.append(4)
assert my_list.find(4) == True

print("TEST PASS")