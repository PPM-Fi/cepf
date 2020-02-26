document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    var dateElems = document.querySelectorAll('.datepicker');
    var dateInstances = M.Datepicker.init(dateElems, {format:'yyyy-mm-dd'});

    var timeElems = document.querySelectorAll('.timepicker');
    var timeInstances = M.Timepicker.init(timeElems);
  });
