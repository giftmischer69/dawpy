# daw

run in docker container for urwid support maybe ? :)

there needs to be information that is more top level than playlist, which is general config (vs playlist level - project config). need to save plugin(&preset) root folder, pattern(midi) root folder, etc... 

- empty project with sane defaults, default name=untiteled oder so
- mrswatson 64 für vst und vsti hosting
- nanohost 64 für vst config und fxp management
- wusic 64 vst für fxb -> fxp (öffnen mit nanohost)
- pydub

## packages:

- core: python api / class

- cli: wraps core headless for a cli (batch processing)

  - https://github.com/tiangolo/typer

  - https://github.com/tiangolo/typer-cli

- tui: (interactive) CRUD cli loop with commands, wraps core
  - https://github.com/yaronn/blessed-contrib

- gui: (interactive) jupyter like:

- https://rubikscode.net/2020/11/23/deploying-machine-learning-models-with-fastapi-and-angular/

  - frontend: angular 

  - https://angularjs.org/

  - https://angular.io/cli

  - backend/server: fastapi

  - https://fastapi.tiangolo.com/tutorial/first-steps/

https://pypi.org/project/fastapi-code-generator/

## config
- yaml serialiation und lieber hydra (als configparser)
  - https://hydra.cc/docs/intro/
  - https://pyyaml.org/wiki/PyYAMLDocumentation
  - https://docs.python.org/3/library/configparser.html
    
## deployment
- github (pages) download for local usage zip or installer
- online, hosted, to try it out: heroku free
- conda / pypi / chocolatey / flatpak / pop shop

## targeted platforms:
- windows
- ubuntu

## future features & goals:
- use spacy for ai support https://github.com/explosion

## installation links
- wusic vm http://www.dontcrack.com/freeware/downloads.php/id/4986/software/Wusik-VM/
- mrswatson https://github.com/teragonaudio/MrsWatson/releases/download/0.9.8/MrsWatson-0.9.8.zip
