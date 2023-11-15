import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulate_random_walk(steps, num_simulations):
    final_positions = []

    for _ in range(num_simulations):
        x, y = 0, 0
        for _ in range(steps):
            direction = np.random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up':
                y += 1
            elif direction == 'down':
                y -= 1
            elif direction == 'left':
                x -= 1
            elif direction == 'right':
                x += 1
        final_positions.append((x, y))

    return final_positions

def main():
    st.title("Random Walk Simulation")

    # User input
    steps = st.slider("Number of Steps", min_value=1, max_value=100, value=10)
    num_simulations = st.slider("Number of Simulations", min_value=1, max_value=1000, value=100)

    # Run simulations
    final_positions = simulate_random_walk(steps, num_simulations)

    # Plot the random walk trajectories
    fig, ax = plt.subplots()
    ax.set_title("Random Walk Trajectories")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    for position in final_positions:
        ax.plot(*position, marker='o')

    st.pyplot(fig)

    # Calculate and display probability distribution
    unique_positions, counts = np.unique(final_positions, axis=0, return_counts=True)
    probabilities = counts / num_simulations

    st.subheader("Probability Distribution of Final Positions")
    st.table({"Position": unique_positions, "Probability": probabilities})

if __name__ == "__main__":
    main()
