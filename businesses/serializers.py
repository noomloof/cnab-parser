from rest_framework import serializers
from businesses.models import Business
from transactions.models import Transaction

class BusinessSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = [
            "id",
            "owner_name",
            "business_name",
            'balance'
        ]

    def get_balance(self, obj):
        bal = 0
        for transaction in obj.transactions.all():
            if transaction.type == 'Entrada':
                bal += transaction.value
            else:
                bal -= transaction.value

        return bal