import multiprocessing
from cmd import Cmd

import swagger_client
import uvicorn
from jinja2 import Template
from selenium import webdriver

from models import Daw
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.logger import logger


class View:
    # Handles either
    # - rendering & serving html file + selenium browser reload
    # - server lifecycle with multiprocess.Process
    # - Printing a ascii jinja template to the cmd line
    # - renders a daw object
    # - fastapi htmlresponse
    @classmethod
    def render_html(cls):
        with open("view/template.html", "r") as f:
            template = Template(f.read())
        with open("view/layout.css", "r") as f:
            layout = f.read()
        global global_daw
        daw_config = str(global_daw)
        ret = template.render(
            layout=layout,
            daw_config=daw_config
        )
        return ret


class Prompt(Cmd):
    # handles cmd line interaction with the user and calls other api
    # has a view object
    # has a daw object
    app = FastAPI()

    def __init__(self):
        super().__init__()
        self.api_instance = swagger_client.DefaultApi()
        # self.daw = global_daw
        self.view_server = multiprocessing.Process(target=serve)
        self.view_server.start()
        self.view_url = "http://127.0.0.1:8000/"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(self.view_url)

    @staticmethod
    @app.get("/", response_class=HTMLResponse)
    def get_root():
        return View.render_html()

    def do_greet(self, line):
        print("hello")

    def do_q(self, line):
        return True

    def postcmd(self, stop, line):
        """Hook method executed just after a command dispatch is finished."""
        global global_daw
        global_daw = self.api_instance.get_playlist_daw_get()
        self.browser.refresh()
        return stop

    def postloop(self) -> None:
        print("postloop")
        self.view_server.join()


def serve():
    uvicorn.run(Prompt.app,
                # host=host,
                # port=port,
                log_level="critical",
                use_colors=False)


global_daw = swagger_client.DefaultApi().get_playlist_daw_get()


def main():
    p = Prompt()
    p.cmdloop()
    print("shut down correctly")


if __name__ == '__main__':
    # can be started in true cmd mode or with html view
    main()
