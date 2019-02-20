def areAtLeastTwoEqaul(x, y, z):
    # convert the input to integer values
    num1 = int(x)
    num2 = int(y)
    num3 = int(z)
    if (num1 == num2 or num2 == num3 or num1 == num3):
        return True
    return False

# Tests
# print(areAtLeastTwoEqaul(1,2,3) , "should be false")
# print(areAtLeastTwoEqaul(1,1,2) , "Should be true ")
# print(areAtLeastTwoEqaul(1,2,1) , "should be true")
# print(areAtLeastTwoEqaul(2,1,1) , "should be true")

# print(areAtLeastTwoEqaul("1", 1, 2), "should be true")