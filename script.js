function toggleDropdown(event) {
    const dropdown = event.target.nextElementSibling;
    dropdown.style.display =
      dropdown.style.display === "block" ? "none" : "block";
  }
  
  /*3rd*/

  function toggleAbout() {
    var shortAbout = document.getElementById('about-short');
    var fullAbout = document.getElementById('about-full');
    if (shortAbout.classList.contains('d-none')) {
      shortAbout.classList.remove('d-none');
      fullAbout.classList.add('d-none');
    } else {
      shortAbout.classList.add('d-none');
      fullAbout.classList.remove('d-none');
    }
  }


  document.addEventListener('DOMContentLoaded', function() {
    var tooltipIcon = document.getElementById('tooltip-icon');
    var tooltip = tooltipIcon.querySelector('.tooltip');
  
    tooltipIcon.addEventListener('mouseenter', function() {
      tooltip.style.visibility = 'visible';
    });
  
    tooltipIcon.addEventListener('mouseleave', function() {
      tooltip.style.visibility = 'hidden';
    });
  });
  
  
  /*documents*/

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.show-more-button').forEach(button => {
        button.addEventListener('click', function() {
            let parentBox = this.closest('.show-more-box');
            let listLinks = parentBox.querySelector('.list-links');
            listLinks.style.maxHeight = listLinks.style.maxHeight ? '' : listLinks.scrollHeight + 'px';
            this.setAttribute('aria-expanded', this.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
        });
    });
});
