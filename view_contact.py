def show_contact(info):
    """Функция показа контактов в справочнике"""
    for elem_contact in info:
        print(f"id: {elem_contact['id']},"
              f" Имя: {elem_contact['name']},"
              f" Номер: {elem_contact['phone']},"
              f" Комментарий: {elem_contact['comment']}")


def show_search_contact(info):
    """Функция показа поиска результа контактов"""
    if isinstance(info, dict):
        for elem_contact in [info]:
            print(f"id: {elem_contact['id']},"
                  f" Имя: {elem_contact['name']},"
                  f" Номер: {elem_contact['phone']},"
                  f" Комментарий: {elem_contact['comment']}")
    else:
        print(info)


def announce_information(info):
    """Функция объявления информации"""
    print(info)
