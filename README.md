crud user
Primeiro, clone o repositório em sua máquina local: git clone https://github.com/AlbertoWagner/crud_user.git

Instale o requirements:

pip install -r requirements.txt

Crie o database:

python manage.py migrate

Rodar o projeto

python manage.py runserver

O projeto estará disponível em 127.0.0.1:8000.

Teste do projeto ./manage.py test user

OBS: Quando for resgatar a senha do user olha para terminal o e-mail aparecera la.
