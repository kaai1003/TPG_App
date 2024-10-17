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
});