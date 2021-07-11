login_attempt = document.querySelector('#auth-modal .help-block')

register_attempt = document.querySelector('#reg-modal .help-block')

if (login_attempt) {
    auth_modal.classList.add("d-block");
} else if (register_attempt) {
    reg_modal.classList.add("d-block");
}
