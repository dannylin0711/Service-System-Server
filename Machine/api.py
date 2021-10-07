from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets, serializers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Errorcode, Machine, AdditionalFile
import mimetypes


class AdditionalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFile
        fields = '__all__'


class ErrorcodeSerializer(serializers.ModelSerializer):
    additional_file = AdditionalFileSerializer(many=True)

    class Meta:
        model = Errorcode
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):
    error_codes = ErrorcodeSerializer(many=True)

    class Meta:
        model = Machine
        fields = '__all__'


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Machine.objects.all()
        machine_name = self.request.query_params.get('machine')
        if machine_name is not None:
            queryset = queryset.filter(machine_type=machine_name)
        return queryset


class ErrorcodeViewSet(viewsets.ModelViewSet):
    queryset = Errorcode.objects.all()
    serializer_class = ErrorcodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdditionalFileViewSet(viewsets.ModelViewSet):
    queryset = AdditionalFile.objects.all()
    serializer_class = AdditionalFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def get_file(request, filename):
    fl = open(filename, 'rb')
    response = HttpResponse(fl, content_type='image/png')
    response['Content-Disposition'] = "attachment; filename=%s" % fl
    return response



