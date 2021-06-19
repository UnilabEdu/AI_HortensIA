var auth_modal = document.getElementById("auth-modal");
var reg_modal = document.getElementById("reg-modal");

// Get the button that opens the modal
var auth_btn = document.getElementById("auth-btn");
var reg_btn = document.getElementById("reg-btn");

// Get the <span> element that closes the modal

var span_close_1 = document.getElementsByClassName("close")[0];
var span_close_2 = document.getElementsByClassName("close")[1];

// When the user clicks on the button, open the modal
auth_btn.onclick = function () {
  auth_modal.classList.add("d-block");
  if(auth_inside_cont.classList.contains("d-none")){
    auth_inside_cont.classList.remove("d-none");
    reset_pass_cont.classList.add("d-none");
  }
};

reg_btn.onclick = function () {
  reg_modal.classList.add("d-block");
};

// When the user clicks on <span> (x), close the modal
span_close_1.onclick = function () {
  auth_modal.classList.remove("d-block");
};
span_close_2.onclick = function () {
  reg_modal.classList.remove("d-block");
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == auth_modal) {
    auth_modal.classList.remove("d-block");
  } else if (event.target == reg_modal) {
    reg_modal.classList.remove("d-block");
  }
};

// togle modals
const auth_inside_cont = document.querySelector(".auth__left__container");
const reset_pass_cont = document.querySelector(".reset__pass__left__container")
const enter_btn = document.querySelector(".enter__btn");
const inside_reg_btn = document.querySelector(".reg__btn");
const reset_password = document.querySelector(".reset__password")

enter_btn.addEventListener("click", () => {
  auth_modal.classList.add("d-block");
  reg_modal.classList.remove("d-block");
  if(auth_inside_cont.classList.contains("d-none")){
    auth_inside_cont.classList.remove("d-none");
    reset_pass_cont.classList.add("d-none");
  }
});
inside_reg_btn.addEventListener("click", () => {
  auth_modal.classList.remove("d-block");
  reg_modal.classList.add("d-block");
});
reset_password.addEventListener('click', () => {
    auth_inside_cont.classList.add("d-none");
    reset_pass_cont.classList.remove("d-none");
})
