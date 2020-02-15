document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    var dropdownElems = document.querySelectorAll('.dropdown-trigger');
    var dropdownInstances = M.Dropdown.init(dropdownElems, { hover: false });

    var collapsableElems = document.querySelectorAll('.collapsible');
    var collapsableInstances = M.Collapsible.init(collapsableElems);
  });
