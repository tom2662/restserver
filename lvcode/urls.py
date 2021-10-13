# myapi/urls.py
from django.urls import include, path
from django.conf.urls import url 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^api/calclv$', views.lvcalc ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
