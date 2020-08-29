from django import template
from django.utils import timezone

from services.main_logic import get_users_purchases
from main.models import Purchase

register = template.Library()


@register.simple_tag
def get_week_purchase():
    return Purchase.objects.filter(date__range=[timezone.now() - timezone.timedelta(7), timezone.now()])