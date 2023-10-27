from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDestroyView,
    PromoteEmployeeView
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('employees/promote/<int:pk>/', PromoteEmployeeView.as_view(), name='promote-employee'),
    path('departments/', DepartmentListCreateView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
]
