import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col=('date'))

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,8))
    ax.plot(df.index, df["value"], 'r', linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", size=16)
    ax.set_xlabel("Date", size=16)
    ax.set_ylabel("Page Views", size=16)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():    
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(10, 8), legend=True, xlabel="Years", ylabel="Average Page Views").figure
    plt.legend([
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ], title="Months", fontsize=11.5)

    # This block of commented out code(lines 45 - 50) also works, but not with respect to the included test cases. Use Jupyter notebook 
    # or any other IDE to visualize the bar plot.

    #fig = df_bar.plot.bar(figsize=(10, 8), legend=True).figure
    #plt.legend(["January", "February","March","April","May","June","July","August","September","October","November","December"],
                #title="Months", fontsize=11.5)
    #plt.xlabel("Years", size=12)
    #plt.ylabel("Average Page Views", size=12)
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes= plt.subplots(nrows=1, ncols=2, figsize=(15,8))
    axes[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=axes[0])
    axes[1] = sns.boxplot(x=df_box["month"], y=df_box["value"],order=["Jan","Feb","Mar","Apr","May","Jun",
                                                                  "Jul","Aug","Sep","Oct","Nov","Dec"], ax=axes[1])

    axes[0].axes.set_title("Year-wise Box Plot (Trend)", size=12)
    axes[0].set_xlabel("Year", size=12)
    axes[0].set_ylabel("Page Views", size=12)

    axes[1].axes.set_title("Month-wise Box Plot (Seasonality)", size=12)
    axes[1].set_xlabel("Month", size=12)
    axes[1].set_ylabel("Page Views", size=12)

    ## This block of commented out code (lines 79 - 92) also works, but not with respect to the included test cases.
    # Use Jupyter notebook or any other IDE to visualize the bar plot.This works when plotting the boxplots individually.
    #fig, ax = plt.subplots(figsize=(20,8))
    #boxplot = sns.boxplot(y=df_box["value"], x=df_box["year"])
    #boxplot.axes.set_title("Year-wise Box Plot (Trend)", size=12)
    #boxplot.set_xlabel("Year", size=12)
    #boxplot.set_ylabel("Page Views", size=12)
    #plt.show()

    #fig, ax = plt.subplots(figsize=(20,8))
    #boxplot = sns.boxplot(y=df_box["value"], x=df_box["month"], order=["Jan","Feb","Mar","Apr","May","Jun",
                                                                  # "Jul","Aug","Sep","Oct","Nov","Dec"],)
    #boxplot.axes.set_title("Year-wise Box Plot (Trend)", size=12)
    #boxplot.set_xlabel("Year", size=12)
    #boxplot.set_ylabel("Page Views", size=12)
    #plt.show()    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
