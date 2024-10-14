$(document).ready(function(){
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
  // Upload some data to table
  $.ajax({
		url: 'http://localhost:5000/api/v1/users/', // The Flask API endpoint
		type: 'GET',
		success: function(data) {
			// Handle success response
			const headTable = $('#table-head');
			headTable.empty();
			const checkbox = '<th>' +
													'<span class="custom-checkbox">' +
														'<input type="checkbox" id="selectAll">' +
														'<label for="selectAll"></label>' +
													'</span>' +
												'</th>';
			headTable.append(checkbox);
			const headers = ['Id', 'User', 'Role', 'Actions']
			headers.forEach(function(header) {
				const th = '<th>' + header + '</th>';
				headTable.append(th);
			});
			const dataTable = $('#data-table tbody');
			dataTable.empty();
			data.forEach(function(item) {
				dataTable.append('<tr>')
				const dtCheck = '<td>' +
												'<span class="custom-checkbox">' +
													'<input type="checkbox" id="checkbox1" name="options[]" value="1">' +
													'<label for="checkbox1"></label>' +
												'</span>' +
											'</td>';
				dataTable.append(dtCheck);
				const td = '<td>' + item.id + '</td>' +
										'<td>' + item.user + '</td>' +
										'<td>' + item.role + '</td>';
				dataTable.append(td);
				const dtAction = '<td>' +
														'<a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>' +
														'<a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>' +
													'</td>';
				dataTable.append(dtAction);
				dataTable.append('</tr>');
			})
		},
	});
});
