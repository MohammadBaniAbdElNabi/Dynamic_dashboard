# Real-Time Monte Carlo Simulation Dashboard

This project leverages Monte Carlo simulations to predict temperature variations using real-time data fetched directly from Google Sheets. Built with **Streamlit**, **Pandas**, and **NumPy**, the app offers an interactive dashboard for visualizing the data, running simulations, and downloading the results.

## Features

- **Live Data Integration**: Fetch temperature data in real-time from Google Sheets.
- **Monte Carlo Simulations**: Run Monte Carlo simulations to predict future temperature values based on historical data.
- **Interactive Dashboard**: 
  - View and edit the temperature data.
  - Adjust the number of simulations for more precise predictions.
  - Visualize predicted temperature trends.
  - Download simulation results in CSV format.
- **Auto-Refresh**: The app auto-refreshes every 30 seconds to keep data up to date.

## Requirements

To run this project locally or in GitHub Codespaces, ensure the following dependencies are installed:

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Gspread
- OAuth2client

You can use the provided `requirements.txt` to install all the necessary libraries.

## Installation Instructions

Follow the steps below to set up the project either on your local machine or in GitHub Codespaces.

### Option 1: Running in GitHub Codespaces

1. **Clone the Repository**:
   - Navigate to the repository on GitHub.
   - Click on **"Open with Codespaces"** to create a new Codespace instance.

2. **Build the Environment**:
   - Codespaces will automatically set up the environment by reading the `devcontainer.json` configuration files.

3. **Run the App**:
   - Open the terminal in Codespaces and run the following command to start the Streamlit app:
     ```bash
     streamlit run streamlit_app.py
     ```
   - The app will be available at the forwarded port (`http://localhost:8501`) inside Codespaces.

### Option 2: Running Locally

1. **Clone the Repository**:
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/MohammadBaniAbdElNabi/Dynamic_dashboard.git
     cd Dynamic_dashboard
     ```

2. **Create a Virtual Environment** (Optional but recommended):
   - You can create a virtual environment to isolate the project dependencies:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```

3. **Install Dependencies**:
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the App**:
   - Run the Streamlit app:
     ```bash
     streamlit run streamlit_app.py
     ```
   - The app will be available at `http://localhost:8501`.

## Project Structure

- `devcontainer.json`: GitHub Codespaces configuration file to build the development container.
- `requirements.txt`: Lists all Python dependencies for the project.
- `streamlit_app.py`: Main Streamlit application file that contains the logic for fetching data, running Monte Carlo simulations, and rendering the dashboard.

## How It Works

### 1. **Data Fetching**:
   - The app fetches temperature data from a Google Sheets document using the provided Google Sheets link.
   - Data is refreshed every 30 seconds to ensure real-time accuracy.

### 2. **Monte Carlo Simulations**:
   - The app runs Monte Carlo simulations on the temperature data using a **bootstrap resampling** technique.
   - The results are visualized and displayed in an interactive chart, which helps to understand potential future temperature trends.

### 3. **Interactive Features**:
   - **Edit Data**: Users can edit the temperature data directly within the dashboard.
   - **Simulations**: Users can select the number of simulations and view the predicted outcomes.
   - **Download Results**: Once simulations are complete, users can download the results in CSV format.

### 4. **Visualizations**:
   - **Temperature Trend**: Displays the historical temperature trend over time.
   - **Simulated Predictions**: Visualizes the predicted temperature outcomes from the Monte Carlo simulations.


## Contributions

Feel free to fork this project and make contributions! If you have any suggestions, issues, or improvements, please open a **pull request** or **issue** on GitHub.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
