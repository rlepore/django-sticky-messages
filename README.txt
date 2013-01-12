=====
Sticky Messages
=====

Sticky Messages is a simple Django app to display "sticky" messages stored in
a message model that expire after a given time period. 

Inspiration from:
http://stackoverflow.com/questions/3076365/how-to-make-django-messages-stackoverflow-style

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "stickymessages" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'stickymessages',
      )

2. Add "stickymessages" to your TEMPLATE_CONTEXT_PROCESSORS setting like this::

      TEMPLATE_CONTEXT_PROCESSORS = (
          ...
          'stickymessages.context_processors.latest_sticky_message',
      )

3. Run `python manage.py syncdb` to create the stickymessages models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
  to create a message (you'll need the Admin app enabled).
  
5. To display a message simply add
{% include "stickymessages/display_latest_message.html" %} to one of your
templates.
    NOTE: Template file uses bootstrap 'alert alert-block' classes for styling.
    You may create your own styling by using the sticky-message style.