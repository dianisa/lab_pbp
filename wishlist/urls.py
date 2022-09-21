from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_xml
from wishlist.views import show_wishlist_json
from wishlist.views import show_wishlist_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', show_wishlist_id, name='show_wishlist_id'),
    path('xml/<int:id>', show_wishlist_id, name='show_wishlist_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]