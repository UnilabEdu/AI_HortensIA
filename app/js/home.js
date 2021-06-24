// home page nav

const profile = document.querySelector(".profile");
const nav = document.querySelector(".nav");

profile.addEventListener('click', () => {
    console.log('asdfknsapdjf')
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
    console.log('1');
    eng.classList.remove("lang__action");
    geo.classList.add("lang__action");
  } else {
    console.log("2");
    geo.classList.remove("lang__action");
    eng.classList.add("lang__action");
  }
});