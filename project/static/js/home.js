// home page nav

const profile = document.querySelector(".profile");
const nav = document.querySelector(".nav");

// profile.addEventListener('click', () => {
//   if (nav.classList.contains("d-none")){
//     nav.classList.remove("d-none");
//   } else {
//     nav.classList.add("d-none");
//   }
// });

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

const emotionSelectors = document.querySelectorAll('.emotions');
const title = document.getElementById('title');
const synonym = document.getElementById('synonym');
const about = document.getElementById('about');
const help = document.getElementById('help');
const aboutQuestion = document.getElementById('about-question');
const helpQuestion = document.getElementById('help-question');

const emotionAreaIdentifiers = ['38', '30', '29',
  '28', '31', 'Group_1540',
  '34', '17', '7',
  '35', '11', '8',
  '36', '12', '14',
  '25', '21', '13',
  '37', '15', '9',
  'Group_1525', '19', '10',
  '27', '26', '6', '5', '4', '3', '2', '1', '40']  // selectors for clickable areas corresponding to an emotion have these IDs
const emptyAreaIdentifiers = ['33', '32', '16', '24', '23', '22', '20', '18']  // selectors for empty areas, not corresponding to any emotion


fetch('http://localhost:5000/api/emotionlist')
  .then((response) => {
    if (!response.ok) {
      throw Error('ERROR');
    }
    return response.json();
  })
  .then((data) => {
    emotionNamesData = data
    console.log(emotionNamesData)
  })


for (let i = 0; i < emotionSelectors.length; i++) {
  emotionSelectors[i].addEventListener('click', () => {
    if (!emptyAreaIdentifiers.includes(emotionSelectors[i].id)) {
        let correctIndex = emotionAreaIdentifiers.indexOf(emotionSelectors[i].id)

        title.innerHTML = emotionNamesData[correctIndex].emotion;
        synonym.innerHTML = emotionNamesData[correctIndex].synonym;
        about.innerHTML = emotionNamesData[correctIndex].example;
        help.innerHTML = emotionNamesData[correctIndex].example;
        aboutQuestion.innerHTML = "რას გვეუბნება " + emotionNamesData[correctIndex].emotion + ":"
        helpQuestion.innerHTML = "როგორ დაგეხმარება " + emotionNamesData[correctIndex].emotion + ":"
  }
  });
}
