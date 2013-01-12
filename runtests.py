#!/usr/bin/env python
import sys
from django.conf import settings
from django.core.management import call_command

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'stickymessages',
            'stickymessages.tests',
        ),
        ROOT_URLCONF=None,
        USE_TZ=True,
        SECRET_KEY='mysecretkey'
    )


from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['stickymessages', ])
if failures:
    sys.exit(failures)