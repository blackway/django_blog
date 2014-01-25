# -*- coding: utf-8 -*-
from django import template

register = template.Library()


# 사용법 {% load blog_filters %}
# {{ name |capitalize }}
@register.filter
def capitalize(value):
    return value.capitalize()

# @register.filter
# def board_no(*args):
#     return ''


@register.simple_tag
def board_no(page, page_total, counter):
    if page == '':
        page = 1
    else:
        page -= 1
    return (page_total + 1) - (counter + (page*10))
# def board_no(a, b, *args, **kwargs):
    # warning = kwargs['warning']
    # profile = kwargs['profile']