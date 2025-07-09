from rest_framework import serializers
from chamados.models import Chamados

class ChamadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chamados
        fields = '__all__'

