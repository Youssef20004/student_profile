from django.db import models

def student_photo_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if ext not in ['jpg', 'jpeg', 'png']:
        ext = 'jpg'  
    filename = f"{instance.code}.{ext}"

    return f"photos/{filename}"

class Student(models.Model):
    arabic_name = models.CharField(max_length=100, blank=True, verbose_name="الاسم بالعربي")
    seat_number = models.CharField(max_length=9, unique=True, verbose_name="رقم الجلوس")
    code = models.CharField(max_length=10, unique=True, verbose_name="كود الطالب")
    national_id = models.CharField(max_length=14, unique=True, verbose_name="الرقم القومي")
    english_name = models.CharField(max_length=100, blank=True, verbose_name="الاسم بالإنجليزي")
    photo = models.ImageField(upload_to=student_photo_path, blank=True, null=True, verbose_name="الصورة")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['seat_number', 'national_id']),
        ]
        ordering = ['-created']
        # verbose_name = "طالب"
        # verbose_name_plural = "الطلاب"

    def __str__(self):
        return self.arabic_name

        