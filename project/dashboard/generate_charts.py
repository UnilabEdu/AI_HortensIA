from pychartjs import BaseChart, ChartType, Color
from project.dashboard.data_processing import data_user_line


def generate_charts():
    frequencies, month_labels = data_user_line()

    purple_gradient = Color.JSLinearGradient('ctx', 0, 0, 600, 0,
                                             (0, Color.RGBA(93, 65, 145, 0.9)),
                                             (1, Color.RGBA(93, 65, 145, 0.5))
                                             ).returnGradient()

    class ChartMonth(BaseChart):
        type = ChartType.Line

        class data:
            label = "Tickets Filed Last 30 Days"
            data = frequencies
            borderColor = Color.Hex("#5D4191")
            borderWidth = 2
            backgroundColor = purple_gradient
            tension = 0.4
            fill = True

        class labels:
            group = [str(date) for date in month_labels]

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
            data = frequencies[-7:]
            borderColor = Color.Hex("#5D4191")
            borderWidth = 2
            backgroundColor = purple_gradient
            tension = 0.4
            fill = True

        class labels:
            group = [str(date) for date in month_labels[-7:]]

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

    return ChartMonth, ChartWeek
