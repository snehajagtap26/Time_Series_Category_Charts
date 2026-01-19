import matplotlib.pyplot as plt

def plot_time_series(df, output_path):
    daily_sales = df.groupby('Date')['Sales'].sum()
    plt.figure()
    daily_sales.plot()
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
def plot_monthly_quarterly(df, monthly_path, quarterly_path):
    monthly = df.resample('ME', on='Date')['Sales'].sum()   
    quarterly = df.resample('QE', on='Date')['Sales'].sum() 

    monthly.plot(title='Monthly Sales')
    plt.tight_layout()
    plt.savefig(monthly_path)
    plt.close()
    quarterly.plot(title='Quarterly Sales')
    plt.tight_layout()
    plt.savefig(quarterly_path)
    plt.close()