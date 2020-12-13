from django.dispatch import receiver
from django.db.models import signals
from .models import Order
from django.core.mail import send_mail
from django.conf import settings

@receiver(signals.post_save, sender=Order)
def order_email(sender, instance, **kwargs):
    if instance.status == 'Recieved':
        subject = 'TUD - Tallaght Merch Order'
        message = 'Dear {}, \n\nYou have successfully placed an order with TUD - Tallaght Merch.\n\nYour order has being recieved and will be processed soon.\n\nThanks,\nThe TUD Tallaght Merch Team'.format(instance.billingName)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.emailAddress], fail_silently=False,)

@receiver(signals.post_save, sender=Order)
def shipped_email(sender, instance, **kwargs):
    if instance.status == 'Shipped':
        subject = 'TUD - Tallaght Merch Order'
        message = 'Dear {}, \n\nYour order has now shipped, \nSit tight! Your order will be delivered within the next 2 working days.\n\nThanks,\nThe TUD Tallaght Merch Team'.format(instance.billingName)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.emailAddress], fail_silently=False,)

@receiver(signals.post_save, sender=Order)
def inprogress_email(sender, instance, **kwargs):
    if instance.status == 'In Progress':
        subject = 'TUD - Tallaght Merch Order'
        message = 'Dear {}, \n\nYour order is now in progress, \n Your order will be ready for dispatch within the next 2 working days.\n\nThanks,\nThe TUD Tallaght Merch Team'.format(instance.billingName)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.emailAddress], fail_silently=False,)

@receiver(signals.post_save, sender=Order)
def delayed_email(sender, instance, **kwargs):
    if instance.status == 'Delayed':
        subject = 'TUD - Tallaght Merch Order'
        message = 'Dear {}, \n\nUnfortunetly your order has being delayed, \n We endevour to get your order back on track as soona as possible.\nWe hope your order will be ready for dispatch within the next 4 working days.\n\nFot the inconvience this may cause, we are giving you a coupon code for 10% off your next order. Just use the code DELAY10 at the checkout.\n\nThanks,\nThe TUD Tallaght Merch Team'.format(instance.billingName)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.emailAddress], fail_silently=False,)