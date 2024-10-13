$(document).ready(function() {
  $('form.login-form').on('submit', function(e) {
    e.preventDefault(); // Prevent the form from actually submitting

    // Get the username and password values
    var username = $('input[placeholder="username"]').val();
    if (username === '') {
      alert("Missinig User Name!!!!");
      return;
    }
    var password = $('input[placeholder="password"]').val();
    if (password === '') {
      alert("Missinig User Password!!!!");
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
          alert('Welcome :' + resp.user); // Display success message
          // You can redirect to a new page or take other actions
        } else {
          alert("User Password Not Correct!!!"); // Display failure message
        }
      },
      error: function(xhr, status, err) {
        alert("User Not Found");
      },
    });
  });
});