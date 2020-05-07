from django import template

register = template.Library()


def newcut(value, arg):
    """This cuts out all values of 'arg' from the string!"""

    return value.replace(arg, '')


register.filter('newcuttocall', newcut)