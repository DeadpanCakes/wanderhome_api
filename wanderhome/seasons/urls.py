from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"seasons", views.SeasonViewSet)
router.register(r"months", views.MonthViewSet)
router.register(r"lacks", views.LackViewSet)
router.register(r"signs", views.SignViewSet)
router.register(r"events", views.EventViewSet)
router.register(r"effects", views.EffectViewSet)
router.register(r"effect-moves", views.EffectMoveViewSet)
router.register(r"holidays", views.HolidayViewSet)
router.register(r"traditions", views.TraditionViewSet)
router.register(r"holiday-moves", views.HolidayMoveViewSet)
router.register(r"customs", views.CustomViewSet)

urlpatterns = [path("", include(router.urls))]
