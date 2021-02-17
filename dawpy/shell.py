from cmd import Cmd
import json
from dawpy._version import __version__
from dawpy.daw import Daw

# https://github.com/yaronn/wopr
# https://github.com/willmcgugan/rich


class View:
    @classmethod
    def print_daw(cls, daw):
        parsed = json.loads(daw.json())
        print(json.dumps(parsed, indent=4, sort_keys=True))


class Shell(Cmd):
    """ the dawpy shell, based on the built in python cmd module """

    def __init__(self):
        super().__init__()
        self.prompt = "dsh>"
        self.daw = Daw()
        self.view = View()
        self.debug = True

    def preloop(self):
        print(f"welcome to the dawpy shell, version: {__version__}")
        self.do_help("")

    def do_q(self, line):
        """ Quits the shell """
        return True

    def do_pr_daw(self, line):
        """ Prints the daw """
        self.view.print_daw(self.daw)
