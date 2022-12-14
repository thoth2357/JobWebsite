from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key) -> list:
    """
    args: Takes the value and the key to split the value by the key
    return: Returns the value turned into a list.
    """
    return value.split(key)

@register.simple_tag
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()