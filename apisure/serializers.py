# serializers for output


from rest_framework import serializers
from .models import Guarantee, Project


class GuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
