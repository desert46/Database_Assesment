'''docstring'''

#imports
import sqlite3
# constants and variable
DATABASE = "clashroyale_database.db"
user_input = ''
# functions
def search_cards():
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
    if user_input == "1":
        print_all_cards()
    elif user_input == "2":
        print_all_goblins()
    elif user_input == '3':
        print_all_skeletons()
    elif user_input == "4":
        print_all_cards_that_die_to_zap()
    elif user_input == "5":
        print_all_cards_that_die_to_log()
    elif user_input == "6":
        print_all_cards_that_die_to_fireball()
    elif user_input == "7":
        print_all_cards_that_die_to_poison()
    elif user_input == "8":
        print_all_cards_that_die_to_lightning()
    elif user_input == "9":
        print_all_buildings()
    elif user_input == "10":
        print_all_spells()
    elif user_input == "11":
        print_all_troops()
    else:
        print("")
        print("INVALID INPUT, PLEASE TRY AGAIN\n")
        search_cards()

def print_all_cards():
    '''prints all cards nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()
    print("Command successfully executed")
    main_menu()


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
    while True:
        name = input('What is the name of the card?\n')
        if name.replace(" ","").isalpha():
            break
        else:
            print("Please enter a valid card name using only letters and spaces.")
    
    while True:
        try:
            elixir = int(input('How much does it cost?\n'))
            if elixir > 0:
                break
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter positive whole number.")
    
    while True:
        try:
            hp = int(input(f"What is the hp of {name}?\n"))
            if hp > 0:
                break
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter a positive whole number.")
    
    while True:
        try:
            dmg = int(input("How much damage does it deal?\n"))
            if dmg > 0:
                break
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter a positive whole number")
    
    while True:
        try:
            attack_speed = float(input(f"What is the attack speed of {name}?\n"))
            if attack_speed > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a positive number.")
    
    while True:
        try:
            type_id = int(input(f'''\nWhat is the card type of {name}?
1. Troop
2. Building
3. Spell
Please enter the number corresponding to the card type:\n'''))
            if type_id in [1, 2, 3]:
                break
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            rarity_id = int(input(f'''\nWhat is the rarity of {name}?
1. Common
2. Rare
3. Epic
4. Legendary
5. Champion
Please enter the number corresponding to the rarity:\n'''))
            if rarity_id in [1, 2, 3, 4, 5]:
                break
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            speed = int(input(f'''\nWhat is the speed of {name}?
1. Slow
2. Medium
3. Fast
4. Very Fast
5. Stationary
6. None
Please enter the number corresponding to the card speed:\n'''))
            if speed in [1, 2, 3, 4, 5, 6]:
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
                break
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid number")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = '''INSERT INTO card (type_id, rarity_id, dmg, elixir, speed, hp, attack_speed, name) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (type_id, rarity_id, dmg, elixir, speed, hp, attack_speed, name))
    db.commit()
    db.close()
    print(f"{name} was successfully added to the database")
    main_menu()
    
def remove_data():
    name = input("What is the name of the card you would like to remove? (Your input is case sensitive!)\n")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f'''DELETE FROM card WHERE name = "{name}"'''
    cursor.execute(sql)
    db.commit()
    db.close()
    print(f"{name} was successfully removed")

def update_data():
    while True:
        try:
            id = int(input("What is the ID of the card you want to update?\n"))
            if id > 0:
                break
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter positive whole number.")
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
            if column in [1, 2, 3, 4, 5, 6, 7, 8]:
                if column == 1:
                    column = "type_id"
                    while True:
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
                    column = "rarity_id"
                    while True:
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
                    column = "dmg"
                    while True:
                        try:
                            change = int(input("What will be the new damage?\n"))
                            if change > 0:
                                break
                            else:
                                print("Please enter a positive whole number.")
                        except ValueError:
                            print("Please enter a positive whole number")
                elif column == 4:
                    column = "elixir"
                    while True:
                        try:
                            change = int(input("What will the new cost be?\n"))
                            if change > 0:
                                break
                            else:
                                print("Please enter a positive whole number.")
                        except ValueError:
                            print("Please enter positive whole number.")
                elif column == 5:
                    column = "speed"
                    while True:
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
                            if change in [1, 2, 3, 4, 5, 6]:
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
                                break
                            else:
                                print("Please enter a valid option.")
                        except ValueError:
                            print("Please enter a valid number")
                elif column == 6:
                    column = "hp"
                    while True:
                        try:
                            change = int(input(f"What will be the new hp?\n"))
                            if change > 0:
                                break
                            else:
                                print("Please enter a positive whole number.")
                        except ValueError:
                            print("Please enter a positive whole number.")
                elif column == 7:
                    column = "attack_speed"
                    while True:
                        try:
                            change = float(input(f"What will be the new attack speed?\n"))
                            if change > 0:
                                break
                            else:
                                print("Please enter a positive number.")
                        except ValueError:
                            print("Please enter a positive number.")
                elif column == 8:
                    column = "name"
                    while True:
                        change = input('What will be the updated name?\n')
                        if change.replace(" ","").isalpha():
                            break
                        else:
                            print("Please enter a valid card name using only letters.")
                break
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid number")
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f'''UPDATE card SET {column} = "{change}" WHERE card_id = {id};'''
    cursor.execute(sql)
    db.commit()
    db.close()
    print(f"Update has been successfully saved")
    main_menu()
    
def custom_search():
    column = input("What would ")

def main_menu():
    print("\n")
    print("What would you like to do?")
    print("Please type the corresponding number, then press Enter.")
    print('''
1. Search cards
2. Edit data
3. Custom Search
4. Exit\n''')
    valid_response = False
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
            print("Coming soon")
        elif user_input == "4":
            valid_response = True
            print("Closing Programme")
            print("Thanks for using Alex Yao's Clash Royale Database! :)")
        else:
            user_input = input("That is not a valid response, please try again\n")
    
# maincode
print("Hello! Welcome to Alex Yao's Clash Royale Database.")
def main_menu():
    print("\n")
    print("What would you like to do?")
    print("Please type the corresponding number, then press Enter.")
    print('''1. Search cards
    2. Edit data
    3. COMING SOON
    4. Exit''')

    valid_response = False
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
            print("Coming soon")
        elif user_input == "4":
            valid_response = True
            print("Closing Programme")
            print("Thanks for using Alex Yao's Clash Royale Database! :)")
        else:
            user_input = input("That is not a valid response, please try again\n")
main_menu()
 
# Lettuce go
# MegaNUTTY nUtNut