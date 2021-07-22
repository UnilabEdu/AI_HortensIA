console.log('Loaded TRANSLATIONS')


// var fetchCurrentLanguage = async function () {
//     console.log('started fetching')
//     var response = await fetch('/currentlang');
//     console.log('fetched')
//     return await response.json();
// };
//
// async function getCurrentLanguage() {
//     console.log('attempting fetch')
//     let lang = await fetchCurrentLanguage()
//     useLanguage(lang.language)
//     // if (window.location.pathname === '/dashboard/') {
//     //     runChartConfigs()
//     //     runChartScripts()
//     // }
//
// }

fetch('/currentlang')
  .then(response => response.json())
  .then(data => useLanguage(data.language));



// English to Georgian translations to texts set in JS are given below
// Example of the nesting structure: txt/Dashboard/Goal/Rank/Next

function useLanguage(lang) {
    lang_toggler = document.getElementById('lang-checkbox')
    console.log('started useLanguage')

    if (lang === 'en') {
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
                        tooltips: [],
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
                        tooltips: [],
                        default: {
                            info: 'Start submitting tickets to appear in the leaderboard',
                            targ: 'The amount of tickets to rank-up will be shown here'
                        },

                        calculated: {
                            info: 'Surpass the next user in the leaderboard:',
                            targ: ['Submit ', ' more tickets']
                        }
                    },
                    lvl: {
                        tooltips: [],
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
                        month: 'Tickets in the last 30 days',
                        week: 'Tickets in the last 7 days'
                    }

                },

                lead: {
                    global: {},
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
                        emotions: ['Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt']
                    }
                }

            }

        }
    }



    else if (lang === 'ka') {

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
                        tooltips: [],
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
                        tooltips: [],
                        default: {
                            info: 'აქ დაგითვლით ლიდერბორდში გადასასწრებად დარჩენილი ბარათების რაოდენობას',
                            targ: 'დაიწყეთ ბარათების შევსება'
                        },

                        calculated: {
                            info: 'გადაასწარით ლიდერბორდში შემდეგ მომხმარებელს',
                            targ: ['შეავსეთ კიდევ ', ' ბარათი.']
                        }
                    },
                    lvl: {
                        tooltips: [],
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
                        month: 'ბოლო 30 დღის სტატისტიკა',
                        week: 'ბოლო 7 დღის სტატისტიკა'
                    }

                },

                lead: {
                    global: {},
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
                        emotions: ['აგრესია', 'ოპტიმიზმი', 'სიყვარული', 'მორჩილება', 'აკრძალვა', 'გაკიცხვა', 'სინანული', 'ზიზღი']
                    }
                }

            }

        }
    }
    else {
        console.log('Error fetching language')
    }
    console.log(txt.dash.goal.streak.default.targ)
}


// getCurrentLanguage()
