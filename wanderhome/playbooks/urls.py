from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"playbooks", views.PlaybookViewSet)
router.register(r"animals", views.AnimalViewSet)
router.register(r"personalities", views.PersonalityViewSet)
router.register(r"appearances", views.AppearanceViewSet)
router.register(r"histories", views.HistoryViewSet)
router.register(r"relationships", views.RelationshipViewSet)
router.register(r"signature-moves", views.SignatureMoveViewSet)
router.register(r"seasonal-moves", views.SeasonalMoveViewSet)

urlpatterns = [
    path("", include(router.urls))
]
