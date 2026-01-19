def generate_summary(df, output_file):
    total_sales = df['Sales'].sum()
    top_category = df.groupby('Category')['Sales'].sum().idxmax()
    with open(output_file, 'w') as f:
        f.write(f"Total Sales: {total_sales}\n")
        f.write(f"Top Performing Category: {top_category}\n")
        
        f.write("Chart Justification:\n")
        f.write("- Line charts are used to visualize sales trends over time.\n")
        f.write("- Bar charts compare total sales across categories clearly.\n")
        f.write("- Pie charts show proportional sales contribution by category.\n")