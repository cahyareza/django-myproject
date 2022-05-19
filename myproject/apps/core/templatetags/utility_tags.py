from urllib.parse import urlencode
from datetime import datetime
from django import template
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

register = template.Library()


def construct_query_string(context, query_params):
    # empty values will be removed
    query_string = context["request"].path
    if len(query_params):
        encoded_params = urlencode([
            (key, force_str(value))
            for (key, value) in query_params if value
        ]).replace("&", "&amp;")
        query_string += f"?{encoded_params}"
    return mark_safe(query_string)


"""TAGS"""


@register.simple_tag(takes_context=True)
def modify_query(context, *params_to_remove, **params_to_change):
    """Renders a link with modified current query parameters"""
    query_params = []
    for key, value_list in context["request"].GET.lists():
        if not key in params_to_remove:
            # don't add key-value pairs for params_to_remove
            if key in params_to_change:
                # update values for keys in params_to_change
                query_params.append((key, params_to_change[key]))
                params_to_change.pop(key)
            else:
                # leave existing parameters as they were
                # if not mentioned in the params_to_change
                for value in value_list:
                    query_params.append((key, value))
                    # attach new params
    for key, value in params_to_change.items():
        query_params.append((key, value))
    return construct_query_string(context, query_params)\

"""FILTERS"""

DAYS_PER_YEAR = 365
DAYS_PER_MONTH = 30
DAYS_PER_WEEK = 7

@register.filter(is_safe=True)
def date_since(specific_date):
    """
    Returns a human-friendly difference between today and past_date
    (adapted from https://www.djangosnippets.org/snippets/116/)
    """
    today = timezone.now().date()
    if isinstance(specific_date, datetime):
        specific_date = specific_date.date()
    diff = today - specific_date
    diff_years = int(diff.days / DAYS_PER_YEAR)
    diff_months = int(diff.days / DAYS_PER_MONTH)
    diff_weeks = int(diff.days / DAYS_PER_WEEK)
    diff_map = [
        ("year", "years", diff_years,),
        ("month", "months", diff_months,),
        ("week", "weeks", diff_weeks,),
        ("day", "days", diff.days,),
    ]
    for parts in diff_map:
        (interval, intervals, count,) = parts
        if count > 1:
            return _(f"{count} {intervals} ago")
        elif count == 1:
            return _("yesterday") \
                if interval == "day" \
                else _(f"last {interval}")
    if diff.days == 0:
        return _("today")
    else:
        # Date is in the future; return formatted date.
        return f"{specific_date:%B %d, %Y}"
