/* superbook/superbook/static/js/script.js */
// JavaScript utilities for SuperBook

document.addEventListener('DOMContentLoaded', function() {
  // Inicializar tooltips do Bootstrap se necessário
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});
