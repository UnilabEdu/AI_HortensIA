// tickets.js handles fetching the text from backend to mark in tickets view, updating
// the text, fetching emotions data, selecting emotions from the emotion-wheel, submitting a ticket


// Initialize the first sentence, create a function for displaying the next sentence

const targetCardText = document.getElementById('target-card-text');
const nextButton = document.getElementById('next-submit-ticket')

var fetchNextText = async function () {
    let response = await fetch('/api/ticketrequest');
    return await response.json();
};

async function displayNextText() {
    currentTextData = await fetchNextText();
    if (currentTextData.text) {
        targetCardText.style.opacity = 1
        targetCardText.innerHTML = currentTextData.text

        targetCardText.animate([
          { transform: 'translate3D(-2000px, 0, 0)' },
          { transform: 'translate3D(0, 0, 0)' }
        ], {
          duration: 1500,
          iterations: 1
        })
        targetCardText.style.right = 0
        targetCardText.style.position = 'static'

        targetCardText.style.color = '#000000'
        nextButton.style.opacity = 1
    } else {
        targetCardText.innerHTML = txt.ticket.nomore
        targetCardText.style.color = '#320606'
        nextButton.style.opacity = 0.5
        nextButton.disabled = true
    }
}

displayNextText()




// Update Current Emotion Info by clicking on Selector Areas

const emotionSelectors = document.querySelectorAll('.emotions');
const title = document.getElementById('title');
const synonym = document.getElementById('synonym');
const about = document.getElementById('about');
const aboutQuestion = document.getElementById('about-question');

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


fetch('/api/emotionlist')
  .then((response) => {
    if (!response.ok) {
      throw Error('ERROR');
    }
    return response.json();
  })
  .then((data) => {
    emotionNamesData = data
  })


for (let i = 0; i < emotionSelectors.length; i++) {
  emotionSelectors[i].addEventListener('click', () => {
    if (!emptyAreaIdentifiers.includes(emotionSelectors[i].id)) {
        let correctIndex = emotionAreaIdentifiers.indexOf(emotionSelectors[i].id)

        title.innerHTML = emotionNamesData[correctIndex].emotion;
        synonym.innerHTML = emotionNamesData[correctIndex].similar;
        about.innerHTML = emotionNamesData[correctIndex].definition;
        aboutQuestion.innerHTML = txt.ticket.about[0] + emotionNamesData[correctIndex].emotion + txt.ticket.about[1]
        nextButton.disabled = false

        chosenEmotion = correctIndex
  }
  });
}




// Initialize function to reset the selected emotion after the emotion is submitted

function resetSelectedEmotion() {
    title.innerHTML = txt.ticket.reset.title
    synonym.innerHTML = txt.ticket.reset.synonym
    about.innerHTML = txt.ticket.reset.about
    aboutQuestion.innerHTML = txt.ticket.reset.about_question
    nextButton.disabled = true

    chosenEmotion = null
}




// Send a POST request by clicking on Next button, submit data, and move on to the next sentence

successField = document.getElementById('ticket-submit-success')

nextButton.addEventListener('click', function() {
        if (chosenEmotion != null) {
            let text = currentTextData.id
            let emotion = chosenEmotion
            let user = currentTextData.user
            let secret = currentTextData.secret

            fetch('/api/ticketrequest', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    text: text,
                    emotion: emotion,
                    user: user,
                    secret: secret
                })
            }).then(response => response.json())
                .then(data => {
                    successField.style.color = '#054718'
                    successField.innerHTML = txt.ticket.submit + emotionNamesData[chosenEmotion].emotion + ')'
                    successField.style.display = 'block'

                    targetCardText.style.position = 'absolute'
                    targetCardText.animate([
                      { transform: 'translate3D(0, 0, 0)' },
                      { transform: 'translate3D(2000px, 0, 0)' }
                    ], {
                      duration: 1000,
                      iterations: 1
                    })
                    setTimeout(displayNextText(), 1000)
                    resetSelectedEmotion()
                })
                .catch((error) => {
                    successField.style.color = '#47050b'
                    successField.innerHTML = txt.ticket.error
                    successField.style.display = 'block'
                });
        }
    }
)
