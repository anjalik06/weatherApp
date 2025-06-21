
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import io
import streamlit as st

def plot_temperature_chart(df):
    df['time'] = pd.to_datetime(df['time'])

   
    sns.set_theme(style="darkgrid")

    
    plt.figure(figsize=(10, 5))
    ax = sns.lineplot(data=df, x='time', y='temperature', marker='o', color='deepskyblue')
    ax.set_title('Hourly Temperature Forecast')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temp (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    st.image(buf)
    
def plot_humidity_chart(df):
    df['time'] = pd.to_datetime(df['time'])

   
    sns.set_theme(style="darkgrid")

    
    plt.figure(figsize=(10, 5))
    ax = sns.lineplot(data=df, x='time', y='humidity', marker='o', color='deepskyblue')
    ax.set_title(' Hourly Humidity Chart')
    ax.set_xlabel('Time')
    ax.set_ylabel('Humidity')
    plt.xticks(rotation=45)
    plt.tight_layout()

    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    st.image(buf)