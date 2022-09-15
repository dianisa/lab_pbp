from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Dianisa Wulandari'
}
    return render(request, "wishlist.html", context)

def show_wishlist_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_wishlist_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_wishlist_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    
    if ("json" in request.path):
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")