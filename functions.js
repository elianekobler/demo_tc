/// Initialize variables
let currentDate = new Date();    // Default to today



// Handle tab switching
function openTab(evt, tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tabcontent');
    tabContents.forEach(content => content.style.display = 'none');  // Hide all content

    // Remove 'active' class from all tab links
    const tabLinks = document.querySelectorAll('.tablinks');
    tabLinks.forEach(link => link.classList.remove('active'));  // Remove active class
    
    // Show the corresponding tab content
    document.getElementById(tabName).style.display = 'block';
    
     // Add 'active' class to the clicked tab link (button)
    evt.currentTarget.classList.add('active');

    if (tabName === 'tc_forecast') {
       updateOverview();
    }
}

// Show today's date for the availability range of the plots
document.getElementById('date_display').textContent = currentDate.toDateString();

// Handling date changes
document.getElementById('btn_before').addEventListener('click', function() {
    currentDate.setDate(currentDate.getDate() - 1); // Move to previous day
    updateOverview(); // Update tc overview plot
});

document.getElementById('btn_after').addEventListener('click', function() {
    currentDate.setDate(currentDate.getDate() + 1); // Move to next day
    updateOverview(); 
});

// Handling date submission from the input field
document.getElementById('inp_sel_date').addEventListener('change', function() {
    currentDate = new Date(document.getElementById('inp_sel_date').value); // Set the selected date
    updateOverview(); // Update tc overview plot
});

// Functions for the TC tab
function updateOverview () {
    const plotArea = document.getElementById('plot_area'); // Your common plot container
    const dateStr = currentDate.toISOString().split('T')[0]; // Format date to YYYY-MM-DD
    const times = ['12', '00'];

    // Update the date input field to reflect the selected date
    document.getElementById('inp_sel_date').value = dateStr;

    // Clear the previous plots
    plotArea.innerHTML = '';
    
    function checkIfImageExists(dateStr, time) {
      return new Promise((resolve) => {
          const img = new Image();
          img.onload = () => resolve(true);
          img.onerror = () => resolve(false);
          img.src = `./images/${dateStr}_${time}UTC/ECMWF_TC_tracks_${dateStr}_${time}UTC.png`;
      });
    }

    function addImage(dateStr, time) {
        const img = document.createElement('img');
        img.src = `./images/${dateStr}_${time}UTC/ECMWF_TC_tracks_${dateStr}_${time}UTC.png`;
        img.alt = '';
        plotArea.appendChild(img);
    }

    // Check both times
    Promise.all(times.map(time => checkIfImageExists(dateStr, time)))
      .then(results => {
          const [exists12, exists00] = results;
          
          if (exists12) {
              addImage(dateStr, '12');
          }
          
          if (exists00) {
              addImage(dateStr, '00');
          }
          
          if (!exists12 && !exists00) {
            const img = document.createElement('img');
            img.alt = 'No images available for the selected date';
            plotArea.appendChild(img);
            console.log('No images available for the selected date.');
          }
      });
}

// Handle page load
document.addEventListener('DOMContentLoaded', function() {
    // Set the default active tab (Tab 1) when the page loads
    const defaultTab = document.querySelector('.tablinks.active');
    if (defaultTab) {
        // Trigger the click event for the default active tab to show its content
        openTab({ currentTarget: defaultTab }, 'tc_forecast');
    }
    updateOverview();
});