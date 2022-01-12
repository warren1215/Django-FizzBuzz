from rest_framework import serializers
from .models import FizzModel

class FizzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FizzModel
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')
        read_only_fields = ('useragent', 'creation_date')