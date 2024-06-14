'''
Began writing on 6 May 2024, Finished on 14 June 2024
Written by Alex Yao 22177
This python application is used to access information from a database. The database can be viewed and edited through 
this python application by displaying options that the user can select with numbers 
to navigate throughout the database.
'''

# imports
import sqlite3
# constants and variable
DATABASE = "clashroyale_database.db"
user_input = ''
# functions
def search_cards(): # this will open up a menu to search for cards
    '''opens up a menu to search for cards'''
    print("Please type the corresponding number, then press Enter.")
    user_input = input('''1. Print all Cards
2. Print all Goblin related cards
3. Print all Skeleton related cards
4. Print all troops that die to Zap
5. Print all troops that die to The Log
6. Print all troops that die to Fireball
7. Print all troops that die to Poison
8. Print all troops that die to Lightning
9. Print all Buildings
10. Print all Spells
11. Print all Troops\n''')
    if user_input == "1": # proccesses user input
        print_all_cards()  # after it redirects you to the corresponding function
    elif user_input == "2":
        print_all_goblins() # if input is 2, it redirects you to this function
    elif user_input == '3':
        print_all_skeletons() # if input is 3, it redirects you to this function
    elif user_input == "4":
        print_all_cards_that_die_to_zap() #if input is 4, it redirects you to this function
    elif user_input == "5":
        print_all_cards_that_die_to_log() #if input is 5, it redirects you to this function
    elif user_input == "6":
        print_all_cards_that_die_to_fireball() # if input is 6, it redirects you to this function
    elif user_input == "7":
        print_all_cards_that_die_to_poison() # if input is 7, it redirects you to this function
    elif user_input == "8":
        print_all_cards_that_die_to_lightning() # if input is 8, it redirects you to this function
    elif user_input == "9":
        print_all_buildings() # if input is 9, it redirects you to this function
    elif user_input == "10":
        print_all_spells() # if input is 10, it redirects you to this function
    elif user_input == "11":
        print_all_troops() # if input is 11, it redirects you to this function
    else:
        print("") 
        print("INVALID INPUT, PLEASE TRY AGAIN\n") # if none of the input is valid, it prints this message
        search_cards() # this then redirects you back to the menu to re-enter an input

def print_all_cards():
    '''prints all cards nicely'''
    db = sqlite3.connect(DATABASE) #connects to database
    cursor = db.cursor()
    sql = "SELECT * FROM card;" # sql statement
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID") # columns so user can understand the numbers
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}") # spits out numbers in loop
    db.close()
    print("Command successfully executed")
    main_menu() #redirects user to the main menu after the query has been executed


def print_all_goblins():
    '''prints all goblin card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE name LIKE '%goblin%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_skeletons():
    '''prints all skeleton card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE name LIKE '%Skeleton%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_cards_that_die_to_zap():
    '''prints all zappable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '192' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_cards_that_die_to_log():
    '''prints all loggable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '290' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_cards_that_die_to_fireball():
    '''prints all fireballable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '689' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_cards_that_die_to_poison():
    '''prints all poisonable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '728' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_cards_that_die_to_lightning():
    '''prints all lightningable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '1056' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_buildings():
    '''prints all building card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '2';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_spells():
    '''prints all spell card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '3';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def print_all_troops():
    '''prints all troop cards'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()
    
def edit_data():
    '''Brings up a menu where user can edit the database'''
    print("Please type the corresponding number, then press Enter.")
    user_input = input('''1. Add data
2. Remove data
3. Update existing data\n''')
    if user_input == "1":
        add_data()
    elif user_input == "2":
        remove_data()
    elif user_input == "3":
        update_data()
    else:
        print("INVALID INPUT, PLEASE TRY AGAIN")
        edit_data()

