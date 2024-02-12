from library import Library
from time import sleep
# creating a method to clean console
import os
CLEAR_COMMAND = 'cls' if os.name=='nt' else 'clear'
clear = lambda: os.system(CLEAR_COMMAND)

# library object
lib = Library()

# functions to call according to user input
options = [
	lib.list_books, # 0
	lib.add_book, # 1
	lib.remove_book # 2
]

# menu loop
clear()
while True:
    print(
"""
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
4) Quit
"""
)
    q = int(input("Please select an option: "))

    if q == 4:
        del lib
        break
    elif q > 0 and q < 4:
        clear()
        options[q-1]()
    else:
        clear()
        print("Hatalı giriş!")