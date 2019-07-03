==================
django-simple-form
==================

Django-simple-form is a simple way to build your forms in HTML-level.


Installation
~~~~~~~~~~~~

You can get Django simple form by using pip::

    $ pip install django-simple-form


To enable the package you need to add it to `INSTALLED_APPS`::

    INSTALLED_APPS = [
        ...
        'simple_form',
        ...
    ]


Usage
~~~~~

Render all fields form::

    {% load simple_form %}

    ...

    {{ form|render_form }}


Render field by field::

    {% load simple_form %}

    ...

    {{ form.name|render_field }}
    {{ form.email|render_field }}



Custom the template
~~~~~~~~~~~~~~~~~~~


Create a folder with name `simple_form` in your template dir::

    templates/
        ...
        simple_form/
            field.html
            ...

In HTML file you define the structure for each field the form::


    <div>
      <label for="{{ field.auto_id }}">
        {{ field.label }}
      </label>

      {{ field }}

      {% if field.errors %}
        {% for error in field.errors %}
          <span>{{ error }}</span>
        {% endfor %}
      {% endif %}
    </div>

    {% if field.help_text %}
      <p title="{{ field.help_text }}">
        {{ field.help_text }}
      </p>
    {% endif %}


If you need to customize the rendering for the type field, create an HTML file to the specific type of his widget::

    templates/
        ...
        simple_form/
            field.html
            checkboxinput.html
            ...
