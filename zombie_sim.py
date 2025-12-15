import streamlit as st
import pandas as pd
import numpy as np

# --- 1. SET UP THE INTERFACE ---
st.title("🧟 Interactive Zombie Outbreak Simulator")
st.write("""
Adjust the parameters in the **sidebar** to see how the virus spreads.
Can you flatten the curve?
""")

# --- 2. THE SIDEBAR (User Inputs) ---
st.sidebar.header("Simulation Parameters")

# Sliders for the user to tweak variables
N = st.sidebar.number_input("Total Population (N)", value=1000, step=100)
I0 = st.sidebar.number_input("Initial Zombies (I0)", value=1, step=1)
days = st.sidebar.slider("Duration (Days)", min_value=10, max_value=365, value=100)

st.sidebar.markdown("---") # Separator line

# The Rates (The most important sliders)
beta = st.sidebar.slider("Infection Rate (Beta)", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
gamma = st.sidebar.slider("Recovery Rate (Gamma)", min_value=0.0, max_value=1.0, value=0.1, step=0.01)

# Display R0 (Reproduction Number)
if gamma > 0:
    r0_val = beta / gamma
    st.sidebar.write(f"**R0 (Reproduction Number):** {r0_val:.2f}")
    if r0_val < 1:
        st.sidebar.success("The outbreak will die out!")
    else:
        st.sidebar.error("The outbreak will grow!")

# --- 3. RUN THE SIMULATION (The Engine) ---

# Initialize variables based on user input
S, I, R = N - I0, I0, 0
S_list, I_list, R_list = [S], [I], [R]

# The Math Loop
for _ in range(days):
    new_infections = (beta * S * I) / N
    new_recoveries = gamma * I
    
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    
    # Clip values to ensure they don't go below 0
    S, I, R = max(S, 0), max(I, 0), max(R, 0)
    
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# --- 4. VISUALIZATION ---

# Convert data to a DataFrame (Table) for easy charting
chart_data = pd.DataFrame({
    "Susceptible": S_list,
    "Infected": I_list,
    "Recovered": R_list
})

# Create an interactive Line Chart
st.line_chart(chart_data)

# Show final stats
col1, col2, col3 = st.columns(3)
col1.metric("Healthy Left", int(S))
col2.metric("Peak Zombies", int(max(I_list)))
col3.metric("Total Recovered/Dead", int(R))