from model_contact import InfoContact
import pytest


@pytest.fixture()
def work_to_infocontact():
    return InfoContact()


def test_collecting_contacts(work_to_infocontact):
    """Чтобы проверить данный тест, необходимо указать абсолютный путь к файлу:
    в модуле model_contact, класс InfoContact метод collecting_contacts,
    к примеру E:\PycharmProjects\phoneGuide_2\Guide.json"""
    if len(work_to_infocontact.collecting_contacts()) > 0:
        assert isinstance(work_to_infocontact.collecting_contacts(), list), 'Не актуальный тип'
    else:
        assert isinstance(work_to_infocontact.collecting_contacts(), str), 'Не актуальный тип'
