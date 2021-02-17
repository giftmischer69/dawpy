from pybuilder.core import use_plugin

#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
import shutil
import sys
import subprocess
import os
import logging

#todo!
#use_plugin("python.core")
#use_plugin("python.unittest")
#use_plugin("python.flake8")
#use_plugin("python.coverage")
#use_plugin("python.distutils")

# todo pybuilder should build bdist and sdist, wheel
# todo tests
# todo pybuilder black formatter plugin

name = "dawpy"
default_task = [
    "clean",
    "publish",
    "generate_docs",
    "oxidize"
]


@init
def set_properties(project):
    logging.basicConfig(level=logging.INFO)
    project.set_property("coverage_break_build", False)


@task
def clean(logger):
    dirs_to_clean = ["build", ".pybuilder", "target", "docs", "dawpy.egg-info"]
    for dir_str in dirs_to_clean:
        dir_name = f"./{dir_str}/"
        logger.info(f"removing build directory {dir_name}")
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)


def run_checked(command):
    proc = subprocess.run(
        command,
        stdout=sys.stdout,
        shell=True,
    )
    return_code = proc.returncode
    logging.info(f"return_code: {return_code}")
    if return_code != 0:
        raise Exception
    pass


@task
def oxidize(logger):
    logger.info("running oxidize")
    run_checked("pyoxidizer build")
    run_checked("build\\x86_64-pc-windows-msvc\\debug\\install\\dawpy.exe --help")


@task
def generate_docs(logger):
    logger.info("generating documentation")
    subprocess.check_output("pycco -i -s -l python dawpy ")
