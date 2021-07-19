// Automatically open relevant modal (login or register) after an unsuccessful authorization attempt

login_attempt = document.querySelector('#auth-modal .help-block')

register_attempt = document.querySelector('#reg-modal .help-block')

if (login_attempt) {
    auth_modal.classList.add("d-block");
} else if (register_attempt) {
    reg_modal.classList.add("d-block");
}

// END


// Email subscription functionality

email_submit_btn = document.getElementById('email-subscription-btn')

email_submit_btn.addEventListener('click', function() {
    let email = document.getElementById('email-subscription-input').value
    let help_text = document.getElementById('email-subscription-help-text')
    if (email.length < 1) {
        help_text.innerHTML = txt.subscr.zero
            help_text.style.display = 'block'
    } else if (email.length > 355 || !email.includes('@') || !email.includes('.')) {
        help_text.innerHTML = txt.subscr.invalid
            help_text.style.display = 'block'
    } else {
        fetch('/api/subscribe',{
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({email: email})
      }).then(response => response.json())
        .then(data => {
          help_text.innerHTML = txt.subscr.success
          help_text.style.display = 'block'
        })
        .catch((error) => {
          help_text.innerHTML = txt.subscr.error
          help_text.style.display = 'block'
          console.log(error)
        });
    }
})
