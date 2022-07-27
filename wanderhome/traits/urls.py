from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"trait-categories", views.TraitCategoryViewSet)
router.register(r"traits", views.TraitViewSet)
router.register(r"trait-moves", views.TraitMoveViewSet)

urlpatterns = [
    path("", include(router.urls))
]
