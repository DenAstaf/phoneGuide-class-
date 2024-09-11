import json
import re


class InfoContact:
    @staticmethod
    def collecting_contacts():
        """Функция сбора контактов в справочнике"""
        with open('Guide.json', 'r', encoding='utf-8') as file:
            obj_json = json.load(file)  # Десерилизует из файла json в объект
            if len(obj_json["Contacts"]) > 0:
                return obj_json["Contacts"]
            else:
                return "\n--Справочник пустой--"


class PhoneGuide:
    def __init__(self, name, phone, comment, id_contact):
        self.__name = name
        self.__phone = phone
        self.__comment = comment
        self.__id = id_contact

    def create_contact(self):
        """Функция создания контактов"""
        with open('Guide.json', 'r', encoding='utf-8') as file:  # Считывает данные из файла
            obj_json = json.load(file)  # Десерилизует из файла json в объект
            if len(obj_json["Contacts"]) != 0:  # Если данные в справочнике есть, то
                obj_json["Contacts"].reverse()  # Делает реверс списку, чтобы получить последний id
                id_contact = obj_json["Contacts"][0]["id"] + 1
            else:
                id_contact = 1  # Если контактов в справочнике нет, то id объекта = 1

        with open('Guide.json', 'w', encoding='utf-8') as file:  # Записывает данные в файл
            contact = {"id": id_contact,
                       "name": self.__name,
                       "phone": self.__phone,
                       "comment": self.__comment}  # Контакты объекта в формате словаря
            obj_json["Contacts"].reverse()  # Делает реверс списку, чтобы вернуть его в первоначальное положение
            obj_json["Contacts"].append(contact)  # Добавляются контакты в список
            (json.dump(obj_json, file, ensure_ascii=False))  # Серилизуются и записываются в файл

        return "\n--Данные успешно записаны в справочник--"

    def search_contact(self, search_criteria):
        """Функция поиска контактов"""
        continue_search = None  # Флаг выхода из цикла

        with open('Guide.json', 'r', encoding='utf-8') as file:  # Считывает данные из файла
            obj_json = json.load(file)  # Десерилизует из файла json в объект
            while continue_search != "нет":
                flag_result_search = False  # Флаг, показывает нашлись ли результаты

                # Проходится циклом по всей коллекции
                for elem_contact in obj_json["Contacts"]:
                    # Если аргумент фукнции all, то ищет по всем данным
                    if search_criteria == "all":
                        id_search = re.findall(fr'{self.__name.lower()}.*', str(elem_contact['id']).lower())
                        name_search = re.findall(fr'{self.__name.lower()}.*', elem_contact['name'].lower())
                        phone_search = re.findall(fr'{self.__name.lower()}.*', elem_contact['phone'].lower())
                        comment_search = re.findall(fr'{self.__name.lower()}.*', elem_contact['comment'].lower())

                        # Если нашел, то показывает все найденные данные
                        if len(id_search) != 0 or len(name_search) != 0 or len(phone_search) != 0 or len(
                                comment_search) != 0:
                            return elem_contact

                    # Если аргумент фукнции name, то ищет только по имени
                    else:
                        name_search = re.findall(fr'{self.__name.lower()}.*', elem_contact['name'].lower())

                        # Если нашел, то показывает все найденные данные
                        if len(name_search) != 0:
                            return elem_contact

                if not flag_result_search:
                    return "\n--Таких данных в справочнике нет--"

    def change_contact(self):
        """Функция изменения контактов в справочнике"""
        with open('Guide.json', 'r', encoding='utf-8') as file:
            obj_json = json.load(file)  # Десерилизует из файла json в объект

        id_contact = -1  # Содержит id контакта, который надо удалить

        # Получает id контакта в guide.json
        for id_loop in range(len(obj_json["Contacts"])):
            if obj_json["Contacts"][id_loop]['id'] == int(self.__id):
                id_contact = id_loop

        if 0 <= id_contact <= len(obj_json["Contacts"]):
            pass
        else:
            return "\n--Нет такого номера контакта--"

        if self.__name is not None:
            obj_json["Contacts"][id_contact]["name"] = self.__name
        elif self.__phone is not None:
            obj_json["Contacts"][id_contact]["phone"] = self.__phone
        elif self.__comment is not None:
            obj_json["Contacts"][id_contact]["comment"] = self.__comment

        with open('Guide.json', 'w', encoding='utf-8') as file:  # Записывает данные в файл
            (json.dump(obj_json, file, ensure_ascii=False))  # Серилизуются и записываются в файл

        return "\n--Данные успешно сохранены--"

    def del_contact(self):
        """Функция удаления контакта в справочнике"""
        # 1. Показывает все контакты
        with open('Guide.json', 'r', encoding='utf-8') as file:
            obj_json = json.load(file)  # Десерилизует из файла json в объект

            id_contact = -1  # Содержит id контакта, который надо удалить

            # Получает позицию нужного элемента в коллекции
            for id_loop in range(len(obj_json["Contacts"])):
                if obj_json["Contacts"][id_loop]['id'] == int(self.__id):
                    id_contact = id_loop
                    break

            # Удаляет элемент из коллекции
            if 0 <= id_contact <= len(obj_json["Contacts"]):
                if id_contact < len(obj_json["Contacts"]):
                    del obj_json["Contacts"][id_contact]
                else:
                    del obj_json["Contacts"][id_contact - 1]
            else:
                return "\n--Нет такого номера контакта--"

        with open('Guide.json', 'w', encoding='utf-8') as file:  # Записывает данные в файл
            json.dump(obj_json, file, ensure_ascii=False)  # Серилизуются и записываются в файл
            return "\n--Контакт успешно удален--"
