# 🧟 Interactive Zombie Outbreak Simulator

A powerful, interactive web-based simulation tool to visualize the dynamics of a zombie outbreak (or virus spread) using the classic **SIR (Susceptible-Infected-Recovered)** model. Built with Python and Streamlit.

## 🚀 Features

- **Interactive Controls**: Adjust population size, initial infection count, and simulation duration in real-time.
- **Epidemiology Modeling**: Tweak **Infection Rate ($\beta$)** and **Recovery Rate ($\gamma$)** to see how they impact the spread.
- **R0 Calculator**: Automatically calculates and displays the basic reproduction number ($R_0$) to predict if the outbreak will explode or die out.
- **Dynamic Visualization**: Live-updating line charts showing the progression of Susceptible, Infected, and Recovered populations.
- **Key Metrics**: Instant view of final stats like "Healthy Left", "Peak Zombies", and "Total Recovered".

## 🛠️ Prerequisites

Ensure you have **Python 3.x** installed on your system.
This project relies on the following Python libraries:
- `streamlit`
- `pandas`
- `numpy`

## 📦 Installation

1. **Clone or Download** this repository to your local machine.

2. **Navigate to the project directory**:
   ```bash
   cd path/to/project
   ```

3. **(Optional but Recommended) Create and Activate a Virtual Environment**:
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   You can install the required packages using pip:
   ```bash
   pip install streamlit pandas numpy
   ```

## 🎮 Usage

To run the simulation, execute the following command in your terminal:

```bash
streamlit run zombie_sim.py
```

This will automatically open the application in your default web browser (usually at `http://localhost:8501`).

## 🧠 Understanding the Parameters

- **Total Population (N)**: The total number of people in the simulation.
- **Initial Zombies (I0)**: How many people start as infected (Patient Zero).
- **Infection Rate (Beta)**: The probability of transmitting the infection per contact. Higher beta = faster spread.
- **Recovery Rate (Gamma)**: The rate at which infected individuals recover (or are removed/die). Higher gamma = faster recovery.
- **R0 (Reproduction Number)**: $\beta / \gamma$.
  - If $R_0 < 1$: The outbreak dies out.
  - If $R_0 > 1$: The outbreak grows exponentially.
