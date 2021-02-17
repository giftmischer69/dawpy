@echo ON
call conda env remove -n dawpy
call conda create -y -n dawpy
call conda activate dawpy
call conda install -y -c conda-forge python=3.8 pip rust=1.47.0 openjdk=11.0.6
call curl.exe --output lib\jfugue-5.0.9.jar http://www.jfugue.org/jfugue-5.0.9.jar
call pip install pickledb pydantic pycco pybuilder
call cargo install --version 0.10.2 pyoxidizer