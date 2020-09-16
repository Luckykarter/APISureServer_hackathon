# serializers for output


# EXAMPLE:

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

# # add information of X-wing as well into defence tower serializer
# class XwingSerializer(serializers.ModelSerializer):
#     pilot = serializers.StringRelatedField(many=False)
#
#     class Meta:
#         model = XWing
#         fields = ['id', 'name', 'pilot']
#
#
# # representation for defence towers
# class DefenceTowerSerializer(serializers.ModelSerializer):
#     target = XwingSerializer()
#
#     class Meta:
#         model = DefenceTower
#         fields = '__all__'
