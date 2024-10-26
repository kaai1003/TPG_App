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
			'serial_number': $('#addEmployeeModal').find('#serial_number').val(),
			'terminals': $('#addEmployeeModal').find('#terminals').val(),
			'supplier_id': $('#addEmployeeModal').find('#supplier_id').val(),
			'photo': $('#addEmployeeModal').find('#photo').val()
		};
        
        // Example: Logging form data (you can modify it to send the data using AJAX)
    console.log(formData);

        // You can now send the form data using AJAX
		$.ajax({
			url: 'http://localhost:5000/api/v1/connectors', // The Flask API endpoint
			type: 'POST',
			contentType: 'application/json',
			data: JSON.stringify(formData),
			success: function(resp) {
			  // Handle success response
			  console.log(resp)
        window.location.href = `/connectors`;
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
      url: 'http://localhost:5000/api/v1/connectors/' + itemId, // The Flask API endpoint
      type: 'GET',
      success: function(resp) {
        // Handle success response
        console.log(resp);
        $('#editEmployeeModal').find('#serial_number').val(resp.serial_number);
        $('#editEmployeeModal').find('#terminals').val(resp.terminals);
        $('#editEmployeeModal').find('#supplier_id').val(resp.supplier_id);
        $('#editEmployeeModal').find('#photo').val(resp.photo);
      },
      error: function(err) {
        console.log(err);
      },
    });
    $('#editForm').on("submit", function(event) {
      event.preventDefault();
      const formData = {
        'serial_number': $('#editEmployeeModal').find('#serial_number').val(),
        'terminals': $('#editEmployeeModal').find('#terminals').val(),
        'supplier_id': $('#editEmployeeModal').find('#supplier_id').val(),
        'photo': $('#editEmployeeModal').find('#photo').val()
      };
      $.ajax({
        url: 'http://localhost:5000/api/v1/connectors/' + itemId, // The Flask API endpoint
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/connectors`;
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
        url: 'http://localhost:5000/api/v1/connectors/' + itemId, // The Flask API endpoint
        type: 'DELETE',
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/connectors`;
        },
        error: function(err) {
          console.log(err);
        }
      });
    });
  });
});