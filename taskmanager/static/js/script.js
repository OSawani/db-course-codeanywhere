document.addEventListener("DOMContentLoaded", function() {
  // Sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // Modal initialization
  let modals = document.querySelectorAll('.modal');
  M.Modal.init(modals);
});

  /*
  We are actually going to be using a few different elements from Materialize, so let's give our
  variables a more unique name.
  The querySelector will be 'sidenav', and then we'll just initialize that without defining any variable.
  */