from django import template

register = template.Library()


@register.filter
def set_index(i_row, i_col):
    return i_col * 25 + i_row


@register.filter
def highlight(score, i):
    if score == i:
        return "highlight"
    else:
        return ""


