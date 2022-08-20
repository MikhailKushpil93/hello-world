# Напишите код, который запрашивает у пользователя три имени и три возраста. 
# После ввода имен и возрастов запросите у пользователя одно из имен и выведите 
# # соответствующий возраст.

name_and_age = {}

count = 0 
while count < 3:
    count2 = count + 1
    name = input(f"Ведить ім'я {count2}: ")
    name_and_age[name] = input("Ведить вік: ")
    count += 1

print(name_and_age)

one_name = input("Найти ім'я: ")

print("Вік " + one_name +" : " + name_and_age[one_name])

