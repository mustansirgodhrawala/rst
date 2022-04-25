# try:
# import gnureadline as readline

# except ImportError:
#     import readline
import logging
from rich import print

LOG_FILENAME = "/tmp/rst.log"
logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


class SimpleCompleter:
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text,
            # so build a match list.
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
                logging.debug("%s matches: %s", repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug("(empty input) matches: %s", self.matches)

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug("complete(%s, %s) => %s", repr(text), state, repr(response))
        return response


def input_loop():
    line = ""
    while line != "stop":
        print("[yellow]rst>>>[/yellow]", end="")
        line = input("")
        return line
