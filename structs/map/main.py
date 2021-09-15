from map import Map

# Custom Map
m = Map()
m.put('a', 0)
m.put('b', 1)
m.put('c', 2)
m.put('d', 3)
m.put('e', 4)
m.put('f', 5)

assert m.get('a') == 0
assert m.get('b') == 1
assert m.get('c') == 2
assert m.get('d') == 3
assert m.get('e') == 4
assert m.get('f') == 5

m.delete('b')
assert m.get('b') is None
assert m.get('a') is not None
assert m.get('a') == 0

# Python Map/Dict
n = {}
n['a'] = 0 # put 
n['b'] = 1 # put 

assert n.get('a') == 0
assert n.get('b') == 1
