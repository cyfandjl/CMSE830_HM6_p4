#midterm_project
import streamlit as st #create a web app
import numpy as np
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt
import hiplot as hip
import plotly.express as px #visualize library
import altair as alt


#upload datasets
aoti = pd.read_csv('PRSA_Data_Aotizhongxin_20160101-20161231.csv')


st.write("""
    ## Beijing Air-Quality Data from Aotizhongxin in 2016

    """)

#Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(aoti.isna().transpose(), cmap="magma")
plt.title("The distribution of NaN")
st.pyplot(plt)


# User selection
st.sidebar.header("User input choice")
columns = aoti.columns.tolist()
x_axis = st.sidebar.selectbox("Select X variable:", columns)
y_axis = st.sidebar.selectbox("Select Y variable:", columns)
selected_plots = st.sidebar.multiselect("Select plots to display", 
                                            ["regplot", "violinplot", "histplot"],
                                            default=["regplot"])

if "regplot" in selected_plots:
    st.write("""
    ## Regplot

    """)
    if aoti[x_axis].dtype != 'object' and aoti[y_axis].dtype != 'object':
        plt.figure(figsize=(8, 6))
        sns.regplot(data=aoti, x=x_axis, y=y_axis)
        st.pyplot(plt)
    else:
        st.write("""
        #### *This column is not numerical.*

        """)


if "violinplot" in selected_plots:
    st.write("""
    ## Violinplot

    """)
    if aoti[x_axis].dtype != 'object' and aoti[y_axis].dtype != 'object':
        plt.figure(figsize=(8, 6))
        sns.violinplot(data=aoti, x=x_axis, y=y_axis, palette="Set3", bw=2, cut=2, linewidth=5)
        st.pyplot(plt)
    else:
        st.write("""
        #### *This column is not numerical.*

        """)


if "histplot" in selected_plots:
    st.write("""
    ## Histplot

    """)
    if aoti[x_axis].dtype != 'object':
        sns.set_context("talk")
        plt.figure(figsize=(8, 6))
        plt.hist(aoti[x_axis], bins=30)
        plt.axvline(x=np.mean(aoti[x_axis]), linewidth=2, color='g',label = "Mean")
        plt.axvline(x=np.median(aoti[x_axis]), linewidth=2, color='r',linestyle='--', label = "Median")
        plt.xlabel(f" {x_axis} ")
        plt.ylabel("count")
        plt.legend(loc=0)
        st.pyplot(plt)

    else:
        st.write("""
        #### *This column is not numerical.*

        """)






