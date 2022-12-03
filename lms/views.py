
from rest_framework import viewsets

from lms.models import Curator, Direction, Group, Discipline, Student
from lms.serializer import (
    CuratorSerializer,
    DirectionSerializer,
    GroupSerializer,
    DisciplineSerializer,
    StudentSerializer,
)


class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = CuratorSerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = DirectionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = GroupSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = DisciplineSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects
    queryset = queryset.all()
    queryset = queryset.order_by('id')
    serializer_class = StudentSerializer
