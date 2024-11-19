import matplotlib.pyplot as plt
import random
import numpy as np


def generate_sierpinski_triangle_markov(iterations):
    vertices = [
        (0, 0),
        (1, 0),
        (0.5, 0.866)
    ]

    current_point = (random.uniform(0, 1), random.uniform(0, 1))

    points = [current_point]

    transition_matrix = np.array([
        [0.3, 0.5, 0.2],
        [0.4, 0.3, 0.3],
        [0.3, 0.3, 0.4]
    ])

    previous_vertex_index = random.randint(0, 2)

    for _ in range(iterations):
        probabilities = transition_matrix[previous_vertex_index]
        selected_vertex_index = np.random.choice([0, 1, 2], p=probabilities)
        selected_vertex = vertices[selected_vertex_index]

        midpoint = (
            (current_point[0] + selected_vertex[0]) / 2,
            (current_point[1] + selected_vertex[1]) / 2
        )

        current_point = midpoint

        previous_vertex_index = selected_vertex_index

        points.append(current_point)

    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, s=0.1, color="blue")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

    return "Done!"


iterations = 50000
result = generate_sierpinski_triangle_markov(iterations)
print(result)