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
  // const catgs = document.querySelectorAll('.sidebar a');
  // catgs.forEach(function(catg) {
  //   catg.addEventListener('click', function(e) {
  //     e.preventDefault();
  //     const catgText = this.innerText;
  //     if (catgText === ' Connectors') {
  //       window.location.href = `/connectors`;
  //     }
  //     if (catgText === ' TestProbes') {
  //       window.location.href = `/TestProbes`;
  //     }
  //     if (catgText === ' TestModules') {
  //       window.location.href = `/TestModules`;
  //     }
  //     if (catgText === ' Suppliers') {
  //       window.location.href = `/Suppliers`;
  //     }
  //     return;
  //   });
  // });
	$('#addForm').on("submit", function(event) {
    event.preventDefault();  // Prevent the default form submission

    // Collect form data
    let pushBack = $('#addEmployeeModal').find('#pushback').val();
    if (pushBack === 'true') {
      pushBack = true;
    } else if (pushBack === 'false') {
      pushBack = false;
    } else {
      Swal.fire({
        title: 'Error Pusback',
        text: 'Pushback should true or false!!!!',
        icon: 'error',
        width: '400px'
      });
      return;
    }
		const formData = {
      'serial_number': $('#addEmployeeModal').find('#serial_number').val(),
      'terminals': $('#addEmployeeModal').find('#terminals').val(),
      'pushback': pushBack,
      'supplier_id': $('#addEmployeeModal').find('#supplier_id').val(),
      'connector_id': $('#addEmployeeModal').find('#connector_id').val(),
      'probeid': $('#addEmployeeModal').find('#probeid').val()
		};
        
        // Example: Logging form data (you can modify it to send the data using AJAX)
    console.log(formData);

        // You can now send the form data using AJAX
		$.ajax({
			url: 'http://localhost:5000/api/v1/testmodules', // The Flask API endpoint
			type: 'POST',
			contentType: 'application/json',
			data: JSON.stringify(formData),
			success: function(resp) {
			  // Handle success response
			  console.log(resp)
        window.location.href = `/TestProbes`;
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
      url: 'http://localhost:5000/api/v1/testmodules/' + itemId, // The Flask API endpoint
      type: 'GET',
      success: function(resp) {
        // Handle success response
        console.log(resp);
        $('#editEmployeeModal').find('#serial_number').val(resp.serial_number);
        $('#editEmployeeModal').find('#terminals').val(resp.terminals);
        $('#editEmployeeModal').find('#pushback').val(resp.pushback);
        $('#editEmployeeModal').find('#supplier_id').val(resp.supplier_id);
        $('#editEmployeeModal').find('#connector_id').val(resp.connector_id);
        $('#editEmployeeModal').find('#probeid').val(resp.probeid);
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
        'puchback': $('#editEmployeeModal').find('#puchback').val(),
        'supplier_id': $('#editEmployeeModal').find('#supplier_id').val(),
        'connector_id': $('#editEmployeeModal').find('#connector_id').val(),
        'probeid': $('#editEmployeeModal').find('#probeid').val()
      };
      $.ajax({
        url: 'http://localhost:5000/api/v1/testmodules/' + itemId, // The Flask API endpoint
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/testmodules`;
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
        url: 'http://localhost:5000/api/v1/testmodules/' + itemId, // The Flask API endpoint
        type: 'DELETE',
        success: function(resp) {
          // Handle success response
          console.log(resp)
          window.location.href = `/testmodules`;
        },
        error: function(err) {
          console.log(err);
        }
      });
    });
  });
});