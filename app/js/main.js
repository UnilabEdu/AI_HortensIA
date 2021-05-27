var auth_modal = document.getElementById("auth-modal");
var reg_modal = document.getElementById("reg-modal");


// Get the button that opens the modal
var auth_btn = document.getElementById("auth-btn");
var reg_btn = document.getElementById("reg-btn");

// Get the <span> element that closes the modal

var span_close_1 = document.getElementsByClassName("close")[0];
var span_close_2 = document.getElementsByClassName("close")[1];


// When the user clicks on the button, open the modal
auth_btn.onclick = function() {
    auth_modal.style.display = "block";
}

reg_btn.onclick = function() {
    reg_modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_close_1.onclick = function() {
    auth_modal.style.display = "none";
}
span_close_2.onclick = function() {
    reg_modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == auth_modal) {
        auth_modal.style.display = "none";
    }
    else if (event.target == reg_modal){
        reg_modal.style.display = "none";
    }
}