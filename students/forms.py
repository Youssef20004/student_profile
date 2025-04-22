
from django import forms
from .models import Student

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['english_name', 'photo']
        labels = {
            'english_name': 'الاسم بالإنجليزي',
            'photo': 'الصورة الشخصية',
        }
        widgets = {
            'english_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'أدخل الاسم بالإنجليزية'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100',
                'accept': 'image/jpeg,image/png'
            }),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # التحقق من الحجم
            if photo.size > 2 * 1024 * 1024:  # 2MB
                raise forms.ValidationError("الصورة كبيرة جدًا، الحد الأقصى 2 ميجابايت.")
            # التحقق من الصيغة
            ext = photo.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError("يُسمح فقط بصور بصيغة PNG أو JPG.")
        return photo

    def clean_english_name(self):
        english_name = self.cleaned_data.get('english_name')
        if english_name and not all(c.isalpha() or c.isspace() for c in english_name):
            raise forms.ValidationError("الاسم الإنجليزي يجب أن يحتوي على حروف فقط.")
        return english_name
