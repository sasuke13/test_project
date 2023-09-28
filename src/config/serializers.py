from rest_framework import serializers


class RevenueWithoutSpendDTOSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)


class SpendDTOSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    spend = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    impressions = serializers.IntegerField(default=0)
    clicks = serializers.IntegerField(default=0)
    conversion = serializers.IntegerField(default=0)
    revenue = RevenueWithoutSpendDTOSerializer(required=False, many=True)


class SpendWithoutRevenueDTOSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    spend = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    impressions = serializers.IntegerField(default=0)
    clicks = serializers.IntegerField(default=0)
    conversion = serializers.IntegerField(default=0)


class RevenueDTOSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    spend = SpendWithoutRevenueDTOSerializer()
    date = serializers.DateField()
    revenue = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)
