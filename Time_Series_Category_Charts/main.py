from scripts.data_loader import load_data
from scripts.time_series_charts import plot_time_series, plot_monthly_quarterly
from scripts.category_charts import plot_category_charts
from scripts.summary import generate_summary
DATA_PATH = 'data/sales_data.csv'
CHART_PATH = 'outputs/charts/'
df = load_data(DATA_PATH)
plot_time_series(df, CHART_PATH + 'sales_over_time.png')
plot_monthly_quarterly(df,
CHART_PATH + 'monthly_sales.png',
CHART_PATH + 'quarterly_sales.png')
plot_category_charts(df,
CHART_PATH + 'category_bar.png',
CHART_PATH + 'category_pie.png')
generate_summary(df, 'outputs/summary.txt')