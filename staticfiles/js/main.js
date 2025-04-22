document.getElementById('login-form').addEventListener('submit', function(event) {
    const seatNumber = document.getElementById('seat-number').value;
    const errorMessage = document.getElementById('error-message');

    // إعادة تعيين الرسالة
    errorMessage.classList.remove('show');
    errorMessage.textContent = '';

    // التحقق من رقم الجلوس
    if (!seatNumber) {
        event.preventDefault();
        errorMessage.textContent = 'رجاءً أدخل رقم الجلوس.';
        errorMessage.classList.add('show');
        hideErrorAfterDelay(errorMessage);
        return;
    }

    if (seatNumber.length < 5) {
        event.preventDefault();
        errorMessage.textContent = 'رقم الجلوس يجب أن يكون 5 أرقام على الأقل.';
        errorMessage.classList.add('show');
        hideErrorAfterDelay(errorMessage);
        return;
    }
});

function hideErrorAfterDelay(element) {
    setTimeout(() => {
        element.classList.remove('show');
        element.textContent = '';
    }, 5000); // إخفاء بعد 5 ثوانٍ
}

// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

