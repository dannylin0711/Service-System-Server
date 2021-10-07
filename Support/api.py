
from rest_framework import routers
from Machine.api import MachineViewSet, ErrorcodeViewSet, AdditionalFileViewSet


v1 = routers.DefaultRouter()
v1.register(r'machine', MachineViewSet)
v1.register(r'error_code', ErrorcodeViewSet)
v1.register(r'additional_file', AdditionalFileViewSet)

