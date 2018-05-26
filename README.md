# Django Singleton Model
Singleton design-pattern implementation for using with django models and works with more recent versions of django

## Using
Install the package
```bash
$ pip3 install django-singleton-model
```

now you can import the SingletonModel class and inherit from it
```python
from singleton_models import SingletonModel

class MySingleModel(SingletonModel):
	pass
```

and that's it. Don't add it to INSTALLED_APPS.

## Running tests
Go into example folder
```bash
$ cd example
```
and run them
```bash
$ ./manage.py test
```

## Troubleshooting
Check the example folder if you have any doubts. Or you can created an issue it doesn't work anyway.
