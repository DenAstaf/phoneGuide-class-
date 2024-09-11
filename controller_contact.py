from model_contact import InfoContact
from model_contact import PhoneGuide
from view_contact import show_contact
from view_contact import show_search_contact
from view_contact import announce_information


class ControllerContact:
    @staticmethod
    def __exit_from_guide():
        """Функция выхода в главное меню или полностью из справочника"""
        exit_menu = input("\nВыйти в главное меню - 1\n"
                          "Выйти из справочника - 2\n")

        while True:
            if exit_menu.isdigit() and 1 <= int(exit_menu) <= 2:
                if exit_menu == "1":
                    return input("Нажмите цифру желаемого действия:\n"
                                 "Показать контакты - 1\n"
                                 "Создать контакт - 2\n"
                                 "Найти контакт - 3\n"
                                 "Изменить контакт - 4\n"
                                 "Удалить контакт - 5\n"
                                 "Выход - 6\n")
                else:
                    return True
            else:
                exit_menu = input("\nВыйти в главное меню - 1\n"
                                  "Выйти из справочника - 2\n")

    def work_to_phoneguide(self):
        work_to_phone_guide = input("Открыть справочник (да/нет) ")

        if work_to_phone_guide == "да":

            menu = input("Нажмите цифру желаемого действия:\n"
                         "Показать контакты - 1\n"
                         "Создать контакт - 2\n"
                         "Найти контакт - 3\n"
                         "Изменить контакт - 4\n"
                         "Удалить контакт - 5\n"
                         "Выход - 6\n")

            close_from_phone_guide = False  # Флаг выхода из цикла while
            data = None  # Содержит значение функции exit_from_guide

            while not close_from_phone_guide:

                if menu.isdigit() and 1 <= int(menu) <= 6:

                    if menu == "1":
                        info_contact_lst = InfoContact.collecting_contacts()  # Контролер получает список из model, содержащий в себе словарь со всеми контактами
                        show_contact(info_contact_lst)  # Контроллер передает данные во вьюху, для отоброжения контактов
                        data = self.__exit_from_guide()  # содержит значение: продолжить или выйти

                    elif menu == "2":
                        name = input("Задайте имя контакта: ")
                        phone = input("Задайте телефон контакта: +")
                        comment = input("Добавьте комментарий к контакту: ")

                        while True:
                            save_contact = input("Сохранить контакт (да/нет): ")

                            if save_contact.isalpha() and save_contact == "да" or save_contact == "нет":
                                if save_contact == "да":
                                    phone_guide = PhoneGuide(name, phone, comment, id_contact=None)  # Экземпляр класса PhoneGuide
                                    result = phone_guide.create_contact()  # Контролер дает задачу model создать контакт и вернуть результат создания контакта
                                    announce_information(result)  # Контроллер передает данные во вьюху, для отоброжения результата создания контакта
                                    data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                    break
                                else:
                                    announce_information("\n--Сохранение контакта отменено--")
                                    data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                    break
                            else:
                                announce_information("\n--Необходимо вводить актуальные значения--")

                    elif menu == "3":
                        while True:
                            select_search = input("Выберите желаемый поиск:\n"
                                                  "По всем параметрам - 1\n"
                                                  "По имени - 2\n")

                            if select_search.isdigit() and 1 <= int(select_search) <= 2:
                                search_word = input("введите данные для поиска: ")
                                phone_guide = PhoneGuide(name=search_word, phone=None, comment=None, id_contact=None)  # Экземпляр класса PhoneGuide

                                if select_search == "1":
                                    result = phone_guide.search_contact(search_criteria="all")  # Контролер дает задачу model найти контакт
                                    show_search_contact(result)  # Контроллер передает данные во вьюху, для отоброжения результата поиска контакта
                                elif select_search == "2":
                                    result = phone_guide.search_contact(search_criteria="name")  # Контролер дает задачу model найти контакт
                                    show_search_contact(result)  # Контроллер передает данные во вьюху, для отоброжения результата поиска контакта

                                continue_search = input("\n--Продолжить поиск? (да/нет)-- ")

                                if continue_search.isalpha() and continue_search == "нет":
                                    data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                    break
                                elif continue_search.isalpha() and continue_search == "да":
                                    continue
                                else:
                                    while continue_search != "да" and continue_search != "нет":
                                        announce_information("\n--Введите актуальные данные--")
                                        continue_search = input("Продолжить поиск? (да/нет) ")

                                    if continue_search == "нет":
                                        data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                        break

                            else:
                                announce_information("\n--Введите актуальные данные--")

                    elif menu == "4":
                        info_contact_lst = InfoContact.collecting_contacts()  # Контролер получает список из model, содержащий в себе словарь со всеми контактами
                        show_contact(info_contact_lst)  # Контроллер передает данные во вьюху, для отоброжения контактов
                        name_change = ""
                        phone_change = ""
                        comment_change = ""
                        phone_guide = None

                        remove_contact_id = input("\nВведите id контакта, который вы хотите изменить: ")

                        while True:
                            if remove_contact_id.isdigit():
                                break
                            else:
                                announce_information("\n--Не актуальные данные--")
                                remove_contact_id = input("\nВведите id контакта, который вы хотите изменить: ")

                        while True:
                            select_change = input("\nВыберите где внести изменения:\n"
                                                  "Имя - 1\n"
                                                  "Телефон - 2\n"
                                                  "Комментарий - 3\n")
                            if select_change.isdigit() and select_change == "1":
                                name_change = input("Введите желаемое имя: ")
                                break
                            elif select_change.isdigit() and select_change == "2":
                                phone_change = input("Введите желаемый телефон: +")
                                break
                            elif select_change.isdigit() and select_change == "3":
                                comment_change = input("Введите желаемый комментарий: ")
                                break
                            else:
                                announce_information("\n--Введите актуальные данные--")

                        flag_save_change = False
                        while not flag_save_change:
                            save_change = input("Сохранить изменения (да/нет) : ")

                            if save_change.isalpha() and save_change == "да" or save_change == "нет":
                                if save_change == "да":
                                    if name_change != "":
                                        phone_guide = PhoneGuide(name=name_change, phone=None, comment=None,
                                                                 id_contact=remove_contact_id)  # Экземпляр класса PhoneGuide
                                    elif phone_change != "":
                                        phone_guide = PhoneGuide(name=None, phone=phone_change, comment=None,
                                                                 id_contact=remove_contact_id)  # Экземпляр класса PhoneGuide
                                    elif comment_change != "":
                                        phone_guide = PhoneGuide(name=None, phone=None, comment=comment_change,
                                                                 id_contact=remove_contact_id)  # Экземпляр класса PhoneGuide

                                    result = phone_guide.change_contact()  # Контролер дает задачу model изменить контакт
                                    announce_information(result)
                                else:
                                    announce_information("\n--Изменение в контакте отменено--")
                                flag_save_change = True
                            else:
                                announce_information("\n--Введите актуальное значение--")

                        data = self.__exit_from_guide()  # содержит значение: продолжить или выйти

                    elif menu == "5":
                        info_contact_lst = InfoContact.collecting_contacts()  # Контролер получает список из model, содержащий в себе словарь со всеми контактами
                        show_contact(info_contact_lst)  # Контроллер передает данные во вьюху, для отоброжения контактов

                        remove_contact = input("\nВведите id контакта, который вы хотите удалить (0 - отменить удаление): ")

                        while True:
                            if remove_contact.isdigit() and remove_contact != "0":
                                phone_guide = PhoneGuide(name=None, phone=None, comment=None,
                                                         id_contact=remove_contact)  # Экземпляр класса PhoneGuide

                                result = phone_guide.del_contact()  # Контролер дает задачу model удалить контакт
                                announce_information(result)
                                data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                break
                            elif remove_contact == "0":
                                announce_information("\n--Удаление отменено--")
                                data = self.__exit_from_guide()  # содержит значение: продолжить или выйти
                                break
                            else:
                                announce_information("\n--Не актуальные данные--")
                                remove_contact = input(
                                    "Введите id контакта, который вы хотите удалить (0 - отменить удаление): ")

                    elif menu == "6":
                        close_from_phone_guide = True

                    if isinstance(data, str):  # Если фукция типа str, то присваеваем menu значение данной функции
                        menu = data
                    else:
                        close_from_phone_guide = True  # Если bool, то значит пользователь запросил выход из справочника

                else:
                    announce_information("\nВведите актуальное значение:\n")
                    menu = input("Нажмите цифру желаемого действия:\n"
                                 "Показать контакты - 1\n"
                                 "Создать контакт - 2\n"
                                 "Найти контакт - 3\n"
                                 "Изменить контакт - 4\n"
                                 "Удалить контакт - 5\n"
                                 "Выход - 6\n")

        else:
            announce_information("\nВы ввели не актуальные данные, до встречи!")
