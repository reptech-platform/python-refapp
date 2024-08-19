from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create the schema view object for generating API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="My Trip API",  # Title of the API
        default_version='v1',  # Default API version
        description="Test description",  # Description of the API
        terms_of_service="https://www.google.com/policies/terms/",  # Terms of service URL
        contact=openapi.Contact(email="contact@myapi.local"),  # Contact email
        license=openapi.License(name="BSD License"),  # License information
    ),
    public=True,  # Publicly accessible
    permission_classes=(permissions.AllowAny,),  # Permissions required to access the schema
)
