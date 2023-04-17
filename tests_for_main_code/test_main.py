from main_code.main import last_five, edited_list_

def test_last_five():
    assert len(last_five()) == 5
    assert last_five()[0]["date"] == "2019-07-15T11:47:40.496961"
    for dict_list in last_five():
        assert "CANCELED" not in dict_list["state"]


def test_edited_list():
    assert "15.07.2019" in edited_list_(last_five())[0]
    assert "19.05.2019" in edited_list_(last_five())[2]
    assert "05.01.2019" in edited_list_(last_five())[3]
    assert "Счёт **2265" in edited_list_(last_five())[0]
    assert "МИР 5211 27** ****" in edited_list_(last_five())[2]
    assert "руб." in edited_list_(last_five())[4]
