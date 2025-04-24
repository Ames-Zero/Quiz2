from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee_app import views

# Swagger/OpenAPI imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Set up DRF router and register viewsets
router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'attendances', views.AttendanceViewSet)
router.register(r'performances', views.PerformanceViewSet)
router.register(r'projects', views.ProjectViewSet)

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Data API",
        default_version='v1',
        description="API documentation for Employee Data Generation & Visualization",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]