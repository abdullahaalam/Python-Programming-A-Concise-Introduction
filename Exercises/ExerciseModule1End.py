# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:11:51 2016

@author: Abdullah A. Alam
"""

# - ExerciseModule1End.py *- coding: utf-8 -*-
""" Find and correct all the errors in the following Python functions. 
    Upload your file. """
""" 
Exercise 1 
"""
#%%
def print_phrase():
    phrase = "Now is the time"
    print (phrase)
#%%
""" 
Exercise 2
"""
#%%
def favorite_sport(favorite):
    sport = "favorite"
    print("Your favorite sport is",sport)
#%%
""" 
Exercise 3 
"""
#%%
def username(yourname):
    print("Your name is ",yourname)
#%%
"""
Exercise 4
"""
#%%
def compare_numbers(x,y):
    if x == y:
        print("they are equal")
    else:
        print(x, "and", y, 'are not equal')
#%%
"""
Exercise 5
"""
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print ('Count from 5 to 100 in steps of 5')
    ct = 5
    while ct <= 100:
        print(ct, end = " ")
        ct = ct + 5
    print()
#%%