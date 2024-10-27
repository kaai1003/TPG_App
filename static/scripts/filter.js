document.addEventListener('DOMContentLoaded', function() {
  const categories = document.getElementById('category1');
  const filters = document.getElementById('category2');
  
  // Example options mapped by category value
  const optionsMap = {
      connectors: [
          { value: 'serial_number', text: 'Serial Number' },
          { value: 'supplier_id', text: 'Supplier' },
          { value: 'terminals', text: 'Terminals' }
      ],
      testmodules: [
        { value: 'serial_number', text: 'Serial Number' },
        { value: 'supplier_id', text: 'Supplier' },
        { value: 'connector_id', text: 'Connector' },
        { value: 'probeid', text: 'Probe' },
        { value: 'terminals', text: 'Terminals' }
      ],
      testprobes: [
        { value: 'serial_number', text: 'Serial Number' },
        { value: 'supplier_id', text: 'Supplier' },
      ],
      suppliers: [
          { value: 'name', text: 'Name' },
          { value: 'type', text: 'Type' }
      ]
  };
  
  categories.addEventListener('change', function() {
      const selectedCategory = categories.value;

      // Clear current options in filters
      filters.innerHTML = '<option value="selected">Select Filter</option>';

      // Check if a valid category is selected and populate filters
      if (optionsMap[selectedCategory]) {
          optionsMap[selectedCategory].forEach(option => {
              const newOption = document.createElement('option');
              newOption.value = option.value;
              newOption.text = option.text;
              filters.appendChild(newOption);
          });
          filters.disabled = false; // Enable category2
          filters.addEventListener('change', function() {
            const selectedFilter = filters.value;
          });
      } else {
          filters.disabled = true; // Disable category2 if no valid selection
      }
  });
});