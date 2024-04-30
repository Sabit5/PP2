import psycopg2
import csv
from config import host, user, password, db_name
from psycopg2 import Error
import re

# Connect to database
conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)
conn.autocommit = True

# Cursor
cursor = conn.cursor()


# Functions
# def createtable():
#     sql = '''
#         CREATE TABLE phone(
#         name CHAR(20),
#         number CHAR(12)
#     )
#     '''
#     cursor.execute(sql)


# 2
exists = False
def insertdata():
    global exists
    name = input("Name to insert ")
    number = input("Number to insert ")
    
    # to chech if it exists
    cursor.execute("SELECT * from phonebook where name = %s", (name,))
    result = cursor.fetchone()
    # print(result)
    if result:
        exists = True

    if exists == False:
        sql = f'''
        INSERT INTO phonebook(name, number) VALUES
        ('{name}', '{number}')
        '''
        cursor.execute(sql)
    elif exists == True: 
        cursor.execute("UPDATE phonebook SET number = %s WHERE name = %s", (number, name))


def insertfromcsv():
    with open("some.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            sql = f'''
                INSERT INTO phonebook(name, number) VALUES
                ('{row[0]}', '{row[1]}')
                '''
            cursor.execute(sql)


def updatedatabyname():
    find = input("Enter a name to find: ")
    update = input("Enter a new number(<=11): ")
    sql = f'''
    UPDATE phonebook SET number = '{update}' WHERE name = '{find}'
    '''
    cursor.execute(sql)
    
def updatedatabynumber():
    find = input("Enter a number to find(<=11)")
    update = input("Enter a new name ")
    sql = f'''
    UPDATE phonebook SET name = '{update}' WHERE number = '{find}'
    '''
    cursor.execute(sql)    


# 5
def deletedatabyname():
    find = input("Enter a name to delete: ")
    sql = f'''
    DELETE FROM phonebook WHERE name = '{find}';
    '''
    cursor.execute(sql)
    
def deletedatabynumber():
    find = input("Enter a number(<=11) to delete ")
    sql = f'''
    DELETE FROM phonebook WHERE number = '{find}';
    '''
    cursor.execute(sql)


# 1
def show():
    filter = input("What you need to find? write NAME or NUMBER: ")
    sql = f'''
    SELECT * FROM phonebook WHERE name LIKE '%{filter}%' OR number LIKE '%{filter}%'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        for i in result:
            print(i)
    else:
        print('There are none')


# 3
def add_users():
    contacts = []
    incorrect_values = []
    pattern = r'^\d{11}$'
    
    num_contacts = int(input("Enter the amount of contacts you want to add: "))
    
    for _ in range(num_contacts):
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts.append((name, number))

        # to chech if it exists
        cursor.execute("SELECT * from phonebook where name = %s", (name,))
        result = cursor.fetchone()
        # print(result)
        if result:
            exists = True
        else:
            exists = False
    
    try:
        for contact in contacts:
            if re.match(pattern, contact[1]):
                if exists:
                    cursor.execute("UPDATE phonebook SET number =%s WHERE name =%s ", (number, name))
                else:
                    cursor.execute('INSERT INTO phonebook(name, number) VALUES (%s, %s)', (contact[0], contact[1]))
            else:
                incorrect_values.append(contact)
                
    except (Exception, Error) as error:
        print("ERROR:", error)
    
    print(f'List of incorrect numbers is: {incorrect_values}')

# 4
def show_pagination():
    offset = int(input("Enter a start(included): "))-1
    limit = int(input("Enter an end(included): "))
    cursor.execute("SELECT * FROM phonebook OFFSET %s LIMIT %s", (offset, limit))
    result = cursor.fetchall()

    for i in result:
        print(i)



if __name__ == '__main__':
    intro = """
    Number must be less than or equal 11!
    Commands:
          insert
          add many users
          insert csv
          delete, update by name
          delete, update by number
          show
          show within
          exit 
          """
    print(intro)
    run = True
    while run:
        enter = input(str("Enter what you want to do: "))
        if enter == 'insert':
            insertdata()
        elif enter == 'delete by name':
            deletedatabyname()
        elif enter == 'delete by number':
            deletedatabynumber()
        elif enter == 'update by name':
            updatedatabyname()
        elif enter == 'update by number':
            updatedatabynumber()
        elif enter == 'show':
            show()
        elif enter == 'insert csv':
            insertfromcsv()
        elif enter == 'exit':
            run = False
        elif enter == 'add many users':
            add_users()
        elif enter == 'show within':
            show_pagination()
        else:
            print("Wrong input!")

    #  Closing connection
    cursor.close()
    conn.close()