def add_data():
    '''Brings up step by step instructions for users to input their new card'''
    while True: # loop to continue to loop through until input is valid
        name = input('What is the name of the card?\n')
        if name.replace(" ","").isalpha(): # this makes it so only letters and spaces are allowed
            break  # breaks loop so user can continue
        else:
            print("Please enter a valid card name using only letters and spaces.") # prints this then loops back if input contains numbers
    
    while True:
        try:
            elixir = int(input('How much does it cost?\n'))
            if elixir > 0 and elixir <10: # only allows input that is a number between 1-10
                break # breaks loop so user can continue
            else:
                print("Please enter a positive whole number between 1-10.")
        except ValueError: 
            print("Please enter positive whole number.") # prints this then loops back if input is not a number
    
    while True: # loop to continue to loop through until input is valid
        try:
            hp = int(input(f"What is the hp of {name}?\n"))
            if hp > 0: # this makes it only allows input above 0
                break # breaks loop so user can continue
            else:
                print("Please enter a positive whole number.")
        except ValueError: # prints this then loops back if input is not a number
            print("Please enter a positive whole number.")
    
    while True: # loop to continue to loop through until input is valid
        try:
            dmg = int(input("How much damage does it deal?\n"))
            if dmg > 0: # this makes it only allows input above 0
                break # breaks loop so user can continue
            else: # prints this and loops back if input is below 0
                print("Please enter a positive whole number.")
        except ValueError: 
            print("Please enter a positive whole number") # prints this and loops back if input isn't a number
    
    while True: # loop to continue to loop through until input is valid
        try:
            attack_speed = float(input(f"What is the attack speed of {name}?\n"))
            if attack_speed > 0: # only accept input above 0
                break # breaks loop so user can continue
            else:
                print("Please enter a positive number.") # prints this and loops back if input is below 0
        except ValueError:
            print("Please enter a positive number.")  # prints this and loops back if input isn't a number
    
    while True: # loop to continue to loop through until input is valid
        try:
            type_id = int(input(f'''\nWhat is the card type of {name}?
1. Troop
2. Building
3. Spell
Please enter the number corresponding to the card type:\n'''))
            if type_id in [1, 2, 3]: #only accepts number 1, 2, 3
                break #breaks loops so user can continue
            else:
                print("Please enter a valid option.") # prints this loops back is input is not 1, 2, 3
        except ValueError:
            print("Please enter a valid number") #prints and loops back if input isnt a number

    while True: # loop to continue to loop through until input is valid
        try:
            rarity_id = int(input(f'''\nWhat is the rarity of {name}?
1. Common
2. Rare
3. Epic
4. Legendary
5. Champion
Please enter the number corresponding to the rarity:\n''')) # will trigger error if input isnt an int
            if rarity_id in [1, 2, 3, 4, 5]: #allows input that is 1, 2, 3, 4, 5
                break #breaks so user can continue
            else:
                print("Please enter a valid option.") # prints this and loops back if input isnt in the list
        except ValueError:
            print("Please enter a valid number") # prints this and loops back if input isnt an integar

    while True: # loop to continue to loop through until input is valid
        try:
            speed = int(input(f'''\nWhat is the speed of {name}?
1. Slow
2. Medium
3. Fast
4. Very Fast
5. Stationary
6. None
Please enter the number corresponding to the card speed:\n''')) # 
            if speed in [1, 2, 3, 4, 5, 6]: # proccesses input to make sure it if one of the options
                if speed == 1:
                    speed = "Slow"
                elif speed == 2:
                    speed = "Medium"
                elif speed == 3:
                    speed = "Fast"
                elif speed == 4:
                    speed = "Very Fast"
                elif speed == 5:
                    speed = "Stationary"
                elif speed == 6:
                    speed = "None"
                break # if input is valid, this wil break and let user continue
            else:
                print("Please enter a valid option.") # if the input is a number that is outside of the list
        except ValueError:
            print("Please enter a valid number") # prints this message and loops back if the input isnt a number

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = '''INSERT INTO card (type_id, rarity_id, dmg, elixir, speed, hp, attack_speed, name) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (type_id, rarity_id, dmg, elixir, speed, hp, attack_speed, name))
    db.commit() # commits so new card is saved
    db.close()
    print(f"{name} was successfully added to the database")
    main_menu() # redirects the user to main menu once the item is added
    
def remove_data():
    '''Brings up way for user to enter a way to remove a card via their ID'''
    id = input("What is the ID of the card you would like to remove?\n")
    if id.isnumeric(): # only accepts input that is a number
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = f'''DELETE FROM card WHERE card_id = "{id}"'''
        cursor.execute(sql)
        db.commit()
        db.close()
        print("Item was successfully removed")
    else:
        print("Please enter a whole number.")
        remove_data()
    main_menu() # redirects user back to main menu once the item is removed

def update_data():
    '''Brings up instructions where the user can select a column and card to update'''
    while True: # loops to keep looping until valid input is entered
        try:
            id = int(input("What is the ID of the card you want to update?\n"))
            if id > 0: #only accepts input that is above 0
                break #breaks loop so user can continue when a valid input is received
            else:
                print("Please enter a positive whole number.") # prints this then loops back if input is below 0
        except ValueError:
            print("Please enter positive whole number.") # prints this then loops back if input was not a number
    while True:
        try:
            column = int(input('''\nWhat column would you like to update?
1. Type ID
2. Rarity ID
3. Damage
4. Elixir
5. Speed
6. HP
7. Attack Speed
8. Name
Please enter the number corresponding to each column:\n'''))
            if column in [1, 2, 3, 4, 5, 6, 7, 8]: # only accepts input from the numbers in the list
                if column == 1: 
                    column = "type_id" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = int(input('''\nWhat will be the updated card type?
1. Troop
2. Building
3. Spell
Please enter the number corresponding to the card type:\n'''))
                            if change in [1, 2, 3]:
                                break
                            else:
                                print("Please enter a valid option.")
                        except ValueError:
                            print("Please enter a valid number")
                elif column == 2:
                    column = "rarity_id"  # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = int(input(f'''\nWhat will be the new updated rarity?
