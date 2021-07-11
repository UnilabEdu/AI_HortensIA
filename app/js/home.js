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
    eng.classList.remove("lang__action");
    geo.classList.add("lang__action");
  } else {
    geo.classList.remove("lang__action");
    eng.classList.add("lang__action");
  }
});


// Hortensia
// const AI_hortensia = {
//   0: {
//     id: 1,
//     tit: "blabla1",
//     sinonimi: 'sinonimi1',
//     rasgv: 'bskdlfahdsklfhasdf',
//     rogdag: 'foasdfas'
//   },
//   1: {
//     id: 2,
//     tit: "blabla2",
//     sinonimi: 'sinonimi2',
//     rasgv: 'bskdlfahdskl222222222222',
//     rogdag: 'foasdfa222 2222 222222 222'
//   }  
// }
const allObjClass = document.querySelectorAll('.emotions');
var x = document.getElementById('title');

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
        x.innerHTML = data[i].title; 
      });
    }
  });




// function my(e) {
//   var element = e.document.getElementById(id);
//   AI_hortensia.e
//   x.innerHTML = "Swapped text!";
// }


// for (let o = 0; o < AI_hortensia.length; o++) {
//   console.log('gkns')
//   if(allObjClass[i] == AI_hortensia[o]){
//     console.log('bal')
//     x.innerHTML = AI_hortensia[i.tit];
//   }
// }  