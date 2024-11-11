from rest_framework import serializers

class PunctSerializer(serializers.Serializer):
    x = serializers.FloatField()
    y = serializers.FloatField()

    def to_representation(self, instance):
        return {"x":instance.x,"y":instance.y}

class LineSerializer(serializers.Serializer):
    p1 = PunctSerializer()
    p2 = PunctSerializer()

    def to_representation(self, instance):
        return {
            "p1": PunctSerializer(instance.p1).data,
            "p2": PunctSerializer(instance.p2).data,
        }