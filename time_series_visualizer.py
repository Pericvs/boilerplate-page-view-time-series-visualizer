import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
px = 1/plt.rcParams['figure.dpi'] 
# Clean data
df = df[(df['value']<df['value'].quantile(0.975)) & (df['value']>df['value'].quantile(0.025))]
df.index=pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    df_line=df.copy()
    fig = plt.figure(figsize=(3200*px, 1000*px))
    plt.plot(df_line.index,df_line.value,color='r',linewidth=2.0)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #plt.rc('font', size=22)
    #df.plot(figsize=(3200*px, 1000*px),title='Date freeCodeCamp Forum Page Views 5/2016-12/2019',xlabel='Date', ylabel='Page Views', ax=ax1, color='r')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    # Calculate the mean value for each month and year
    #df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    #df_bar=df_bar.unstack()
    #df_bar.columns=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Create a bar plot using Seaborn
    fig = sns.catplot(data=df_bar, kind='bar', x='Year', y='value', hue='Month',hue_order=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ], legend=False, palette='nipy_spectral', errorbar=None)  
    # Adjust the figure size as needed
    #df_bar.plot(kind='bar', ax=ax1)
    
    # Customize the plot
    plt.xlabel('Years')
    plt.xticks(rotation=90)
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]

    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    fig, [ax1,ax2] = plt.subplots(1,2,figsize=(20,6))
    sns.boxplot(data=df_box, ax=ax1, x='year', y='value', hue='year', legend=False, palette='tab20')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, ax=ax2, x='month', y='value',hue='month', order=order, legend=False, palette='tab20')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
