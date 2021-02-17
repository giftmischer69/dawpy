#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
import shutil
import sys
import subprocess
import os
import logging

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")

# todo tests

name = "dawpy"
default_task = [
    "clean",
    "blacken",
    "run_unit_tests",
    "analyze",
    "setup_py_sdist_bdist_wheel",
    "generate_docs",
    "oxidize",
]


@init
def set_properties(project):
    logging.basicConfig(level=logging.INFO)
    project.set_property("coverage_break_build", False)
    project.depends_on_requirements("requirements.txt")
    project.set_property("dir_source_main_python", ".")
    project.set_property(
        "flake8_exclude_patterns",
        "build,.pybuilder,target,dist,.bzl,.toml,.md,jython,.jython_cache",
    )
    project.set_property("flake8_verbose_output", True)


@task
def clean(logger):
    dirs_to_clean = [
        "build",
        "target",
        "docs",
        "dawpy.egg-info",
        "dist",
        ".jython_cache",
    ]
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


@task
def blacken(logger):
    logger.info("running the black formatter on directory .")
    run_checked("black .")


@task
def setup_py_sdist_bdist_wheel(logger):
    logger.info("running: python setup.py sdist bdist_wheel")
    run_checked("python setup.py sdist bdist_wheel")


@task
def generate_docs(logger):
    logger.info("generating documentation")
    subprocess.check_output("pycco -i -s -l python dawpy ")


@task
def oxidize(logger):
    logger.info("running oxidize")
    run_checked("pyoxidizer build")
    run_checked("build\\x86_64-pc-windows-msvc\\debug\\install\\dawpy.exe --help")
