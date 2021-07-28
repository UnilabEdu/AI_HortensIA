// auth.js handles emails subscriptions, automatically opening relevant auth modals, and translating validator texts


// Automatically open relevant modal (login or register) after an unsuccessful authorization attempt
login_attempt = document.querySelector('#auth-modal .help-block')

register_attempt = document.querySelector('#reg-modal .help-block')

if (login_attempt) {
    auth_modal.classList.add("d-block");
} else if (register_attempt) {
    reg_modal.classList.add("d-block");
}


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
        });
    }
})


// Translate validator texts
let loginHelpTexts_en = ['Username is required', 'Email is required', 'Invalid Email',
    'Password is required', 'Username/Email does not exist', 'Incorrect Password',
    'Email address is required', 'Invalid Email address',
    'This Email is already in use. Please try another one.', 'This Username is already in use. Please try another one.',
    "Username may only contain letters, numbers, '-', '.' and '_'",
    'Username must be at least 3 characters long',
    'Password must have at least 6 characters with one lowercase letter, one uppercase letter and one number',
    ]

let loginHelpTexts_ka = ['შეიყვანეთ მომხმარებლის სახელი', 'შეიყვანეთ ელ-ფოსტა', 'ელ-ფოსტა არასწორადაა შეყვანილი',
    'შეიყვანეთ პაროლი', 'მონაცემები არასწორადაა შეყვანილი', 'პაროლი არასწორია',
    'შეიყვანეთ ელ-ფოსტა', 'ელ-ფოსტა არასწორადაა შეყვანილი',
    'ელ-ფოსტის მისამართი დაკავებულია', 'მომხმარებლის სახელი დაკავებულია',
    "გამოიყენეთ ასოები, ციფრები ან: -, . , _",
    'გამოიყენეთ მინიმუმ 3 სიმბოლო',
    'გამოიყენეთ 6+ სიმბოლო: დიდი/პატარა ასოები, ციფრები',
    ]

let loginHelpTexts_enShort = loginHelpTexts_en.slice()
loginHelpTexts_enShort[8] = 'This Email is already in use';
loginHelpTexts_enShort[9] = 'This Username is already in use';
loginHelpTexts_enShort[10] = 'Use only letters, numbers, -, ., and _'
loginHelpTexts_enShort[11] = 'Use at least 3 characters'
loginHelpTexts_enShort[12] = 'Use 6+ characters: uppercase/lowercase letters, numbers'

let helpTexts = document.querySelectorAll('.help-block')

if (helpTexts.length > 0) {
    for (let i = 0; i < helpTexts.length; i++) {
        let currentTextIndex = loginHelpTexts_en.indexOf(helpTexts[i].innerHTML)
        if (current_lang === 'ka') {
            helpTexts[i].innerHTML = loginHelpTexts_ka[currentTextIndex]
        } else if (current_lang === 'en') {
            helpTexts[i].innerHTML = loginHelpTexts_enShort[currentTextIndex]
        }
    }
}