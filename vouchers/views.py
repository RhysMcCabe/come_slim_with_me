from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoucherApplyForm
from .models import Voucher
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.utils import timezone


@require_POST
def voucher_apply(request):
    now = timezone.now()
    form = VoucherApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['voucher_id'] = voucher.id
        except Voucher.DoesNotExist:
            request.session['voucher_id'] = None
    return redirect('cart:cart_detail')