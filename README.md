django-allejo
=============

<p align="center">
  <img src="/allejo.png" alt="django-allejo" rel="django-allejo">
</p>

Allejo is an django app who provides management and creation for custom tournaments and rankings for some sports like soccer.
You can use django-allejo for football management simulation games like elifoot or Football Manager also for backend APIs like goalserve and Tabela Fácil.

Allejo works fine on ***Django 1.4+*** and ***Django 1.7***


### Installation

```python
  pip install django-allejo
```

Put allejo app into `INSTALLED_APPS`:

```python
  INSTALLED_APPS = [
      ...
      'allejo',
      ]
```

```
  python manage.py migrate allejo
```

### Django < 1.7

For Django 1.4+ and South users use this `SETTINGS` below:

```python
  SOUTH_MIGRATION_MODULES = {
      'allejo': 'allejo.south_migrations',
  }
```

### Usage

You can input data through django-admin or make a wrapper to read some external API.

```python
  # get all matches from a championship
  championship.match_set.all()

  # standings from a championship
  championship.standings_set.all()
```

### Credits

*Special thanks to [Intip](https://www.github.com/intip)! Thanks for giving space for our 'social codings' hackathons.*

### Copyright

Copyright (c) 2013 Igor P. Leroy. See [LICENSE](/LICENSE) for details.
