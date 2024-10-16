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
  const headTable = $('#table-head');
  const dataTable = $('#data-table tbody');
  
  // Clear previous table headers and rows
  headTable.empty();
  dataTable.empty();
  // Upload Data According to Clicked Category
  const catgs = document.querySelectorAll('.sidebar a');
  catgs.forEach(function(catg) {
    catg.addEventListener('click', function(e) {
      e.preventDefault();
      const catgText = this.innerText;
      const tbTitle = document.getElementById('cat-title');
      tbTitle.innerText = catgText;
      if (catgText === ' Connectors') {
        $.ajax({
          url: 'http://localhost:5000/api/v1/connectors/', // The Flask API endpoint
          type: 'GET',
          success: function(data) {
            const headTable = $('#table-head');
            const dataTable = $('#data-table tbody');
            
            // Clear previous table headers and rows
            headTable.empty();
            dataTable.empty();
            
            // Add table headers
            const headers = ['part_number', 'terminals', 'supplier_id', 'Actions'];
            const headerRow = `
                <th>
                    <span class="custom-checkbox">
                        <input type="checkbox" id="selectAll">
                        <label for="selectAll"></label>
                    </span>
                </th>
                ${headers.map(header => `<th>${header}</th>`).join('')}
            `;
            headTable.append(headerRow);
      
            // Add table rows
            data.forEach(function(item, index) {
                const row = `
                    <tr>
                        <td>
                            <span class="custom-checkbox">
                                <input type="checkbox" id="checkbox${index}" name="options[]" value="${item.id}">
                                <label for="checkbox${index}"></label>
                            </span>
                        </td>
                        <td>${item.part_number}</td>
                        <td>${item.terminals}</td>
                        <td>${item.supplier_id}</td>
                        <td>
                            <a href="#editEmployeeModal" class="edit" data-toggle="modal">
                                <i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i>
                            </a>
                            <a href="#deleteEmployeeModal" class="delete" data-toggle="modal">
                                <i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i>
                            </a>
                        </td>
                    </tr>
                `;
                dataTable.append(row);
            });
          },
        });
        
      }
    });
  });
});