# http://localhost:8000/api/students/444544515/
from rest_framework import serializers
from .models import Student
import re

class StudentSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Student
        fields = ['code', 'arabic_name', 'seat_number', 'national_id', 'english_name', 'photo']
        read_only_fields = ['code', 'arabic_name', 'seat_number', 'national_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.photo and hasattr(instance.photo, 'url'):
            request = self.context.get('request')
            if request:
                representation['photo'] = request.build_absolute_uri(instance.photo.url)
            else:
                representation['photo'] = instance.photo.url
        else:
            representation['photo'] = None
        return representation

    def validate_english_name(self, value):
        if value and not all(c.isalpha() or c.isspace() for c in value):
            raise serializers.ValidationError("الاسم الإنجليزي يجب أن يحتوي على حروف فقط.")
        return value

    def validate_photo(self, value):
        if value:
            if value.size > 2 * 1024 * 1024:  # 2MB
                raise serializers.ValidationError("الصورة كبيرة جدًا، الحد الأقصى 2 ميجابايت.")
            ext = value.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise serializers.ValidationError("يُسمح فقط بصور بصيغة PNG أو JPG.")
        return value

    def validate_national_id(self, value):
        if len(value) != 14 or not value.isdigit():
            raise serializers.ValidationError("الرقم القومي يجب أن يكون 14 رقمًا.")
        return value
