import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# ---------- Stretch Goal -----------
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is None
        if value is None:
            return
        # check if tree has a root
        if self.value is None:
            self.value = BSTNode(value)
        
        # insert in left or right
        if self.value >= value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target exists
        if target is None:
            return False
        
        # check if tree exists
        if self.value is None:
            return False
        
        # check all the other conditions
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                if self.left == target:
                    return True
                else:
                    return self.left.contains(target)
        elif self.value < target:
            if self.right:
                if self.right == target:
                    return True
                else:
                    return self.right.contains(target)

binarySearch = BSTNode(names_1[0])

for name1 in names_1:
    binarySearch.insert(name1)

for name2 in names_2:
    if binarySearch.contains(name2):
        duplicates.append(name2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.