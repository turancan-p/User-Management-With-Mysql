import mysql.connector
from cryptography.fernet import Fernet
import bcrypt
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root ",
    passwd="1234",
    database="userdata"
)

db_cursor = db.cursor()


def create(username, password):
    command = f"SELECT * from users WHERE userName = '{username}';"
    db_cursor.execute(command)
    try:
        result = db_cursor.fetchall()

        passw = result[0][2]
        print(passw)
        salt = result[0][7]
        salt = str.encode(salt)
        utf_pw = password.encode('utf-8')
        hashed = bcrypt.hashpw(utf_pw, salt)
        if bcrypt.checkpw(passw, hashed):
            return True
        else:
            return False

    except mysql.connector.Error as e:
        print("Error: ", e)


def login_check(username, password):
    command = f"SELECT * from users WHERE userName = '{username}';"
    db_cursor.execute(command)
    try:
        result = db_cursor.fetchall()
        db.commit()
        passw = result[0][2]
        print(passw)
        salt = result[0][7]
        salt = str.encode(salt)
        utf_pw = password.encode('utf-8')
        hashed = bcrypt.hashpw(utf_pw, salt)
        print(hashed)
        if str(hashed) == passw:
            print(1)
            return True
        else:
            print(2)
            return False

    except mysql.connector.Error as e:
        print("Error: ", e)


def user_confirmed(username):
    command = f"SELECT userConfirmed from users WHERE userName = '{username}';"
    db_cursor.execute(command)

    for confirmation in db_cursor:
        if confirmation[0] == 1:
            return True
        else:
            return False


def save_user(userName, userPassword, today = None, authority = None, confirmation = None):
    select_command = f"SELECT * FROM users WHERE userName = '{userName}'"
    db_cursor.execute(select_command)
    for username in db_cursor:
        print(username)
        if username[0]:
            print("Username has allready used!")
            return False
        else:
            print("Kayıt Başlıyor")
    if today == None:
        today = date.today()
    if authority == None:
        authority = "Member"
    if confirmation == None:
        confirmation = 0

    insert_command = f"INSERT INTO users (userName, userPassword, userRegisterDate, userAuthority, userConfirmed, passwordKey) VALUES (%s, %s, %s, %s, %s, %s)"
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(userPassword.encode('utf-8'), salt)

    values = (userName, str(hashed), today, authority, confirmation, salt)
    db_cursor.execute(insert_command, values)
    db.commit()
    return True


def confirm_user(userID, confirm):
    update_command = f"UPDATE users SET userConfirmed = '{confirm}' WHERE userID = '{userID}'"
    db_cursor.execute(update_command)
    try:
        result = db_cursor.fetchall()
        print(result)
    except mysql.connector.Error as e:
        print("Error: ", e)


def get_data_for_table(confirm):
    try:
        command = f"SELECT * FROM users where userConfirmed = '{confirm}'"
        db_cursor.execute(command)
        result = db_cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Error: ", e)


def get_all_data_for_table():
    try:
        command = f"SELECT * FROM users"
        db_cursor.execute(command)
        result = db_cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Error: ", e)
