# create record
# update record
# read record
# delete record
# CRUD

# find user

import os
import validation

user_db_path = "data/user_record/"

def create(user_account_number, user_details):

    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ",txt", "x")

    except FileExistsError:
        print("user already exist")

    else:

        f.write(str(user_details))
        completion_state = True

    finally:
        f.close()

        return completion_state



def read(user_account_number):

    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:

        if user_account_number:
            f = open(user_db_path + str(user_account_number) + ",txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")


    except FileNotFoundError:

        print("user not found")
    except TypeError:
        print('invalid account number format')

    except FileExistsError:

        print("user doesn't exist")

    else:
        return f.readline()

    return False


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_account_number):

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")

            is_delete_successful = True

        except FileNotFoundError:

            print("user not found")

        finally:

            return is_delete_successful


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True

    return False

    print(does_email_exist('Stanniss@ymail.com'))

        # print(read(user))
        # print("\n")
        # print('user printed -->')
        # print(user)
        # print("\n")

# print(read(6854781320))
# print(read(9074451830))

def does_account_number_exist(user_account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(user_account_number) + ",txt":

            return True
    return False

def does_password_exist(password):
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == (password):

            return True
    return False

def authenticate_user(user_account_number, password):
    if does_account_number_exist(user_account_number):
        if does_password_exist(password):
            
            user = str.split(read(user_account_number), ',')
        #if password == user_details[3]:
         #   return user

    return False


