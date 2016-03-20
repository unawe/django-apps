from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""

    if hasattr(value, 'keys') and arg in value:
        return value[arg]
    elif hasattr(value, str(arg)):
        result = getattr(value, arg)
        if callable(result):
            result = result()
        return result
    elif arg.isdigit() and len(value) > int(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID
