
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print("Database opened successfully")

if conn and cursor:
    conn.execute('''CREATE TABLE IF NOT EXISTS USER(
        ID INT PRIMARY KEY  NOT NULL,
        NAME TEXT NOT NULL,
        EMAIL TEXT UNIQUE NOT NULL,
        PASSWORD TEXT NOT NULL
    );''')

    print('Table created successfully')

    
    def insert_to_db(conn,cur):
        id = input("Enter your ID:")
        name = input("Enter your name:")
        email = input("Enter your email:")
        password = input("Enter your password:")

        query = "INSERT INTO USER(ID,NAME,EMAIL,PASSWORD) VALUES(?,?,?,?)"
        query_tuple=(id,name,email,password)

        cur.execute(query,query_tuple)
        # conn.commit()

        print('Record inserted successfully')

    def delete_from_db(conn,cursor):
        email = input("Enter EMAIL:")
        query = "DELETE FROM USER WHERE EMAIL = ?"
        try:
            cursor.execute(query,[email])
            # conn.commit()
            print("Email deleted")
        except Exception as e:
            print(e)

    def update_db(conn,cursor):
        name = input("Enter name to update:")
        password = input("Enter password value:")
        email = input("Enter EMAIL:")
        try:
            query = ("UPDATE USER SET NAME = ?,PASSWORD = ?  WHERE EMAIL = ?")
            cursor.execute(query,[name,password,email])
            # conn.commit()
        except:
            print("Error")
        

    def select_from_db(conn,cursor):
        # clause_field = input("Enter Where column:")
        # value = input("Enter Where column value:")
        try:
            cur = cursor.execute("SELECT * FROM USER")# WHERE "+clause_field+" = "+value+");")
            # conn.commit()
        except:
            print("Error")
        else:
            if cur:
                for row in cursor:
                    print(str(row[0])+":"+str(row[1])+":"+str(row[2])+":"+str(row[3]))

    while(True):
        print("Enter 1:SELECT 2:INSERT 3:DELETE 4:UPDATE 5:EXIT\n")
        inp = int(input("Enter your choice:"))
        if inp == 1:
            select_from_db(conn,cursor)
        elif inp == 2:
            insert_to_db(conn,cursor)
        elif inp == 3:
            delete_from_db(conn,cursor)
        elif inp == 4:
            update_db(conn,cursor)
        elif inp == 5:
            conn.commit()
            conn.close()
            print("Goodbye")
            break
        else:
            print("Wrong choice")
            continue
    
else:
    print("Connection could not be opened")
