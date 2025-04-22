document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault(); // منع إرسال الفورم

    const englishName = document.getElementById('english_name').value;
    const photo = document.getElementById('photo').files[0];
    const message = document.getElementById('message');

    // إعادة تعيين الرسالة
    message.className = 'message';
    message.textContent = '';

    // التحقق من الاسم الإنجليزي
    if (!englishName) {
        message.textContent = 'رجاءً أدخل الاسم بالإنجليزي.';
        message.className = 'message error';
        setTimeout(() => { message.className = 'message'; message.textContent = ''; }, 5000);
        return;
    }

    if (!/^[A-Za-z\s]+$/.test(englishName)) {
        message.textContent = 'الاسم الإنجليزي يجب أن يحتوي على حروف فقط.';
        message.className = 'message error';
        setTimeout(() => { message.className = 'message'; message.textContent = ''; }, 5000);
        return;
    }

    // التحقق من الصورة
    if (!photo) {
        message.textContent = 'رجاءً ارفع صورة شخصية.';
        message.className = 'message error';
        setTimeout(() => { message.className = 'message'; message.textContent = ''; }, 5000);
        return;
    }

    if (photo.size > 2 * 1024 * 1024) { // 2MB
        message.textContent = 'الصورة كبيرة جدًا، الحد الأقصى 2 ميجابايت.';
        message.className = 'message error';
        setTimeout(() => { message.className = 'message'; message.textContent = ''; }, 5000);
        return;
    }

    // عرض البيانات
    document.getElementById('english-name').textContent = englishName;
    document.getElementById('english-name-section').style.display = 'block';

    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('profile-photo').src = e.target.result;
        document.getElementById('photo-section').style.display = 'block';
    };
    reader.readAsDataURL(photo);

    // إغلاق الـ Modal
    const modal = bootstrap.Modal.getInstance(document.getElementById('profileModal'));
    modal.hide();

    // رسالة نجاح
    message.textContent = 'تم تحديث البروفايل بنجاح!';
    message.className = 'message success';
    setTimeout(() => { message.className = 'message'; message.textContent = ''; }, 5000);

    // إعادة تعيين الفورم
    document.getElementById('profile-form').reset();
});