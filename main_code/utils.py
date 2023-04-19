import json


def last_five(jsnlist="../operations.json"):
    """
    Получаем список словарей с нужным срезом и с выполенными операциями
    """
    json_list = open(jsnlist, encoding="utf-8")
    json_list_ = json_list.read()
    python_list = json.loads(json_list_)
    json_list.close()
    only_executed = [done for done in python_list if done["state"] == "EXECUTED"]
    last_executed = only_executed[-5:]
    return last_executed


def if_there_is_no_from_(last_executed):
    """
    функция обрабатывает и создаёт список словарей по принципу односторонней банковской операции"
    """
    if_there_is_no_from = []
    for data in last_executed:
        if "from" not in data.keys():
            data["to"] = f'Счёт **{data["to"][-4:]}'
            if_there_is_no_from.extend([{"date" : data["date"], "rest" :f'{data["description"]} \nСчёт **{data["to"][-4:]}\n'
                                 f'{data["operationAmount"]["amount"]} '
                                 f'{data["operationAmount"]["currency"]["name"]}\n'}])
    return  if_there_is_no_from


def account_to_account(last_executed):
    """
    функция обрабатывает и создаёт список словарей по принципу перевода со счёта на счёт
    """
    account_to_account_ = []
    for data in last_executed:
        if "from" in data.keys():
            cards_from = data["from"].split(" ")
            cards_to = data["to"].split(" ")
            if len(cards_from[1]) > 16 and len(cards_to[1]) > 16:
                account_to_account_.extend([{"date" : data["date"], "rest" :f'{data["description"]} \n{cards_from[0]} '
                                f'**{cards_from[1][-4:]} -> {cards_to[0]} **{cards_to[1][-4:]}\n'
                                f'{data["operationAmount"]["amount"]} '
                                f'{data["operationAmount"]["currency"]["name"]}\n'}])
    return account_to_account_

def card_to_account(last_executed):
    """
    функция обрабатывает и создаёт список словарей по принципу перевода с карты на счёт
    """
    card_to_account_ = []
    for data in last_executed:
        if "from" in data.keys():
            cards_from = data["from"].split(" ")
            cards_to = data["to"].split(" ")
            if len(cards_from[1]) == 16 and len(cards_to[1]) > 16:
                cards_from_ = cards_from[1].replace(cards_from[1][6:-4], "******")
                cards_from_with_spaces = f"{cards_from_[0:4]} {cards_from_[4:8]} " \
                                         f"{cards_from_[8:12]} {cards_from_[12:16]}"
                card_to_account_.extend([{"date" :data["date"], "rest" : f'{data["description"]}\n'
                                    f'{cards_from[0]} {cards_from_with_spaces}'
                                    f' -> {cards_to[0]} **{cards_to[1][-4:]}\n'
                                    f'{data["operationAmount"]["amount"]} '
                                    f'{data["operationAmount"]["currency"]["name"]}\n'}])
    return card_to_account_
