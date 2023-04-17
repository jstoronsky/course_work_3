import json
from datetime import datetime


def last_five(jsnlist="/home/jstoronsky/course_work_3/operations.json"):
    json_list = open(jsnlist, encoding="utf-8")
    json_list_ = json_list.read()
    python_list = json.loads(json_list_)
    json_list.close()
    only_executed = [done for done in python_list if done["state"] == "EXECUTED"]
    last_executed = only_executed[-5:]
    last_executed.sort(key=lambda d: d['date'])
    last_executed.reverse()
    return last_executed


def edited_list_(last_executed):
    edited_list = []
    for data in last_executed:
        date_formatted = datetime.fromisoformat(data["date"]).date().strftime("%d.%m.%Y")
        if "from" not in data.keys():
            edited_list.extend([f'{date_formatted} {data["description"]} \nСчёт **{data["to"][-4:]}\n'
                                f'{data["operationAmount"]["amount"]} '
                                f'{data["operationAmount"]["currency"]["name"]}\n'])
        else:
            cards_from = data["from"].split(" ")
            cards_to = data["to"].split(" ")
            if len(cards_from[1]) > 16 and len(cards_to[1]) > 16:
                edited_list.extend([f'{date_formatted} {data["description"]} \n{cards_from[0]} '
                                    f'**{cards_from[1][-4:]} -> {cards_to[0]} **{cards_to[1][-4:]}\n'
                                    f'{data["operationAmount"]["amount"]} '
                                    f'{data["operationAmount"]["currency"]["name"]}\n'])
            elif len(cards_from[1]) == 16 and len(cards_to[1]) > 16:
                cards_from_ = cards_from[1].replace(cards_from[1][6:-4], "******")
                cards_from_with_spaces = f"{cards_from_[0:4]} {cards_from_[4:8]} " \
                                         f"{cards_from_[8:12]} {cards_from_[12:16]}"
                edited_list.extend([f'{date_formatted} {data["description"]}\n'
                                    f'{cards_from[0]} {cards_from_with_spaces}'
                                    f' -> {cards_to[0]} **{cards_to[1][-4:]}\n'
                                    f'{data["operationAmount"]["amount"]} '
                                    f'{data["operationAmount"]["currency"]["name"]}\n'])
    return edited_list


def eventual_print(edited_list):
    for operation in edited_list:
        print(operation)


eventual_print(edited_list_(last_five()))
