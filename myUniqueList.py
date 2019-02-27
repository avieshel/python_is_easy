myUniqueList = []
myLeftovers = []

def add(item):
    if item not in myUniqueList:
        myUniqueList.append(item)
        return True
    else:
        myLeftovers.append(item)
        return False

#Test
assert (add("first")) is True, 'added "first" string unique element'
assert (add("second")) is True, 'added "second" string unique element'
assert (add("first")) is False, 'added "first" string which already exists'
assert (add(1)) is True, 'added unique integer'
assert (add(-1)) is True, 'added unique integer'
assert (add(-1)) is False, 'added integer which already exists'

print('Unique list: ', myUniqueList)
print('Rejected items list: ', myLeftovers)
