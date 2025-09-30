from rest_framework import serializers
from django.db.models import Sum
from .models import Budget
from transaction.models import Transaction

class BudgetSerializer(serializers.ModelSerializer):
    spent_amount = serializers.SerializerMethodField()
    remaining_amount = serializers.SerializerMethodField()
    over_budget = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ("id", "title", "total_amount", "start_date", "end_date",
                  "spent_amount", "remaining_amount", "over_budget",
                  "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at", "spent_amount", "remaining_amount", "over_budget")

    def get_spent_amount(self, obj):
        qs = Transaction.objects.filter(
            user=obj.user,
            type=Transaction.EXPENSE,
            date__gte=obj.start_date,
            date__lte=obj.end_date
        )
        agg = qs.aggregate(total=Sum("amount"))
        return agg["total"] or 0

    def get_remaining_amount(self, obj):
        return float(obj.total_amount) - float(self.get_spent_amount(obj))

    def get_over_budget(self, obj):
        return self.get_spent_amount(obj) > float(obj.total_amount)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user
        return super().create(validated_data)
