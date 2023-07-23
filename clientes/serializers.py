from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validade_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O cpf deve ter 11 dígitos")
        return cpf