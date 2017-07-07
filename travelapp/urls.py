from django.conf.urls import url
from django.contrib import admin
from travelapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^states/$',views.state,name='state'),
    url(r'^city/$',views.city,name='city'),
    url(r'^homepage/$',views.homepage, name='homepage'),
    url(r'^homepage1/$',views.homepage1, name='homepage1'),
    url(r'^home/$',views.home, name='home'),
    url(r'^placemap/$',views.placemap,name = 'placemap'),
    url(r'^disp_image/$',views.disp_image,name='disp_image'),
    url(r'^search/',views.search, name='search'),
    url(r'^viewareas/(?P<c_name>[^/]+)/$', views.viewareas, name = 'viewareas'),
    #url(r'^viewareas/$', views.viewareas, name = 'viewareas'),
    url(r'^description/(?P<d_name>[^/]+)/$', views.description, name = 'description'),
    url(r'^placestoeat/$',views.placestoeat,name = 'place'),
    url(r'^attractions/$',views.attractions,name = 'place2'),
    url(r'^shopping/$',views.shopping,name = 'place3'),
    url(r'signup/$',views.signup, name = 'signup'),
    #url(r'^travelapp/',views.index,name='home'),
    #url(r'^auth/'include('django.contrib.auth.urls')),
    url(r'bookNow/$',views.bookings, name = 'booking'),
    url(r'registration/$',views.registration, name = 'registration'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^success/$', views.success, name='logout'),
    url(r'^homepage1/bookingslist/$',views.bookingslist, name='bookingslist'),
    url(r'^cancelbook/$',views.cancelbook, name='cancelbook'),
    url(r'^booknow/$',views.booknow, name='booknow'),
    url(r'^success/$',views.success, name='success'),
]


