import sqlite3 as db


conn = db.connect('accounts.db')
c = conn.cursor()


def init():
    
    # initialize a new table to store date

    c.execute('''CREATE TABLE IF NOT EXISTS passmanege (
                topic TEXT,
                username TEXT,
                password TEXT
                ) ''')
    conn.commit()
    conn.close() 


def add(topic , username,password):

    # add new items to database    

    c.execute('INSERT INTO passmanege VALUES (:topic , :username , :password)' , {'topic' : topic , 'username' : username , 'password' : password}) 
    conn.commit()
    conn.close()        


def remove(topic , username , password):

    # remove items from database    

    c.execute('DELETE FROM passmanege VALUES(:name , :username , :password)' , {'name' : name , 'username' : username , 'password' : password}) 
    conn.commit()
    conn.close()


def show(topic=None):

    #Show the all date in database

    if topic: 
        c.execute('SELECT * FROM passmanege WHERE topic = (:topic )' , {'topic' : topic})
        results = c.fetchall()
        if results is None:
            print('None')

        else:
            pass

    else:
        c.execute('SELECT * FROM passmanege')
        results = c.fetchall()
        if results is None:
            print('None')

        else:
            pass

    return results
        
    conn.close()    
