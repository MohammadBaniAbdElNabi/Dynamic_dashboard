import streamlit as st
import pandas as pd
import numpy as np
import time

# Google Sheets Link
SHEET_ID = "121CChNjuIxlQjVaQFFOjxkAvuMMpLHSE"
SHEET_NAME = "Sheet1"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/121CChNjuIxlQjVaQFFOjxkAvuMMpLHSE/gviz/tq?tqx=out:csv&sheet=Sheet1"

# Function to fetch live data
@st.cache_data(ttl=30)  # Refreshes every 30 sec
def fetch_data():
    df = pd.read_csv(SHEET_URL)
    return df

# Function to run Monte Carlo simulations
def run_simulations(data, num_simulations):
    results = []
    for _ in range(num_simulations):
        sample = data.sample(frac=1, replace=True)  # Bootstrap resampling
        results.append(sample.iloc[:, 2].mean())  # Using 3rd column (Temperature °C)
    return results

# Streamlit UI
st.title("📊 Real-Time Monte Carlo Simulation Dashboard")

# Load Data
df = fetch_data()

if df.empty:
    st.error("❌ No data found! Check your Google Sheets connection.")
else:
    st.success("✅ Data Loaded Successfully!")

    # Show editable data table
    st.subheader("📝 Edit Data Before Simulation")
    edited_df = st.data_editor(df, num_rows="dynamic")  # Allows in-app editing

    # Ensure correct column names
    if "Timestamp" not in edited_df.columns or "Temperature (°C)" not in edited_df.columns:
        st.error("❌ Required columns not found! Ensure 'Timestamp' & 'Temperature (°C)' exist.")
    else:
        # Convert Timestamp to datetime format
        edited_df["Timestamp"] = pd.to_datetime(edited_df["Timestamp"])

        # Sort data by time
        edited_df = edited_df.sort_values("Timestamp")

        # Draw Temperature vs. Time Plot
        st.subheader("📈 Temperature Trend Over Time")
        st.line_chart(edited_df.set_index("Timestamp")["Temperature (°C)"])

        # User can adjust the number of simulations
        st.subheader("🎛️ Choose Number of Simulations")
        num_simulations = st.slider("Number of Simulations", min_value=100, max_value=5000, value=len(edited_df), step=100)

        # Buttons for interaction
        col1, col2 = st.columns(2)
        run_simulation = col1.button("🚀 Run Simulation")
        reset_data = col2.button("🔄 Reset Data")

        if reset_data:
            st.cache_data.clear()  # Clears cached data
            st.experimental_set_query_params(refresh="true")  # Forces app refresh
            st.experimental_rerun()  # Workaround for auto-refresh

        if run_simulation:
            st.subheader(f"🎲 Running {num_simulations} Simulations")
            simulation_results = run_simulations(edited_df, num_simulations)

            # Show results
            st.line_chart(simulation_results)

            # Download Button
            predictions_df = pd.DataFrame(simulation_results, columns=["Predicted Temperature (°C)"])
            st.download_button(
                label="📥 Download Predictions",
                data=predictions_df.to_csv(index=False),
                file_name="monte_carlo_predictions.csv",
                mime="text/csv"
            )

        # Auto-refresh every 30 sec
        time.sleep(30)
