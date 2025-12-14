from apps.bible_change.users.models.withdrawal import Withdrawal
from rest_framework import serializers

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = ["user","reason","detail","withdrawn_at"]
        read_only_fields = ["user","withdrawn_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        return super().create(validated_data)