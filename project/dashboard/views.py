from flask import render_template
from .generate_charts import generate_charts
from . import dashboard_blueprint


# TODO: @login_required
@dashboard_blueprint.route('/', methods=['GET'])
def dashboard():
    ChartMonth, ChartWeek = generate_charts()
    MonthChart = ChartMonth()
    month_chart = MonthChart.get()

    WeekChart = ChartWeek()
    week_chart = WeekChart.get()

    return render_template('dashboard.html', week_chart=week_chart, month_chart=month_chart)
