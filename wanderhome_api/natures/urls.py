from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"natures", views.NatureViewSet)
router.register(r"aesthetics", views.AestheticViewSet)
router.register(r"moves", views.MoveViewSet)
router.register(r"lore", views.LoreViewSet)

urlpatterns = [path("", include(router.urls))]
