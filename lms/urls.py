from rest_framework.routers import DefaultRouter

from lms.views import CuratorViewSet, DirectionViewSet, GroupViewSet, DisciplineViewSet, StudentViewSet

lms_router = DefaultRouter()

lms_router.register(r'curator', CuratorViewSet, basename='curator')

lms_router.register(r'direction', DirectionViewSet, basename='direction')

lms_router.register(r'Group', GroupViewSet, basename='Group')

lms_router.register(r'Discipline', DisciplineViewSet, basename='Discipline')

lms_router.register(r'Student', StudentViewSet, basename='Student')
