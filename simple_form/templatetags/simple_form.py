from django import template
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_form(form):
    string_fields = force_text(form.non_field_errors())
    for field in form.hidden_fields():
        string_fields += force_text(field)

    for field in form.visible_fields():
        string_fields += render_field(field)

    return mark_safe(string_fields)


@register.filter
def render_field(field):
    slug = field.field.widget.__class__.__name__.lower()
    templates = [
        'simple_form/{0}.html'.format(slug),
        'simple_form/field.html'
    ]
    return template.loader.render_to_string(templates, {'field': field, 'slug': slug})
