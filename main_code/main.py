from datetime import datetime
from utils import if_there_is_no_from_, account_to_account, card_to_account, last_five


def joint_list(first, second, third):
    """
    получаем итоговый список словарей, в котором сортируем принт по дате и приводим дату в требуемый формат
    """
    joint_list_ = first + second + third
    joint_list_.sort(key=lambda d: d['date'])
    joint_list_.reverse()
    for data in joint_list_:
        date_formatted = datetime.fromisoformat(data["date"]).date().strftime("%d.%m.%Y")
        data["date"] = date_formatted
    for operation in joint_list_:
        for value in operation.values():
            print(value)


joint_list(if_there_is_no_from_(last_five()), account_to_account(last_five()), card_to_account(last_five()))
