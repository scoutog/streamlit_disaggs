import streamlit as st
import pandas as pd
import plotly.express as px

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'CHANNEL': ['DIGITAL', 'VALUE', 'PARTNERS', 'DIGITAL', 'VALUE', 'PARTNERS'],
    'BRAND': ['BRANDA', 'BRANDA', 'BRANDA', 'BRANDB', 'BRANDB', 'BRANDB'],
    'Percentage': [0.5, 0.3, 0.2, 0.2, 0.3,0.5]
}

df = pd.DataFrame(data)

def main():
    st.title("Disaggregation Methodology")

    # Display the initial level breakdown
    display_level_breakdown(df, 'CHANNEL')

def display_level_breakdown(dataframe, level):
    st.header(f"{level} Breakdown")

    # Filter DataFrame based on the selected level
    filtered_df = dataframe.groupby(level).sum().reset_index()

    # Display buttons for each unique value with its associated percentage
    for index, row in filtered_df.iterrows():
        button_label = f"{row[level]}: {row['Percentage']:.2%}"
        if st.button(button_label):
            # Allow the user to click into the next level
            next_level_df = dataframe[dataframe[level] == row[level]]
            display_level_breakdown(next_level_df, 'BRAND')

if __name__ == "__main__":
    main()
