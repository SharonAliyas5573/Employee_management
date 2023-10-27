from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PromoteEmployeeView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.years_of_experience >= 5:
            department = instance.department
            existing_manager = department.manager
            if existing_manager is None:
                instance.is_manager = True
                instance.save()
                department.manager = instance
                department.save()

                return Response(
                    {"message": "Employee promoted to manager successfully."},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "This department already has a manager."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "Employee does not meet the criteria for promotion."},
                status=status.HTTP_400_BAD_REQUEST
            )
