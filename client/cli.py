import multiprocessing
from cmd import Cmd

import uvicorn
from jinja2 import Template
from selenium import webdriver

from models import Daw
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


class View:
    # Handles either
    # - rendering & serving html file + selenium browser reload
    # - server lifecycle with multiprocess.Process
    # - Printing a ascii jinja template to the cmd line
    # - renders a daw object
    # - fastapi htmlresponse

    with open("view/template.html", "r") as f:
        template = Template(f.read())

    @classmethod
    def render_html(cls, daw: Daw):
        daw_config = daw.daw_config.__dict__
        return cls.template.render(daw_config=daw_config)


class Prompt(Cmd):
    # handles cmd line interaction with the user and calls other api
    # has a view object
    # has a daw object
    app = FastAPI()
    view_url = "http://127.0.0.1:8000/"
    browser = webdriver.Chrome()
    daw = browser.get(view_url)

    def __init__(self):
        pass

    @staticmethod
    @app.get("/", response_class=HTMLResponse)
    def get_root():
        return View.render_html(Prompt.daw)

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        return True


def serve():
    uvicorn.run(Prompt.app,
                # host=host,
                # port=port,
                # log_level="critical",
                use_colors=False)


def main():
    view_server = multiprocessing.Process(target=serve)
    p = Prompt()
    p.cmdloop()
    view_server.join()
    view_server.terminate()
    print("shut down correctly")


if __name__ == '__main__':
    # can be started in true cmd mode or with html view
    main()
