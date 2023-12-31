from matplotlib import pyplot as plt
import numpy as np
from config import BLOCH_SPHERE_ALPHA
from custom_packages.state_visualization import plot_bloch_vector

def calculate_phi_and_theta(a, b):
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b / np.sin(theta / 2)) if theta != 0 else 0
    return theta, phi

def display_states(states):
    fig = plt.figure()
    fig.canvas.manager.set_window_title('1-qubit states')
    ax = fig.add_subplot(111, projection='3d')
    quantum_states = [np.array([complex(x) for x in line.split()]) for line in states]
    for state in quantum_states:
        theta, phi = calculate_phi_and_theta(state[0], state[1])
        bloch_vector = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]
        plot_bloch_vector(bloch_vector, ax=ax, sphere_alpha=BLOCH_SPHERE_ALPHA)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere', pad=50)

    plt.show()