$(document).ready(function() {

  handleStatusChanged();

});

$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

function handleStatusChanged() {
    $('#toggleElement').on('change', function () {
      toggleStatus();
    });
}

function toggleStatus() {
    if ($('#toggleElement').is(':checked')) {
        $('#elementsToOperateOn :input').attr('disabled', true);
    } else {
        $('#elementsToOperateOn :input').removeAttr('disabled');
    }
}