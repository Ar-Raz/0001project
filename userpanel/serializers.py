from rest_framework import serializers

from .models import ProducerTicket

class ProducerTicketQuickSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProducerTicket
        fields = (
            'id',
            'subject',
            'priorty',
            'timestamp',
        )

class ProducerTicketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProducerTicket
        fields = (
            'id',
            'subject',
            'content',
            'priorty',
            'is_responded',
            'timestamp',
        )