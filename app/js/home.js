// home page nav

const profile = document.querySelector(".profile");
const nav = document.querySelector(".nav");

profile.addEventListener('click', () => {
  if (nav.classList.contains("d-none")){
    nav.classList.remove("d-none");
  } else {
    nav.classList.add("d-none");
  }
});

const leng_checkbox = document.getElementById('lang-checkbox');
const geo = document.getElementById('geo');
const eng = document.getElementById('eng')

leng_checkbox.addEventListener('change', () => {
  if (document.querySelector('#lang-checkbox:checked')) {
    eng.classList.remove("lang__action");
    geo.classList.add("lang__action");
  } else {
    geo.classList.remove("lang__action");
    eng.classList.add("lang__action");
  }
});


// Hortensia

const allObjClass = document.querySelectorAll('.emotions');
const title = document.getElementById('title');
const synonym = document.getElementById('synonym');
const about = document.getElementById('about');
const help = document.getElementById('help');


fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => {
    if (!response.ok) {
      throw Error('ERROR');
    }
    return response.json();
  })
  .then((data) => {
    for (let i = 0; i < allObjClass.length; i++) {
      allObjClass[i].addEventListener('click', () => {
        title.innerHTML = data[i].title; 
        synonym.innerHTML = data[i].title; 
        about.innerHTML = data[i].body; 
        help.innerHTML = data[i].body; 
      });
    }
  });