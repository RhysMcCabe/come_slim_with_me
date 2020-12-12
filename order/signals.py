from django.dispatch import receiver
from django.db.models import signals
from .models import Order
from django.core.mail import send_mail
from django.conf import settings

@receiver(signals.post_save, sender=Order)
def order_email(sender, instance, **kwargs):
    subject = 'TUD - Tallght Merch Order'
    message = 'Dear {}, \n\nYou have successfully placed an order with TUD - Tallaght Merch.\n\nYour order is now being processed and will be dispached within the next 3 working days.\n\n Thanks,\nThe TUD Tallaght Merch Team'.format(instance.billingName)
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [instance.emailAddress], fail_silently=False,)