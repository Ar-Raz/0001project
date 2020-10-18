from rest_framework import serializers

from .models import AboutUs

from hitcount.models import Hit, HitCount

class HitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hit
        fields = ("__all__")

class HitCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = HitCount
        fields = ("__all__")

class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'about_us_content',
        )

class AboutDamirSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'about_damir_content',
        )

class BuyFromDamirSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'buy_from_damir',
        )

class SellInDamirSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'sell_in_damir',
        )


class RulesToUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'terms_and_conditions',
        )

class PrivacyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'privacy_and_policy',
        )
