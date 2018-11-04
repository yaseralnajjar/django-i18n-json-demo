# What is this?

A simple demo to show the usage of python-i18n using json file. No need to recompile *.po *.mo ugly files, just translate and launch!

# How does it work?

`local` folder has the localized strings; it has both EN and AR values for the string `hi`.

And we load those strings in `polls/views.py`, you can see this view in your local server at `http://127.0.0.1:8000/polls/`

```
from django.http import HttpResponse

import i18n
i18n.set('locale', 'ar')
i18n.load_path.append('local')

def index(request):
    return HttpResponse(i18n.t('foo.hi'))
```

# Used packages

`python-i18n` is the main package here.

You can see more info here about the package: https://github.com/danhper/python-i18n

# Running the project (Windows specific)

```
virtualenv venv
call venv\Scripts\activate
python manage.py runserver
```