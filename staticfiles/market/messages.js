// document.addEventListener('DOMContentLoaded', function () {
//     // Check if there are any Django messages
//     {% if messages %}
//         {% for message in messages %}
//             Swal.fire({
//                 icon: "{% if message.tags == 'error' %}error{% else %}success{% endif %}",
//                 title: "{{ message|escapejs }}",  // تأكد من إضافة escapejs
//                 showConfirmButton: false,
//                 timer: 3000
//             });
//         {% endfor %}
//     {% endif %}
// });