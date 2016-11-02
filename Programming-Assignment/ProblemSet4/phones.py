#%%    
"""
Problem 4_4:
This problem is to build on phones.py.  You add a new menu item
  r) Reorder
This will reorder the names/numbers in the phone list. This may sound difficult
at first thought, but it really is straight forward.  You need to add two
lines to the main_loop, one line to menu_choice to print out the new menu
option (and add 'r' to the list of acceptable choices).  In addition you
need to add a new function to do the reordering: I called my reorder_phones().
Here is a start for this very short function:

def reorder_phones():
    global phones       # this insures that we use the one at the top
    pass # replace this pass (a do-nothing) statement with your code


Note: The auto-grader will run your program, choose menu items s, r, s, and q
in that order.  It will provide an unsorted CSV file and see if your program
reorders it appropriately. The grader will provided a version of myphones.csv
that has a different set of names in it from the ones we used in the lesson.
But the result of this added function is shown using the names used in class.

Before:
Choice: s
     Name                     Phone Number 
  1  Jerry Seinfeld          (212) 842-2527
  2  George Costanza         (212) 452-8145
  3  Elaine Benes            (212) 452-8723
After:
Choice: s
     Name                     Phone Number 
  1  Elaine Benes            (212) 452-8723
  2  George Costanza         (212) 452-8145
  3  Jerry Seinfeld          (212) 842-2527

"""
import os
import csv


phones = []
name_pos = 0
phone_pos = 1
phone_header = [ 'Name', 'Phone Number']

def proper_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' needs to be the number of a phone!")
        return False
    which = int(which)
    if which < 1 or which > len(phones):
        print ("'" + str(which) + "' needs to be the number of a phone!")
        return False
    return True
    
def delete_phone(which):
    if not proper_menu_choice(which):
        return
    which = int(which)

    del phones[which-1]
    print( "Deleted phone #", which)

def edit_phone(which):
    if not proper_menu_choice(which):
        return
    which = int(which)
        
    phone = phones[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    
    print(phone[name_pos])
    newname = input("Enter phone name to change or press return: ")
    if newname == "":
        newname = phone[name_pos]
        
    print(phone[phone_pos])    
    newphone_num = input("Enter new phone number to change or press return: ")
    if newphone_num == "":
        newphone_num = phone[phone_pos]
            
    phone = [newname, newphone_num]
    phones[which-1] = phone

  
def save_phone_list():

    f = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()
  
def load_phone_list():
    if os.access("myphones.csv",os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()

def show_phones():
    show_phone(phone_header, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()

def show_phone(phone, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

def reorder_phones():
    global phones       # this insures that we use the one at the top
    pass # replace this pass (a do-nothing) statement with your code
    phones.sort()

def create_phone():
    print("Enter the data for a new phone:")
    newname = input("Enter name: ")
    newphone_num = input("Enter phone number: ")
    phone = [newname,newphone_num]
    phones.append(phone)
    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   r) Reorder")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['r','n','d', 's','e', 'q']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None


def main_loop():
    
    load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_phone()
        elif choice == 'd':
            which = input("Which item do you want to delete? ")
            print("which is ", which)
            delete_phone(which)
        elif choice == 's':
            show_phones()
        elif choice == 'r':
            reorder_phones()
        elif choice == 'e':
            which = input("Which item do you want to edit? ")
            print("which is ", which)
            edit_phone(which)
        else:
            print("Invalid choice.")
            
    save_phone_list()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
#%%
