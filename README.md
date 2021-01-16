# dawpy
## user functions (TODO: Implement in daw/dawserver):
- [X] create new project, name, bpm
- [X] register plugin, plugin parameters
- [X] get registered plugins
- [X] create new pattern, name, optional: other params 
- [X] pattern set 
- [ ] determine pattern length with midi length
- [X] add pattern to playlist
- [X] configure plugin
- [X] configure pattern
- [ ] save playlist
- [ ] save pattern
- [ ] save plugin
- [X] load playlist
- [X] load pattern
- [X] load plugin
- [ ] render pattern
- [X] render playlist
- [ ] implement auto save
## normal procedure
- opens programm
  - daw_config = the user config / if none -> default.yaml / # if none -> get_default() with hardcoded values to create default.yaml
  - playlist = default / empty project / default.yaml
- check registered plugins
- register plugin
- create new playlist
- create new pattern
- add pattern to playlist
- render playlist

## components
### DawServer:
a fastapi server exposing a rest-api which acts as the controller. it takes get, put, etc. and runs commands with the local daw object. 
### Daw:
a python class / api which acts as the model and can be normally imported with python, gets manipulated in dawpy by dawserver
### PromptClient:
python/bash-like interactive shell. commands get parsed and sent to the dawserver, results can be displayed. 
TODO: add to view: piano roll
### WebClient:
[angular|react|vue] frontend server communicating with the DawServer, serving a beautiful (locally hosted) interactive Website (like jupyter) 

## for setup.py
- https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install
- https://github.com/apache/airflow/blob/master/setup.py
- dawpy - daw python package 
- dawpy[prompt] - server + daw + promptclient
- dawpy[gui] - server + daw + webclient
- dawpy[jupyter] - daw + jupyter // maybe create example.ipynb

## ideas / planned
- [ ] for frontend gui: https://rubikscode.net/2020/11/23/deploying-machine-learning-models-with-fastapi-and-angular/
- [ ] do this:
`dawpy etc... [-v/--version]
  Features: WebClient, PromptClient, DawServer, Daw`
like this: 
`magick identify -version
  Features: DPC Cipher Modules OpenCL OpenMP(4.5)`
- [ ] install with dawpy[prompt] dawpy[gui] etc.

## scrap
multi core processing:
  - https://github.com/classner/pymp - Easy, OpenMP style multiprocessing for Python
  - normal threading: x = threading.Thread(target=thread_function, args=(1,)) x.start() x.join() 
