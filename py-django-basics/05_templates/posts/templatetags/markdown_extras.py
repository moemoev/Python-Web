from markdown import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text: str):
    return mark_safe(markdown(text))

@register.filter(name='arg_workaround')
def filter_using_several_parameters_and_using_a_very_long_cun_name_to_override_by_register_filter(text: str, args:str):
    parameters = args.upper().split(', ')
    word = ''.join(str(el) for el in parameters)

    return text.lower() + " " + word