# VIRTUALENV

## Instalar a extensão do pylinkt

## Instalação
pip install virtualenv (windows)
pip3 install virtualenv (linux)

## Iniciar um env
python3 -m venv venv

## Ativar um ambiente virtual
source venv/lib/activate (linux)
.\venv\Scripts\Activate.ps1 (windows)


# pylint

## Instalação
pip install pylint


## Pegar as dependencias de um Ambiente
venv/scripts/pip3 freeze > requirements.txt

## Instalar um pacote via requirements
pip install -r requirements.txt

## Configuração vsCode
.vscode/settings.json
{
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true
  },
  "python.linting.enabled": true,
  "python.linging.pylintEnable":true,
  "editor.tabSize": 4,
  "editor.insertSpaces": true
}

# Configuração manual do pylint
pylint --generate-rcfile > .pylintrc

# Instalação do SQLAlchemy
pip install SQLAlchemy