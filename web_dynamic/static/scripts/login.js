$(document).ready(function() {
  $('form.login-form').on('submit', function(e) {
    e.preventDefault(); // Prevent the form from actually submitting

    // Get the username and password values
    var username = $('input[placeholder="username"]').val();
    if (username === '') {
      Swal.fire({
        title: 'Missing User',
        text: 'Missinig User Name!!!!',
        icon: 'error'
      });
      return;
    }
    var password = $('input[placeholder="password"]').val();
    if (password === '') {
      Swal.fire({
        title: 'Missing Password',
        text: 'Missinig User Password!!!!',
        icon: 'error'
      });
      return;
    }

    // AJAX request to Flask API
    $.ajax({
      url: 'http://localhost:5000/api/v1/users/' + username, // The Flask API endpoint
      type: 'GET',
      success: function(resp, status, xhr) {
        // Handle success response
        console.log(resp)
        if (resp.password === password) {
          Swal.fire({
            title: 'Login Successful',
            text: 'Welcome, ' + resp.user + '!!!!',
            icon: 'success'
          }).then(() => {
            // After alert is closed, redirect to another page (e.g., dashboard.html)
            window.location.href = './main.html';  // Change this to the desired URL
          });
        } else {
          Swal.fire({
            title: 'Login Failed',
            text: 'User Password not Correct!!!!',
            icon: 'error'
          }); // Display failure message
        }
      },
      error: function(xhr, status, err) {
        Swal.fire({
          title: 'Login Failed',
          text: 'User not found!!!!',
          icon: 'error'
        });
      },
    });
  });
});