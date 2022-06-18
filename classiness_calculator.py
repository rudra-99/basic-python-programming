# """You can use this class to represent how classy someone
# or something is.
# "Classy" is interchangable with "fancy".
# If you add fancy-looking items, you will increase
# your "classiness".
# Create a function in "Classy" that takes a string as
# input and adds it to the "items" list.
# Another method should calculate the "classiness"
# value based on the items.
# The following items have classiness points associated
# with them:
# "tophat" = 2
# "bowtie" = 4
# "monocle" = 5
# Everything else has 0 points.
# Use the test cases below to guide you!"""
#################################################################################


class Classy(object):
    def __init__(self):
        self.items = []
        
    #addItem is a function to add items to the list. I have used a different approach here.
    #Instead of adding the items back to the list self.items, I added the values 
    # corresponding to the items. Returning the sum of the integer matrix is easier.  
    def addItem(self,item):
        if item=="tophat":
            self.items.append(2)
        elif item=="bowtie":
            self.items.append(4)
        elif item=="monocle":
            self.items.append(5)
    #here getClassiness just take the argument and returns  the sum of the elements
    # present in the matrix self.items every time the function is called.
    def getClassiness(self):
        return sum(self.items)
# Test cases
me = Classy()


# Should be 0
print(me.getClassiness())

item1=me.addItem("tophat")
# Should be 2
print (me.getClassiness())

item2=me.addItem("bowtie")
item3=me.addItem("jacket")
item4=me.addItem("monocle")
# Should be 11
print (me.getClassiness())

item5=me.addItem("bowtie")
# Should be 15
print (me.getClassiness())
