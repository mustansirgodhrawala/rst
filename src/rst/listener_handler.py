import subprocess

import rst

"""
{'netcat': ['nc', 'netcat'], 'socat': ['socat', 'scat'], 'pwncat': ['pwn', 'pwncat', 'pwncat-cs']}
"""


def activate_netcat(port):
    subprocess.Popen(["terminator", "-e", f"nc -lvnp {port}"])


def activate_socat(port):
    subprocess.Popen(["terminator", "-e", f"socat -d -d TCP4-LISTEN:{port} STDOUT"])


def activate_pwncat(port):
    subprocess.Popen(
        [
            "terminator",
            "-e",
            f"source /opt/pwncat/pwncat-env/bin/activate;pwncat-cs -lp {port}",
        ]
    )


def activate_listener(listeners, listener, port, ngrok_use):
    for key, value in listeners.items():
        for items in value:
            if listener == items:
                if key == "netcat":
                    # Activate netcat
                    print(f"Activating netcat listener on {port}")
                    activate_netcat(port)
                    break

                elif key == "socat":
                    # Activate netcat
                    print("Activating socat listener")
                    activate_socat(port)
                    break

                elif key == "pwncat":
                    # Activate netcat
                    print("Activating pwncat-cs listener")
                    activate_pwncat(port)
                    break

    # Returning back to the main script.
    rst.rst.take_choices(listeners, ngrok_use)  # type: ignore[attr-defined]
