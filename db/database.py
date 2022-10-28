import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root ",
    passwd="1234",
    database="userdata"
)

my_cursor = db.cursor()


def login_check(username, password):
    command = f"SELECT * from users WHERE userName = '{username}' AND userPassword = '{password}';"
    my_cursor.execute(command)

    for user in my_cursor:
        if user is not None:
            return True
        else:
            return False


def user_confirmed(username, password):
    command = f"SELECT userConfirmed from users WHERE userName = '{username}' AND userPassword = '{password}';"
    my_cursor.execute(command)

    for confirmation in my_cursor:
        if confirmation[0] == 1:
            return True
        else:
            return False


def save_user(userName, userPassword):
    select_command = f"SELECT * FROM users WHERE userName = '{userName}'"
    my_cursor.execute(select_command)
    for username in my_cursor:
        print(username)
        if username[0]:
            print("Username has allready used!")
            return False
        else:
            print("Kayıt Başlıyor")
    today = date.today()
    insert_command = f"INSERT INTO users (userName, userPassword, userRegisterDate, userAuthority, userConfirmed) VALUES (%s, %s, %s, %s, %s)"
    values = (userName, userPassword, today, "member", 0)
    my_cursor.execute(insert_command, values)
    db.commit()
    return True


def confirm_user(userID, confirm):
    update_command = f"UPDATE users SET userConfirmed = '{confirm}' WHERE userID = '{userID}'"
    my_cursor.execute(update_command)
    try:
        result = my_cursor.fetchall()
        print(result)
    except mysql.connector.Error as e:
        print("Error: ", e)


def get_data_for_table(confirm):
    try:
        command = f"SELECT * FROM users where userConfirmed = '{confirm}'"
        my_cursor.execute(command)
        result = my_cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print("Error: ", e)
