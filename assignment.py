# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = [-1, -1, -1, -1, -1, -1, -1, -1]
TopOfStack = -1

def Push(Item):
    global Stack, TopOfStack
    if TopOfStack >= 7:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


def Pop():
    global Stack, TopOfStack
    if TopOfStack < 0:
        return -1
    Item = Stack[TopOfStack]
    TopOfStack -= 1
    return Item


# Exercise 2
def ShowStack():
    # Write your code here
    pass


# Exercise 3
def DecimalToBinary(Number):
    # Write your code here
    pass


# Exercise 4
def Editor(Commands):
    # Write your code here
    pass
