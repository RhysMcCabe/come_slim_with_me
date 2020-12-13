from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Wishlist, WishlistItem
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.decorators import login_required

def _wishlist_id(request):
    wishlist = request.session.session_key
    if not wishlist:
        wishlist = request.session.create()
    return wishlist


@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        wishlist = Wishlist.objects.get(wishlist_id=_wishlist_id(request))
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(
            wishlist_id= _wishlist_id(request)
        )
        wishlist.save()
    try:
        wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
        wishlist_item.save()
    except WishlistItem.DoesNotExist:
        wishlist_item = WishlistItem.objects.create(
                    product = product,
                    wishlist = wishlist
            )
        wishlist_item.save()
    return redirect('wishlist:wishlist_detail')

@login_required
def wishlist_detail(request, wishlist_items=None):
   try:
      wishlist = Wishlist.objects.get(wishlist_id=_wishlist_id(request))
      wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
   except ObjectDoesNotExist:
      pass
   return render(request, 'wishlist.html', {'wishlist_items': wishlist_items} )


@login_required
def delete_from_list(request, product_id):
    wishlist = Wishlist.objects.get(wishlist_id=_wishlist_id(request))
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    wishlist_item.delete()
    return redirect('wishlist:wishlist_detail')

