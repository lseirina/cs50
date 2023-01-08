from my_final_project import check_argv, text_emoji, count_princess
import pytest


def test_check_argv():
    with pytest.raises(SystemExit):
        check_argv()

def test_count_princess():
    assert count_princess(["Avrora","Avrora","Avrora","Bell", "Mulan", "Avrora"]) == "Your princess is Avrora"
    assert count_princess(["Mulan", "Bell", "Mulan", "Cinderella", "Ariel", "Mulan"]) == "Your princess is Mulan"
    assert count_princess(["Bell", "Bell", "Mulan", "Bell", "Ariel", "Mulan"]) == "Your princess is Bell"
    assert count_princess(["Cinderella", "Cinderella", "Mulan", "Cinderella", "Ariel", "Mulan"]) == "Your princess is Cinderella"
    assert count_princess(["Ariel", "Bell", "Ariel", "Cinderella", "Ariel", "Ariel"]) == "Your princess is Ariel"
    
def test_text_emoji():
    assert text_emoji("Your princess is Avrora")
    assert text_emoji("Your princess is Mulan")
    assert text_emoji("Your princess is Bell")
    assert text_emoji("Your princess is Cinderella")
    assert text_emoji("Your princess is Ariel")