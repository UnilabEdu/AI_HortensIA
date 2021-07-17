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

const emotionnames =  [
        'რისხვა', 'ბრაზი', 'გაღიზიანება',
        'სიფხიზლე', 'მოლოდინი', 'ინტერესი',
        'აღტყინება', 'სიხარული', 'სიმშვიდე',
        'აღტაცება', 'ნდობა', 'მიმღებლობა',
        'თავზარდამცემი შიში', 'შიში', 'ღელვა',
        'აღფრთოვანება', 'გაკვირვება', 'ყურადღების გაფანტვა',
        'მწუხარება', 'სევდა', 'ნაღვლიანობა',
        'სიძულვილი', 'გულისრევა', 'მოწყენილობა',

        'აგრესია', 'ოპტიმიზმი', 'სიყვარული', 'მორჩილება', 'განცვიფრება', 'გაკიცხვა', 'სინანული', 'ზიზღი', 'ნეიტრალური'
    ]


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
    let correctIndex = emotionAreaIdentifiers.indexOf(emotionSelectors[i].id)
    console.log(emotionnames[correctIndex])
    console.log(correctIndex)
    console.log(emotionSelectors[i].id)
    title.innerHTML = emotionNamesData[correctIndex].emotion;
    synonym.innerHTML = emotionNamesData[correctIndex].emotion;
    about.innerHTML = emotionNamesData[correctIndex].synonym;
    help.innerHTML = emotionNamesData[correctIndex].example;
  });
};









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
