$(document).ready(function() {
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
	$('#addForm').on("submit", function(event) {
    event.preventDefault();  // Prevent the default form submission

        // Collect form data
		const formData = {
			'name': $('#addEmployeeModal').find('#name').val(),
			'type': $('#addEmployeeModal').find('#type').val(),
		};
        
        // Example: Logging form data (you can modify it to send the data using AJAX)
    console.log(formData);

        // You can now send the form data using AJAX
		$.ajax({
			url: 'http://localhost:5000/api/v1/suppliers', // The Flask API endpoint
			type: 'POST',
			contentType: 'application/json',
			data: JSON.stringify(formData),
			success: function(resp) {
			  // Handle success response
			  console.log(resp)
        window.location.href = `/Suppliers`;
			},
			error: function(err) {
			  console.log(err);
			}
		});
  });
  $('.edit').on('click', function () {
    const itemId = $(this).data('id');
    // Fetch item details and populate the edit modal
    $.ajax({
      url: 'http://localhost:5000/api/v1/suppliers/' + itemId, // The Flask API endpoint
      type: 'GET',
      success: function(resp) {
        // Handle success response
        console.log(resp);
        $('#editEmployeeModal').find('#name').val(resp.name);
        $('#editEmployeeModal').find('#type').val(resp.type);
      },
      error: function(err) {
        console.log(err);
      },
    });
    $('#editForm').on("submit", function(event) {
      event.preventDefault();
      const formData = {
        'name': $('#editEmployeeModal').find('#name').val(),
        'type': $('#editEmployeeModal').find('#type').val(),
      };
      $.ajax({
        url: 'http://localhost:5000/api/v1/suppliers/' + itemId, // The Flask API endpoint
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/Suppliers`;
        },
        error: function(err) {
          console.log(err);
        }
      });
    });
  });
  $('.delete').on('click', function () {
    const itemId = $(this).data('id');
    $('#deleteForm').on("submit", function(event) {
      event.preventDefault();
      $.ajax({
        url: 'http://localhost:5000/api/v1/suppliers/' + itemId, // The Flask API endpoint
        type: 'DELETE',
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/Suppliers`;
        },
        error: function(err) {
          console.log(err);
        }
      });
    });
  });
});