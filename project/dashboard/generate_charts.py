from pychartjs import BaseChart, ChartType, Color
from project.dashboard.data_processing import data_user_line, leaderboard, data_radar


def generate_charts():
    frequencies_line, dates_month, heatmap_data = data_user_line()
    usernames, frequencies_leaderboard, placements, colors = leaderboard()

    purple_gradient = Color.JSLinearGradient('ctx', 0, 0, 600, 0,
                                             (0, Color.RGBA(127, 92, 194, 1)),
                                             (1, Color.RGBA(127, 92, 194, 0.55))
                                             ).returnGradient()

    class ChartMonth(BaseChart):
        type = ChartType.Line

        class data:
            label = "Tickets Filed Last 30 Days"
            data = frequencies_line
            borderColor = Color.Hex("#5D4191")
            borderWidth = 2
            backgroundColor = Color.RGBA(127, 92, 194, 1)
            tension = 0.4
            fill = True

        class labels:
            group = [str(date) for date in dates_month]

        class options:
            elements = {
                'point':
                    {
                        'radius': 0,
                        'hitRadius': 25
                    }
            }

            scales = {
                "y": dict(
                    beginAtZero=True,
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                ),
                "x": dict(
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                )
            }

    class ChartWeek(BaseChart):
        type = ChartType.Line

        class data:
            label = "Tickets Filed Last 7 Days"
            data = frequencies_line[-7:]
            borderColor = Color.Hex("#5D4191")
            borderWidth = 2
            backgroundColor = Color.RGBA(127, 92, 194, 1)
            tension = 0.4
            fill = True

        class labels:
            group = [str(date) for date in dates_month[-7:]]

        class options:
            elements = {
                'point':
                    {
                        'radius': 0,
                        'hitRadius': 50
                    }
            }

            scales = {
                "y": dict(
                    beginAtZero=True,
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                ),
                "x": dict(
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                )
            }

    class ChartLeaderboard(BaseChart):
        type = ChartType.Bar

        class data:
            label = "Leaderboard"
            data = frequencies_leaderboard
            backgroundColor = colors
            barThickness = 'flex',
            barPercentage = 1,
            categoryPercentage = 1,
            # borderRadius = 10

        class labels:
            group = usernames

        class options:
            indexAxis = 'y'

            scales = {
                "y": dict(
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                ),
                "x": dict(
                    grid=dict(
                        display=False,
                        drawBorder=False,
                        tickMarkLength=0
                    )
                )
            }

    # class ChartRadar(BaseChart):
    #     type = ChartType.Radar
    #
    #     class labels:
    #         Labels = [
    #             'Rage',
    #             'Vigilance',
    #             'Ecstasy',
    #             'Admiration',
    #             'Terror',
    #             'Amazement',
    #             'Grief',
    #             'Loathing'
    #         ]
    #
    #     class data:
    #         class FirstDataset:
    #             label = 'My Data'
    #             data = user_frequencies
    #             fill = True
    #             backgroundColor = Color.RGBA(255, 99, 132, 0.2)
    #             borderColor = Color.RGBA(255, 99, 132)
    #             pointBackgroundColor = Color.RGBA(255, 99, 132)
    #             pointBorderColor = Color.RGBA(255, 255, 255, 1)
    #             pointHoverBackgroundColor = Color.RGBA(255, 255, 255, 1)
    #             pointHoverBorderColor = Color.RGBA(255, 99, 132)
    #             tension = 0.1
    #
    #
    #         class SecondDataset:
    #             label = 'All Data'
    #             data = all_frequencies
    #             fill = True
    #             backgroundColor = Color.RGBA(54, 162, 235, 0.2)
    #             borderColor = Color.RGBA(54, 162, 235)
    #             pointBackgroundColor = Color.RGBA(54, 162, 235)
    #             pointBorderColor = Color.RGBA(255, 255, 255, 1)
    #             pointHoverBackgroundColor = Color.RGBA(255, 255, 255, 1)
    #             pointHoverBorderColor = Color.RGBA(54, 162, 235)
    #             tension = 0.1
    #
    #     class options:
    #         scales = {
    #             "r": dict(
    #                 beginAtZero=True,
    #             )
    #         }

    return ChartMonth, ChartWeek, ChartLeaderboard, heatmap_data


def generate_radars():
    primary, secondary = data_radar()
    everyone_anytime_primary, everyone_month_primary, everyone_week_primary, everyone_day_primary = primary[0:4]
    user_anytime_primary, user_month_primary, user_week_primary, user_day_primary = primary[4:9]

    everyone_anytime_secondary, everyone_month_secondary, everyone_week_secondary, everyone_day_secondary = secondary[0:4]
    user_anytime_secondary, user_month_secondary, user_week_secondary, user_day_secondary = secondary[4:9]

    def generate_one_radar(first_dataset_frequencies, second_dataset_frequencies, secondary_labels=False):
        if not secondary_labels:
            emotion_labels = [
                    'Rage',
                    'Vigilance',
                    'Ecstasy',
                    'Admiration',
                    'Terror',
                    'Amazement',
                    'Grief',
                    'Loathing'
                ]
        else:
            emotion_labels = [
                'Aggressiveness',
                'Optimism',
                'Love',
                'Submission',
                'Awe',
                'Disapproval',
                'Remorse',
                'Contempt'
            ]

        class ChartRadar(BaseChart):
            type = ChartType.Radar

            class labels:
                Labels = emotion_labels

            class data:
                class FirstDataset:
                    label = 'My Data'
                    data = first_dataset_frequencies
                    fill = True
                    backgroundColor = Color.RGBA(255, 99, 132, 0.2)
                    borderColor = Color.RGBA(255, 99, 132)
                    pointBackgroundColor = Color.RGBA(255, 99, 132)
                    pointBorderColor = Color.RGBA(255, 255, 255, 1)
                    pointHoverBackgroundColor = Color.RGBA(255, 255, 255, 1)
                    pointHoverBorderColor = Color.RGBA(255, 99, 132)
                    tension = 0.1

                class SecondDataset:
                    label = 'All Data'
                    data = second_dataset_frequencies
                    fill = True
                    backgroundColor = Color.RGBA(54, 162, 235, 0.2)
                    borderColor = Color.RGBA(54, 162, 235)
                    pointBackgroundColor = Color.RGBA(54, 162, 235)
                    pointBorderColor = Color.RGBA(255, 255, 255, 1)
                    pointHoverBackgroundColor = Color.RGBA(255, 255, 255, 1)
                    pointHoverBorderColor = Color.RGBA(54, 162, 235)
                    tension = 0.1

            class options:
                scales = {
                    "r": dict(
                        beginAtZero=True,
                    )
                }

        return ChartRadar

    primary_anytime = generate_one_radar(user_anytime_primary, everyone_anytime_primary)
    secondary_anytime = generate_one_radar(user_anytime_secondary, everyone_anytime_secondary, secondary_labels=True)

    primary_month = generate_one_radar(user_month_primary, everyone_month_primary)
    secondary_month = generate_one_radar(user_month_secondary, everyone_month_secondary, secondary_labels=True)

    primary_week = generate_one_radar(user_week_primary, everyone_week_primary)
    secondary_week = generate_one_radar(user_week_secondary, everyone_week_secondary, secondary_labels=True)

    primary_day = generate_one_radar(user_day_primary, everyone_day_primary)
    secondary_day = generate_one_radar(user_day_secondary, everyone_day_secondary, secondary_labels=True)

    return primary_anytime, secondary_anytime, primary_month, secondary_month, \
           primary_week, secondary_week, primary_day, secondary_day
