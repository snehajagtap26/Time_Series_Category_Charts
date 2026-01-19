import matplotlib.pyplot as plt

def plot_category_charts(df, bar_path, pie_path):
    category_sales = df.groupby('Category')['Sales'].sum()
# Bar Chart
    category_sales.plot(kind='bar', title='Sales by Category')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close()
# Pie Chart
    category_sales.plot(kind='pie', autopct='%1.1f%%', title='Category Share')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(pie_path)
    plt.close()