1. Common
2. Rare
3. Epic
4. Legendary
5. Champion
Please enter the number corresponding to the rarity:\n'''))
                            if change in [1, 2, 3, 4, 5]:
                                break
                            else:
                                print("Please enter a valid option.")
                        except ValueError:
                            print("Please enter a valid number")
                elif column == 3:
                    column = "dmg" # changes variable to the corresponding column
                    while True: #loop to keep looping until valid input is entered
                        try:
                            change = int(input("What will be the new damage?\n"))
                            if change > 0: #only accepts input that is above 0
                                break #breaks loop so user can continue when a valid input is received
                            else:
                                print("Please enter a positive whole number.") #prints this and loops back if input is below 0
                        except ValueError:
                            print("Please enter a positive whole number")
                elif column == 4:
                    column = "elixir" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = int(input("What will the new cost be?\n"))
                            if change > 0: # only accepts input above 0
                                break #breaks loop so user can continue when a valid input is received
                            else:
                                print("Please enter a positive whole number less than 10.") # prints this and loops back if input isnt between 1-10
                        except ValueError:
                            print("Please enter a positive whole number.") #prints and loops back if input isnt a number
                elif column == 5:
                    column = "speed" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = int(input('''\nWhat will the new speed be?
Please enter the corresponding number, the press enter
1. Slow
2. Medium
3. Fast
4. Very Fast
5. Stationary
6. None
Please enter the number corresponding to the card speed:\n'''))
                            if change in [1, 2, 3, 4, 5, 6]: #allows input that is in the list
                                if change == 1:
                                    change = "Slow"
                                elif change == 2:
                                    change = "Medium"
                                elif change == 3:
                                    change = "Fast"
                                elif change == 4:
                                    change = "Very Fast"
                                elif change == 5:
                                    change = "Stationary"
                                elif change == 6:
                                    change = "None"
                                break #breaks loop so user can continue once a valid input is received
                            else:
                                print("Please enter a valid option.") # prints this and loops back if input isnt between 1-6
                        except ValueError:
                            print("Please enter a valid number") #prints this and loops if input isnt a number
                elif column == 6:
                    column = "hp" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = int(input(f"What will be the new hp?\n"))
                            if change > 0: #only allows input that is above 0
                                break  # breaks loop so user can continue when a valid input is received
                            else:
                                print("Please enter a positive whole number.")  # prints this and loops back if input is negative
                        except ValueError:
                            print("Please enter a positive whole number.")
                elif column == 7:
                    column = "attack_speed" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        try:
                            change = float(input(f"What will be the new attack speed?\n"))
                            if change > 0: # only allow input above 0
                                break # breaks loop so user can continue once a valid input is received
                            else:
                                print("Please enter a positive number.") # prints this and loops back if input is below 0
                        except ValueError:
                            print("Please enter a positive number.") # prints this and loops back if input isnt a number
                elif column == 8:
                    column = "name" # changes variable to the corresponding column
                    while True:   #loop to keep looping until valid input is entered
                        change = input('What will be the updated name?\n')
                        if change.replace(" ","").isalpha(): #this makes it so input consists of only letters and spaces
                            break # breaks loop so user can continue once a valid input is received
                        else:
                            print("Please enter a valid card name using only letters.") # loops back if input contains numbers or symbols
                break # breaks loops so user can procceed after all instructions are satisfed
            else:
                print("Please enter a valid option.") # loops back if the number entered was invalid
        except ValueError:
            print("Please enter a valid number") # loops back if input is a letter
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f'''UPDATE card SET {column} = "{change}" WHERE card_id = {id};'''
    cursor.execute(sql)
    db.commit()   # commits so data is saved
    db.close()
    print("Update has been successfully saved")
    main_menu() # redirects user back to main menu
    
# maincode
print("Hello! Welcome to Alex Yao's Clash Royale Database.")
def main_menu():
    '''This is the first thing the user will see and is where all of the sub menus can be accessed'''
    print("\n")
    print("What would you like to do?")
    print("Please type the corresponding number, then press Enter.")
    print('''
    1. Search cards
    2. Edit data
    3. Rarity and Type ID Information
    4. Exit''')

    valid_response = False # this variable willl change and break loop
    user_input = input()

    while valid_response == False:
        if user_input == "1":
            valid_response = True
            search_cards()
        elif user_input == "2":
            valid_response = True
            edit_data()
        elif user_input == "3":
            valid_response = True
            print("Each number corresponds to each rarity and type")
            print('''Rarity:
1 - Common
2 - Rare
3 - Epic
4 - Legendary
5 - Champion\n''')
            print('''Type:
1 - Troop
2 - Building
3 - Spell''')
            main_menu() # loops back to main menu
        elif user_input == "4":
            valid_response = True
            print("CLOSING PROGRAMME . . .")
            print("Thanks for using Alex Yao's Clash Royale Database! :)") # closes programme
        else:
            user_input = input("That is not a valid response, please try again\n")
main_menu()

# MegaNUTTY nUtNut
#justiceforclashmini
#saveclashmini
#nolevel15
#DONEZO