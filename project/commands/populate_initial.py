from flask_script import Command
from project.models import db, Emotion, Text
from project.models.user import User, Role
from flask import current_app
from datetime import datetime
from random import randrange
from essential_generators import DocumentGenerator


gen = DocumentGenerator()


class PopulateInitial(Command):

    def run(self):
        populate_initial()


def populate_initial():
    db.drop_all()
    db.create_all()
    populate_db()


def populate_db():
    admin_role = find_or_create_role("Admin")

    find_or_create_user(username='admin',
                        password=current_app.user_manager.hash_password('password'),
                        email='admin@email.com',
                        role=admin_role)

    find_or_create_user(username='user',
                        password=current_app.user_manager.hash_password('password'),
                        email='user@email.com')

    populate_emotions()
    populate_texts()

    db.session.commit()


def find_or_create_role(name):
    role = Role.query.filter_by(name=name).first()

    if not role:
        role = Role(name)

        db.session.add(role)

    return role


def find_or_create_user(username, password, email, role=None):
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(username=username,
                    password=password,
                    email=email,
                    confirmed_at=datetime.utcnow(),
                    active=True)

        if role:
            user.roles.append(role)

        db.session.add(user)

    return user


def populate_emotions():
    emotions_list_en = [  # Primary Emotions
        "Rage", "Anger", "Annoyance",
        "Vigilance", "Anticipation", "Interest",
        "Ecstasy", "Joy", "Serenity",
        "Admiration", "Trust", "Acceptance",
        "Terror", "Fear", "Apprehension",
        "Amazement", "Surprise", "Distraction",
        "Grief", "Sadness", "Pensiveness",
        "Loathing", "Disgust", "Boredom",
        # Secondary Emotions
        'Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt', 'Neutral'
    ]

    emotions_list_ka = [  # ძირითადი ემოციები TODO: improve translations
        'რისხვა', 'ბრაზი', 'გაღიზიანება',
        'სიფხიზლე', 'მოლოდინი', 'ინტერესი',
        'აღტყინება', 'სიხარული', 'სიმშვიდე',
        'აღტაცება', 'ნდობა', 'მიმღებლობა',
        'თავზარდამცემი შიში', 'შიში', 'ღელვა',
        'აღფრთოვანება', 'გაკვირვება', 'ყურადღების გაფანტვა',
        'მწუხარება', 'სევდა', 'ნაღვლიანობა',
        'სიძულვილი', 'გულისრევა', 'მოწყენილობა',
        # დამატებითი ემოციები
        'აგრესია', 'ოპტიმიზმი', 'სიყვარული', 'მორჩილება', 'კრძალვა', 'გაკიცხვა', 'სინანული', 'ზიზღი', 'ნეიტრალური'
    ]

    similar_list_en = [  # Primary Emotions - similar words
                    'Overwhelmed, Furious', 'Mad, Fierce', 'Frustrated, Prickly',
                    'Intense, Focused', 'Curious, Considering', 'Open, Looking',
                    'Delighted, Giddy', 'Excited, Pleased', 'Calm, Peaceful',
                    'Connected, Proud', 'Accepting, Safe', 'Open, Welcoming',
                    'Alarmed, Petrified', 'Stressed, Scared', 'Worried, Anxious',
                    'Inspired, Astonished', 'Shocked, Unexpected', 'Scattered, Uncertain',
                    'Heartbroken, Distraught', 'Bummed, Loss', 'Blue, Unhappy',
                    'Disturbed, Horrified', 'Distrust, Rejecting', 'Tired, Uninterested',
                    # Secondary Emotions
                    'Hostile, Belligerent', 'Hopeful, Cheerful',
                    'Intimate, Passionate', 'Obedient, Compliant',
                    'Amazed, Astonished', 'Dissatisfied, Criticizing',
                    'Sorry, Regretful', 'Disrespectful, Mocking'
                    'Indistinct, Unemotional'
                  ]

    similar_list_ka = [  # ძირითადი ემოციები - მსგავსი სიტყვები
                    'მძვინვარე, გააფთრებული', 'ბოღმიანი, გაცოფებული', 'შეწუხებული, აღელვებული',
                    'ფოკუსირებული, ცოცხალი', 'ცნობისმოყვარე, მისწრაფების მქონე', 'გახსნილი, დაკვირვებული',
                    'აღტაცებული, აღფრთოვანებული', 'აგზნებული, კმაყოფილი', 'წყნარი, მშვიდი',
                    'მოხიბლული, გახარებული', 'დამჯერი, უსაფრთხოდ მყოფი', 'გახსნილი, გულღია',
                    'შეძრწუნებული, აღშფოთებული', 'დაძაბული, ანერვიულებული', 'შეშფოთებული, ფრთხილი',
                    'გაოცებული, გაოგნებული', 'გაკვირვებული, შეცბუნებული', 'დაბნებული, მოდუნებული',
                    'გულგატეხილი, თავგზააბნეული', 'შეწუხებული, უბედური', 'ცხვირჩამოშვებული, დარდიანი',
                    'აფორიაქებული, გაგულისებული', 'უნდობელი, უარმყოფი', 'დაღლილი, დაუინტერესებელი',
                    # დამატებითი ემოციები
                    'მტრული, ბოროტი', 'იმედიანი, მხნე',
                    'კეთილგანწყობილი, ვნებიანი', 'დამჯერი, შემგუებელი',
                    'განცვიფრებული, მოწიწებული', 'უკმაყოფილო, მაკრიტიკებელი',
                    'დანაღვლიანებული, სიბრალულის გრძნობის მქონე', 'უპატივცემლობა, დაცინვა',
                    'გაურკვეველი, უემოციო'
                  ]

    definition_list_en = [  # Primary Emotions - meaning
                    "I'm blocked from something vital", "Something is in the way", "Something is unresolved",
                    "Something big is coming", "Change is happening", "Something useful might come",
                    "This is better than I imagined", "Life is going well", "Something is happening that's essential, pure, or purposeful",
                    "I want to support the person or thing", "This is safe", "We are in this together",
                    "There is big danger", "Something I care about is at risk", "There could be a problem",
                    "Something is totally unexpected", "Something new happened", "I don't know what to prioritize",
                    "Love is lost", "Love is going away", "Love is distant",
                    "Fundamental values are violated", "Something is wrong and violates rules", "The potential for this situation isn't being met",
                    # Secondary Emotions
                    'Something hurtful or insulting happened', "I feel like something good is coming",
                    "I want this person to be happy", 'I have to rely on outside factors',
                    'An unexpected and impactful event occurred', 'This is unacceptable',
                    "I shouldn't have done it", 'This is beneath me',
                    "This didn't impact me in any way"
    ]

    definition_list_ka = [  # ძირითადი ემოციები - განმარტება
                    "საციცოცხლოდ მნიშვნელოვან საკითხში ხელი მეშლება", "რაღაც წინააღმდეგობას მიწევს", "რაღაც პრობლემა უნდა გადავწყვიტო",
                    "ძალიან მნიშვნელოვან მოვლენას ველოდები", "გარკვეული ცვლილება უნდა მოხდეს", "შეიძლება რაიმე მნიშვნელოვანი მოხდეს",
                    "ყველაფერი მოულოდნელად პოზიტიურად განვითარდა", "ცხოვრება მშვენივრად მიდის", "მოცემული მოვლენები მოსალოდნელი და მიზანშეწონილია",
                    "ამას სრულიად ვუჭერ მხარს", "ეს სრულიად უსაფრთხოა", "ეს სიტუაცია მაწყობს და ჩვეულებრივ ვეგუები",
                    "დიდი საფრთხის წინაშე ვიმყოფები", "ჩემთვის მნიშვნელოვანი რაღაც ან ვიღაც საფრთხის ქვეშაა", "შეიძლება გარკვეული პრობლემა გამიჩნდეს",
                    "სრულიად მოულოდნელი რაღაც შემემთხვა", "რაღაც ახალი განვიცადე", "არ ვიცი რას მივაქციო ყურადღება",
                    "სიყვარული დავრკარგე", "სიყვარულს ვკარგავ", "სიყვარულის შეგრძნება იკლებს",
                    "ჩემი მთავარი ღირებულებები შეურაცხყოფილია", "რაღაც არასწორი და დაუშვებელი ხდება", "ამ სიტუაციის სრული პოტენციალი არ რეალიზდება",
                    # დამატებითი ემოციები
                    'ამ მოვლენამ ზიანი ან შეურაცხყოფა მომაყენა', 'მგონია რომ რაღაც კარგი მოხდება',
                    "ამ ადამიანის გაბედნიერება მინდა", 'მიწევს გარე ფაქტორებს მივენდო',
                    'რაღაც განმაცვიფრებელი მოხდა', 'ეს სრულიად მიუღებელია',
                    "ეს არ უნდა მექნა", 'მე ამაზე მაღლა ვდგავარ',
                    "ამან ჩემზე გავლენა არ იქონია"
                  ]

    for emotion_en, similar_en, definition_en, emotion_ka, similar_ka, definition_ka in \
            zip(emotions_list_en, similar_list_en, definition_list_en, emotions_list_ka, similar_list_ka, definition_list_ka):

        db.session.add(Emotion(name_en=emotion_en,
                               similar_en=similar_en,
                               definition_en=definition_en,
                               name_ka=emotion_ka,
                               similar_ka=similar_ka,
                               definition_ka=definition_ka))


def populate_texts():
    for i in range(4000):
        db.session.add(Text(text=gen.sentence(), file=randrange(1, 6)))