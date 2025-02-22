import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Data Visualization App")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Preview of the dataset:")
        st.write(df.head())
        
        # Select visualization type
        visualization = st.selectbox("Select Visualization Type", ["Histogram", "Scatter Plot", "Correlation Heatmap", "Pie Chart", "Column Chart"])
        
        if visualization == "Histogram":
            column = st.selectbox("Select Column for Histogram", df.columns)
            fig, ax = plt.subplots()
            sns.histplot(df[column], kde=True, ax=ax)
            st.pyplot(fig)
        
        elif visualization == "Scatter Plot":
            col1, col2 = st.selectbox("Select X-axis", df.columns), st.selectbox("Select Y-axis", df.columns)
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
            st.pyplot(fig)
        
        elif visualization == "Correlation Heatmap":
            fig, ax = plt.subplots()
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        
        elif visualization == "Pie Chart":
            column = st.selectbox("Select Column for Pie Chart (Categorical)", df.columns)
            pie_data = df[column].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
            ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        
        elif visualization == "Column Chart":
            column = st.selectbox("Select Column for Column Chart (Categorical)", df.columns)
            column_data = df[column].value_counts()
            fig, ax = plt.subplots()
            sns.barplot(x=column_data.index, y=column_data.values, ax=ax, palette="viridis")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
            st.pyplot(fig)
    
if __name__ == "__main__":
    main()
