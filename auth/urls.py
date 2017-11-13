#from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

#from . import views as local_views
from rest_framework.authtoken import views as rest_framework_views


from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^upload/$', views.upload_img, name='upload'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^register', views.signup, name='register'),
]

