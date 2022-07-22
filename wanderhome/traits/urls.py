from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"traits", views.TraitViewSet)
router.register(r"moves", views.MoveViewSet)

urlpatterns = [
    path("", include(router.urls))
]