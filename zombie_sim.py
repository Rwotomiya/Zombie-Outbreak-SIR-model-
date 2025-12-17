import streamlit as st
import pandas as pd
import numpy as np

# --- 1. SET UP THE INTERFACE ---
st.title("🧟 Interactive Zombie Outbreak Simulator")
st.markdown("""
Adjust the parameters to see how the virus spreads.
**New:** Use the **Vaccine Slider** to see if you can achieve Herd Immunity!
""")

# --- 2. THE SIDEBAR (User Inputs) ---
st.sidebar.header("Simulation Parameters")

# Basic Population
N = st.sidebar.number_input("Total Population (N)", value=1000, step=100)
I0 = st.sidebar.number_input("Initial Zombies (I0)", value=1, step=1)
days = st.sidebar.slider("Duration (Days)", 10, 365, 100)

st.sidebar.markdown("---")

# The Rates
beta = st.sidebar.slider("Infection Rate (Beta)", 0.0, 1.0, 0.3, 0.01)
gamma = st.sidebar.slider("Recovery Rate (Gamma)", 0.0, 1.0, 0.1, 0.01)

st.sidebar.markdown("---")

# --- NEW FEATURE: VACCINATION ---
st.sidebar.header("💉 Prevention")
vaccine_pct = st.sidebar.slider("Percentage Vaccinated", 0, 100, 0)
vaccine_efficency = 1.0 # Assuming 100% effective for simplicity

# --- 3. MATH & LOGIC ---

# Calculate Initial Numbers
# Vaccinated people are removed from Susceptible immediately
vaccinated_count = int(N * (vaccine_pct / 100))
S0 = N - I0 - vaccinated_count
I = I0
R = vaccinated_count # Vaccinated people start as "Recovered/Immune"

# Safety check: If we vaccinated more people than exist
if S0 < 0:
    S0 = 0

# Lists to store history
S_list, I_list, R_list = [S0], [I], [R]

# The Simulation Loop
for _ in range(days):
    # Current Susceptible
    S = S_list[-1]
    
    new_infections = (beta * S * I) / N
    new_recoveries = gamma * I
    
    S_new = S - new_infections
    I_new = I + new_infections - new_recoveries
    R_new = R + new_recoveries
    
    # Clip to 0 to prevent negative numbers
    S_new, I_new, R_new = max(S_new, 0), max(I_new, 0), max(R_new, 0)
    
    # Update lists
    S_list.append(S_new)
    I_list.append(I_new)
    R_list.append(R_new)
    
    # Update current values for next loop
    S, I, R = S_new, I_new, R_new

# --- 4. VISUALIZATION ---

# Create Data Table
chart_data = pd.DataFrame({
    "Susceptible (Healthy)": S_list,
    "Infected (Zombies)": I_list,
    "Recovered / Immune": R_list
})

# Display Metrics at the top
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Population", int(N))
col2.metric("Vaccinated Start", vaccinated_count)
col3.metric("Peak Infections", int(max(I_list)))
col4.metric("Total Deaths/Recoveries", int(R_list[-1]))

# Interactive Chart
st.line_chart(chart_data)

# Show R0 Logic
if gamma > 0:
    r0 = beta / gamma
    herd_immunity_threshold = 1 - (1/r0)
    
    st.info(f"**Math Fact:** With an R0 of {r0:.2f}, you need to vaccinate **{herd_immunity_threshold*100:.1f}%** of the population to stop the spread instantly.")