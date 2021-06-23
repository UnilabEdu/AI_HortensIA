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