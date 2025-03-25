"""

person = {"Имя": "Алиса", "возраст": 30 }
person ["город"] = "Москва"
#del person ["возраст"]
#print(person["Имя"])
print("город" in person)
person = {
    "имя": "Алиса",
    "возраст": 30,
    "адрес": {
        "город": "Москва",
        "улица": "Тверская"
    }
}
print(person["адрес"] ["город"])

person = {
    "имя": "Алиса",
    "возраст": 30,
    "хобби": ["путешествия", "фотография", "чтение"]
}
person["хобби"].append("рисование")
print(person["хобби"][1])

name = "Алиса"
age = 30

person = {
    "имя": name,
    "возраст": age
}
print(person["имя"])
print(person["возраст"])


print(person["хобби"])

person["адрес"] ["город"] = "Санкт-Петербург"
print(person["адрес"] ["город"])

person["хобби"].remove("чтение")
print(person["хобби"])
del person["возраст"]
print(person)

coordinates = (10, 20, 30)
print(coordinates[1])
"""
"""
# original_list = [1, 2, 3]
# print("Исходный список:", original_list)  # Выведет: [1, 2, 3]
# reference = original_list
# print("вторая ссылка на список:", reference)
# 
# reference.append(4)
# print("второй список, который ссылется на первый:", original_list)
# print("ID исходного списка:", id(original_list))
# print("ID второй сылки на список:", id(another_reference))
# """
# original = [5, 4, 3]
# copy_from_originale = original.copy()
#
# copy_from_originale.append(6)
#
# print("наш первый список", original)
# print('список чtрез метод .copy()', copy_from_originale)
#
# print('id 1', id(original))
# print("id copy", id(copy_from_originale))


# person = {'name': 'Alice', 'age': 17}
# person['cite'] = 'moskou'
# person.apend
# del person['age']
# print(person)

# list = [1, 11, 111, 231, 1312, 321, 21, 3419]
# list.append('43132')
# list.remove(1)
# list[1] = 'xer'
# print(len(list))
student = {'name': 'ivan', 'age': 20}
student['grade'] = 'a'
student['grade'] = 'b'
del student['age']
print(student['name'])