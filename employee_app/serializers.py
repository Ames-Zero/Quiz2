from rest_framework import serializers
from .models import Department, Employee, Attendance, Performance, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )
    projects = ProjectSerializer(many=True, read_only=True)
    project_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Project.objects.all(), source='projects', write_only=True
    )

    class Meta:
        model = Employee
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone', 'hire_date',
            'department', 'department_id', 'job_title', 'salary', 'is_active', 'created_at',
            'projects', 'project_ids'
        ]

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Attendance
        fields = [
            'id', 'employee', 'employee_id', 'date', 'check_in', 'check_out',
            'status', 'remarks'
        ]

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Performance
        fields = [
            'id', 'employee', 'employee_id', 'review_date', 'score',
            'reviewer', 'comments', 'goal_achieved'
        ]
