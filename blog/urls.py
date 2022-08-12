from django.urls import path
from . import views

#added 20220607
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api_root/', include(router.urls)),
]

#urlpatterns += router.urls