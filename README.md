django-allejo
=============

<p align="center">
  <img src="/allejo.png" alt="django-allejo" rel="django-allejo">
</p>


### Running Demo app:
```
cd demo
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate --all
python manage.py runserver
``` 

### Roadmap:

* Ao criar um campeonato, deve gerar todos os jogos pelo ```mptt```.
* Criar listagem de campeonatos na ```demo/index.html```.
* Criar interna de campeonato. 
* A interna de campeonato deve exibir a chave de playoffs. [hoje a chave de playoffs está estática]
