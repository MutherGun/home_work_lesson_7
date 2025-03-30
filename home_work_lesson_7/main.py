from home_work_lesson_7.funciones.name_check import is_name_valid
from home_work_lesson_7.funciones.age_check import is_adult
from home_work_lesson_7.users.users import user

while True:
    name = input("Enter user name:")
    if is_name_valid(name):
        break
    else:
        print("Name must have atleast four characters. ")

while True:
    age_input = input("Enter user age: ")

    try:
        age = int(age_input)
        if not is_adult(age):
            print("User must be at least 18.")
            print("Creating user FAILED!")
            exit()
        else:
            break
    except ValueError:
        print("Age must be a number.")

email = input("Enter email:")

if is_name_valid(name) and is_adult(age):
    new_user = {"name": name, "age": age, "email": email}
    user.append(new_user)
    print("Registration succes!")

for u in user:
    print(list(u.values()))