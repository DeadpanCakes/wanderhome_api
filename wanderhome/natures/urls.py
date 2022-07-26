from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"nature-categories", views.NatureCategoryViewSet)
router.register(r"natures", views.NatureViewSet)
router.register(r"aesthetics", views.AestheticViewSet)
router.register(r"moves", views.MoveViewSet)
router.register(r"lore", views.LoreViewSet)

urlpatterns = [path("", include(router.urls))]
