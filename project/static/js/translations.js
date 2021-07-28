// translations.js is used to initialize a dictionary containing
// every string that would be needed in .js files and can't be imported from Flask-Babel
// the dictionary changes its language based on current language


if (current_lang === 'en') {

    lang_toggler = document.getElementById('lang-checkbox')
    lang_toggler.removeAttribute('checked')

    txt = {
    subscr: {
        zero: 'Please input your email address.',
        invalid: 'Please input a valid email address.',
        success: 'You have been subscribed successfully.',
        error: 'An error occurred. Please try again later.'
    },


    dash: {

        goal: {
            streak: {
                tooltips: ['Current streak', 'Next goal in'],
                default: {
                    curr: "You haven't submitted a ticket today",
                    targ: "An activity streak will be displayed here later"
                },
                calculated: {
                    active: {
                        curr: ["You are on a ", '-day streak.'],
                        targ: {
                            week: ['Your next goal: a ', '-week streak.'],
                            month: ['Your next goal: a ', '-month streak.'],
                            year: 'Your next goal: a full-year streak.',
                            end: 'We sincerely appreciate your commitment!!'
                        }
                    },
                    paused: {
                        curr: ['You were on a ', '-day streak.'],
                        targ: 'Submit a ticket today to continue your streak'
                    }
                }
            },
            rank: {
                tooltips: ['Tickets after last rank-up', 'Next rank in'],
                default: {
                    info: 'Start submitting tickets to appear in the leaderboard',
                    targ: 'The amount of tickets to rank-up will be shown here'
                },

                calculated: {
                    info: 'Surpass the next user in the leaderboard:',
                    targ: ['Submit ', ' more tickets']
                },

                top: {
                    info: 'You are at the top of the leaderboard',
                    targ: 'Good job!'
                }
            },
            lvl: {
                tooltips: ['Last 7 days total', 'Next level in'],
                curr: ["You've submitted ", " tickets in the last 7 days."],
                targ: [
                    ["Submit ", " more to advance to Level 1"],
                    ["Submit ", " more to advance to Level 2"],
                    ["Submit ", " more to advance to Level 3"],
                    "You've reached Level 3. Thank you!"
                ]
            }
        },

        act: {
            heatmap: {
                date: 'Date',
                amount: 'Amount:'
            },
            line: {
                month: 'Tickets filled',
                week: 'Tickets filled'
            }

        },

        lead: {
            global: {
                hover: 'Tickets filled'
            },
            levels: {
                one: ['The table is empty right now', 'Submit 35 tickets in the last 7 days to appear here'],
                two: ['The table is empty right now', 'Submit 70 tickets in the last 7 days to appear here'],
                three: ['The table is empty right now', 'Submit 105 tickets in the last 7 days to appear here']
            },
            streaks: {
                title: 'Activity Streaks'
            }
        },

        radar: {
            labels: {
                my: 'My data',
                all: "Everyone's data"
            },
            primary: {
                emotions: ["Rage", "Vigilance", "Ecstasy", "Admiration", "Terror", "Amazement", "Grief", "Loathing"]
            },
            secondary: {
                emotions: ['Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse',
                             'Contempt']
            }
        }

    },


    ticket: {
        nomore: 'There are no tickets left for you to submit. Please come back later.  ',
        about: ['What is ', ' telling you:'],
        reset: {
            title: 'Choose an Emotion',
            synonym: 'Similar emotions or synonyms of the chosen emotion',
            about: 'The definition of the chosen emotion',
            about_question: 'What is this emotion telling you?',
        },
        submit: 'Ticket submitted (Emotion: ',
        error: 'An error occurred'
    }
}
}



