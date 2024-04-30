import psycopg2
import csv
from config import host, user, password, db_name

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

# 2-1
def insertfromcsv():
    with open("some.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            sql = f'''
                INSERT INTO phonebook(name, number) VALUES
                ('{row[0]}', '{row[1]}')
                '''
            cursor.execute(sql)

# 2-2
def insertdata():
    name = input("Name to insert ")
    number = input("Number to insert ")
    sql = f'''
   INSERT INTO phonebook(name, number) VALUES
   ('{name}', '{number}')
'''
    cursor.execute(sql)


# 3-1
def updatedatabynumber():
    find = input("Enter a number to find(<=11)")
    update = input("Enter a new name ")
    sql = f'''
    UPDATE phonebook SET name = '{update}' WHERE number = '{find}'
    '''
    cursor.execute(sql)  

# 3-2
def updatedatabyname():
    find = input("Enter a name to find: ")
    update = input("Enter a new number(<=11): ")
    sql = f'''
    UPDATE phonebook SET number(<=11) = '{update}' WHERE name = '{find}'
    '''
    cursor.execute(sql)


# 4
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


# 5
def deletedatabyname():
    find = input("Enter a name to delete: ")
    sql = f'''
    DELETE FROM phonebook WHERE name = '{find}';
    '''
    cursor.execute(sql)
    
# def deletedatabynumber():
#     find = input("Enter a number(<=11) to delete ")
#     sql = f'''
#     DELETE FROM phonebook WHERE number = '{find}';
#     '''
#     cursor.execute(sql)
    

        


if __name__ == '__main__':
    intro = """
    Number must be less than or equal 11!
    Commands:
          insert
          insert csv
          update by name
          update by number
          show
          delete by name
          exit 
          """
    print(intro)
    run = True
    while run:
        enter = input(str("Enter what you want to do: "))
        if enter == 'insert':
            insertdata()
        elif enter == 'insert csv':
            insertfromcsv()
        elif enter == 'update by name':
            updatedatabyname()
        elif enter == 'update by number':
            updatedatabynumber()
        elif enter == 'show':
            show()
        elif enter == 'delete by name':
            deletedatabyname()
        # elif enter == 'delete by number':
        #     deletedatabynumber()

        elif enter == 'exit':
            run = False
        else:
            print("Wrong input!")

    #  Closing connection
    cursor.close()
    conn.close()