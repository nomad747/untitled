__author__ = 'louran'
import os


print("test")

os.getcwd()
mylist = [i for i in range(1,8)]
mylist.append(1)
mylist.extend([1, 4, 4])

myset = set(mylist)
[print(i) for i in myset]