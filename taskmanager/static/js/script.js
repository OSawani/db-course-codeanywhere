document.addEventListener("DOMContentLoaded", function() {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // datepicker initialization
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}
  });

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);
});

  /*
  We are actually going to be using a few different elements from Materialize, so let's give our
  variables a more unique name.
  The querySelector will be 'sidenav', and then we'll just initialize that without defining any variable.
  */