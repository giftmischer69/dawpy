# dawpy

A python based digital audio workstation

unfortunately, only windows is currently supported.
once the first good prototype is working (start of phase 3 - alpha) i will direct my attention towards supporting 
debian-based linux, too.

TODO: Screenshot
TODO: Github Pages Host Docs
TODO: CI-Builds!
Someday: deploy web-service on heroku (free :smiley:)

## installation

TODO: pyoxidizer output zipped as release

- `git clone https://github.com/giftmischer69/dawpy`
- `cd dawpy`
- (optional) `conda create -n dawpy`
- `pip install .`

## running

- `dawpy --help`  

## building 

clone this repository
- `git clone https://github.com/giftmischer69/dawpy`
- `cd dawpy`
- `install_build_dependencies.bat`
- `pyb`

### explanation

this project uses 
- pybuilder to manage the project 

- pyoxidizer to build an exe-file for easy distribution
to non-developer users

#### build dependencies

install build dependencies
- [conda](https://docs.conda.io/en/latest/miniconda.html)
- [VS Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)

- *the following dependencies are written in [PURL](https://github.com/package-url/purl-spec) format*
  - pkg:conda/python@3.8
  - pkg:conda/pip 
  - pkg:conda/rust@1.47.0
  - pkg:pypi/pickledb
  - pkg:pypi/pydantic
  - pkg:pypi/pycco
  - pkg:pypi/pybuilder
  - pkg:cargo/pyoxidizer@0.10.2

- cmd:curl.exe --output lib\jfugue-5.0.9.jar http://www.jfugue.org/jfugue-5.0.9.jar

these dependencies can be installed with [install_build_dependencies.bat](./install_build_dependencies.bat):

```shell
@echo ON
call conda env remove -n dawpy
call conda create -y -n dawpy
call conda activate dawpy
call conda install -y -c conda-forge python=3.8 pip rust=1.47.0 openjdk=11.0.6
call curl.exe --output lib\jfugue-5.0.9.jar http://www.jfugue.org/jfugue-5.0.9.jar
call pip install pickledb pydantic pycco pybuilder
call cargo install --version 0.10.2 pyoxidizer
```