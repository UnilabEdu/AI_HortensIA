from pychartjs import BaseChart, ChartType, Color
from project.dashboard.data_processing import data_user_line, leaderboard, data_radar


def generate_charts():
    frequencies_line, dates_month, heatmap_data = data_user_line()
    usernames, frequencies_leaderboard, placements, colors = leaderboard()
    user_frequencies, all_frequencies = data_radar()

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
            backgroundColor = purple_gradient
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
            backgroundColor = purple_gradient
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

    class ChartRadar(BaseChart):
        type = ChartType.Radar

        class labels:
            Labels = [
                'Rage',
                'Vigilance',
                'Ecstasy',
                'Admiration',
                'Terror',
                'Amazement',
                'Grief',
                'Loathing'
            ]

        class data:
            class FirstDataset:
                label = 'My Data'
                data = user_frequencies[:8]
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
                data = all_frequencies[:8]
                fill = True
                backgroundColor = Color.RGBA(54, 162, 235, 0.2)
                borderColor = Color.RGBA(54, 162, 235)
                pointBackgroundColor = Color.RGBA(54, 162, 235)
                pointBorderColor = Color.RGBA(255, 255, 255, 1)
                pointHoverBackgroundColor = Color.RGBA(255, 255, 255, 1)
                pointHoverBorderColor = Color.RGBA(54, 162, 235)
                tension = 0.1

    return ChartMonth, ChartWeek, ChartLeaderboard, ChartRadar, heatmap_data
