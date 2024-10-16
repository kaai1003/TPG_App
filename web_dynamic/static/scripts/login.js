$(document).ready(function() {
  $('form.login-form').on('submit', function(e) {
    e.preventDefault(); // Prevent the form from actually submitting

    // Get the username and password values
    var username = $('input[placeholder="username"]').val();
    if (username === '') {
      Swal.fire({
        title: 'Missing User',
        text: 'Missinig User Name!!!!',
        icon: 'error',
        width: '400px'
      });
      return;
    }
    var password = $('input[placeholder="password"]').val();
    if (password === '') {
      Swal.fire({
        title: 'Missing Password',
        text: 'Missinig User Password!!!!',
        icon: 'error',
        width: '400px'
      });
      return;
    }

    // AJAX request to Flask API
    $.ajax({
      url: 'http://localhost:5000/api/v1/users/' + username, // The Flask API endpoint
      type: 'GET',
      success: function(resp, status, xhr) {
        // Handle success response
        if (resp.password === password) {
          // i want to go to another html page using flask jinja2 main/<user_id>
          window.location.href = `/main/${resp.id}`;
        } else {
          Swal.fire({
            title: 'Login Failed',
            text: 'User Password not Correct!!!!',
            icon: 'error',
            width: '400px'
          }); // Display failure message
        }
      },
      error: function(xhr, status, err) {
        Swal.fire({
          title: 'Login Failed',
          text: 'User not found!!!!',
          icon: 'error',
          width: '400px'
        });
      },
    });
  });
});