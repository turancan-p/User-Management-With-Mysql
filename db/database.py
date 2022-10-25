import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root ",
    passwd="1234",
    database="userdata"
)

my_cursor = db.cursor()

def login_check(username, password):
    command = f"SELECT userConfirmed from users WHERE userName = '{username}' AND userPassword = '{password}';"
    my_cursor.execute(command)

    for confirm in my_cursor:
        if confirm[0] == 1:
            return True
        else:
            return False