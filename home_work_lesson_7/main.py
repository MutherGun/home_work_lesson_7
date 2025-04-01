from home_work_lesson_7.funciones.name_check import is_name_valid
from home_work_lesson_7.funciones.age_check import is_adult
from home_work_lesson_7.users.users import users

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
    users.append(new_user)
    print("Registration succes!")

def create_user(username, age, email):
    if not is_name_valid(username):
        return{"success": False, "error": "User name must have atleast four characters."}
    if not is_adult(age):
        return{"success": False, "error": "User must be at least 18."}
    return{
        "success":True, "user":
            {"username": username, "age": age, "email": email}}

def print_user_info(user_result):
    if user_result["success"]:
        user = user_result["user"]
        print(f"user: {user['username']}, age: {user['age']}, email: {user['email']}")
    else:
        print(f"Error: {user_result['error']}")

user_result = create_user(name, age, email)

if user_result["success"]:
    users.append(user_result["user"])
    print("Registration success!")

user_list = [
            create_user("Jana", 25, "jana@jana.com"),
            create_user("AB", 20, "ab@ab.com"),
            create_user("Pepa", 17, "pepa@pepa.com"),
            create_user("Veronika", 30, "veronika@veronika.com")]

for user in user_list:
    print_user_info(user)

print("\nAll registered users:")
for u in users:
     print(list(u.values()))
