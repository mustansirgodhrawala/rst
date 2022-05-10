import pyperclip

from rst.lang_handler import provide_rs


def test_main():
    assert 2 * 2 == 4


def test_pyperclip_func():
    provide_rs("something {} {}", "192.168.1.1", "1234")
    assert pyperclip.paste() == "something 192.168.1.1 1234"