else if (current_lang === 'ka') {

    txt = {
            subscr: {
                zero: "გთხოვთ შეიყვანოთ ელ-ფოსტის მისამართი.",
                invalid: "გთხოვთ სწორად შეიყვანოთ ელ-ფოსტის მისამართი.",
                success: "ელ-ფოსტის მისამართი მიღებულია.",
                error: "დაფიქსირდა შეცდომა. თავიდან სცადეთ."
            },


            dash: {

                goal: {
                    streak: {
                        tooltips: ['აქტიურობის დღეები', 'შემდეგ მიზნამდე'],
                        default: {
                            curr: 'დღეს ბარათი არ შეგივსიათ.',
                            targ: 'აქ დაგითვლით, ზედიზედ რამდენი დღე იაქტიურეთ.'
                        },
                        calculated: {
                            active: {
                                curr: ['ზედიზედ ', ' დღე აქტიურობთ.'],
                                targ: {
                                    week: ['შემდეგი მიზანი: ', ' კვირა.'],
                                    month: ['შემდეგი მიზანი: ', ' თვე.'],
                                    year: 'შემდეგი მიზანი: 1 წელი.',
                                    end: 'დიდი მადლობა!'
                                }
                            },
                            paused: {
                                curr: ['ზედიზედ ', ' დღე აქტიურობდით.'],
                                targ: 'შეავსეთ ბარათი დღესაც, რათა გააგრძელოთ აქტიურობის მიმდევრობა'
                            }
                        }
                    },
                    rank: {
                        tooltips: ['სხვაობა წინა რეიტინგთან', 'გადასასწრებად დარჩა'],
                        default: {
                            info: 'აქ დაგითვლით ლიდერბორდში გადასასწრებად დარჩენილი ბარათების რაოდენობას',
                            targ: 'დაიწყეთ ბარათების შევსება'
                        },

                        calculated: {
                            info: 'გადაასწარით ლიდერბორდში შემდეგ მომხმარებელს',
                            targ: ['შეავსეთ კიდევ ', ' ბარათი.']
                        },

                        top: {
                            info: 'შევსებული ბარათების რაოდენობით პირველ ადგილზე ხართ',
                            targ: 'ყოჩაღ!'
                        }
                    },
                    lvl: {
                        tooltips: ['ბოლო 7 დღის ბარათები', 'შემდეგ მიზნამდე'],
                        curr: ["ბოლო 7 დღეში შეავსეთ ", " ბარათი."],
                        targ: [
                            ["პირველ დონეზე გადასასვლელად შეავსეთ კიდევ ", " ბარათი"],
                            ["მეორე დონეზე გადასასვლელად შეავსეთ კიდევ ", " ბარათი"],
                            ["მესამე დონეზე გადასასვლელად შეავსეთ კიდევ ", " ბარათი"],
                            "მესამე დონის კონტრიბუტორი ბრძანდებით. დიდი მადლობა!"
                        ]
                    }
                },

                act: {
                    heatmap: {
                        date: 'თარიღი',
                        amount: 'რაოდენობა'
                    },
                    line: {
                        month: 'შევსებული ბარათები',
                        week: 'შევსებული ბარათები'
                    }

                },

                lead: {
                    global: {
                        hover: 'შევსებული ბარათები'
                    },
                    levels: {
                        one: ['ცხრილი ამჟამად ცარიელია', 'აქ მოსახვედრად, ბოლო 7 დღეში შევსებული უნდა გქონდეთ 35 ბარათი'],
                        two: ['ცხრილი ამჟამად ცარიელია', 'აქ მოსახვედრად, ბოლო 7 დღეში შევსებული უნდა გქონდეთ 70 ბარათი'],
                        three: ['ცხრილი ამჟამად ცარიელია', 'აქ მოსახვედრად, ბოლო 7 დღეში შევსებული უნდა გქონდეთ 105 ბარათი']
                    },
                    streaks: {
                        title: 'აქტივობის მიმდევრობები'
                    }
                },

                radar: {
                    labels: {
                        my: 'ჩემი მონაცემები',
                        all: 'ყველა მონაცემი'
                    },
                    primary: {
                        emotions: ["რისხვა", "სიფხიზლე", "აღტყინება", "აღტაცება", "თავზარდამცემი შიში", "აღფრთოვანება", "მწუხარება", "სიძულვილი"]
                    },
                    secondary: {
                        emotions: ['აგრესია', 'ოპტიმიზმი', 'სიყვარული', 'მორჩილება', 'კრძალვა', 'გაკიცხვა', 'სინანული', 'ზიზღი']
                    }
                }

            },


            ticket: {
                nomore: 'თქვენ ამოწურეთ მარკირებისთვის განკუთვნილი წინადადებების საცავი. ახალი წინადადებები მოგვიანებით დაემატება. ',
                about: ["რას გვეუბნება ", ':'],
                reset: {
                    title: 'აირჩიეთ ემოცია',
                    synonym: 'არჩეული ემოციის სინონიმები ან მსგავსი ემოციები',
                    about: 'არჩეული ემოციის განმარტება',
                    about_question: 'რას გვეუბნება ეს ემოცია?',
                },
                submit: 'მონამეცები მიღებულია (ემოცია: ',
                error: 'დაფიქსირდა შეცდომა'
            }
        }
}
