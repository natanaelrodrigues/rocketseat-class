# VIRTUALENV

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