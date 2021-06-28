var auth_modal = document.getElementById("auth-modal");
var reg_modal = document.getElementById("reg-modal");
var ticket_modal = document.getElementById("ticket-modal");

// Get the button that opens the modal
var auth_btn = document.getElementById("auth-btn");
var reg_btn = document.getElementById("reg-btn");
var ticket_btn = document.getElementById("ticket-btn");

// Get the <span> element that closes the modal

var span_close_1 = document.getElementsByClassName("close")[0];
var span_close_2 = document.getElementsByClassName("close")[1];
var span_close_3 = document.getElementsByClassName("close")[2];

// When the user clicks on the button, open the modal
auth_btn.onclick = function () {
  auth_modal.classList.add("d-block");
};

reg_btn.onclick = function () {
  reg_modal.classList.add("d-block");
};

ticket_btn.onclick = function () {
  ticket_modal.classList.add("d-block");
};

// When the user clicks on <span> (x), close the modal
span_close_1.onclick = function () {
  ticket_modal.classList.remove("d-block");
};
span_close_2.onclick = function () {
  auth_modal.classList.remove("d-block");
};
span_close_3.onclick = function () {
  reg_modal.classList.remove("d-block");
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == auth_modal) {
    auth_modal.classList.remove("d-block");
  } else if (event.target == reg_modal) {
    reg_modal.classList.remove("d-block");
  } else if (event.target == ticket_modal){
    ticket_modal.classList.remove("d-block");
  }
};
