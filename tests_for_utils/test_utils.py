from main_code.utils import last_five, if_there_is_no_from_, account_to_account, card_to_account


def test_last_five():
    assert len(last_five()) == 5
    for dict_list in last_five():
        assert "CANCELED" not in dict_list["state"]


def test_if_there_is_no_from():
    for data in if_there_is_no_from_(last_five()):
        assert "Счёт **2265" in data["rest"]


def test_account_to_account():
    for data in account_to_account(last_five()):
        assert "Счет **3262" or "Счет **3262" in data["rest"]


def test_card_to_account():
    for data in card_to_account(last_five()):
        assert "МИР 5211" or "Maestro 1308" in data["rest"]
