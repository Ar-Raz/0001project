from rest_framework import serializers

from .models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            'id',
            'timestamp',
            'about_us_content',
            'about_damir_content',
            'buy_from_damir',
            'sell_in_damir',
            'terms_and_conditions',
            'privacy_and_policy',
        )
