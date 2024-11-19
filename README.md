# Sierpinski Triangle Generator with Markov Chain

This project generates the Sierpinski Triangle using a Markov chain-based approach. By combining a simple transition matrix with a random walk between the vertices of an equilateral triangle, the script creates a beautiful fractal pattern known as the Sierpinski triangle. It blends chaos theory and stochastic processes in an educational and visually appealing way.

 # Features

Uses a Markov chain transition matrix to decide the next vertex in the sequence.

Generates a Sierpinski triangle based on random walks.

Provides a visual demonstration of how simple probabilistic rules can produce complex fractal structures.

# Requirements

- Python 3.x
- Libraries:
- matplotlib for visualizing the generated points.
- numpy for handling the transition matrix and probabilistic selection.

# Installation

To get started, clone the repository and install the required libraries:

```
git clone github.com/komyl/markovian-sierpinski
cd markovian-sierpinski
pip install -r requirements.txt
```

Alternatively, you can install the libraries manually:

```
pip install matplotlib numpy
```

# Usage

Run the script to generate the Sierpinski triangle. You can adjust the number of iterations to control the detail of the fractal:

```
python MarkovChaosTriangle.py
```

# Example

By default, the script generates 50,000 points, which results in a well-defined Sierpinski triangle:

```
iterations = 50000
result = generate_sierpinski_triangle_markov(iterations)
print(result)
```

This will display the Sierpinski triangle and print a confirmation message indicating that the triangle has been generated and plotted.

# Explanation

The script starts with a random point within the bounds of an equilateral triangle. It then uses a Markov chain to decide which vertex to move towards at each step, according to predefined transition probabilities in the transition matrix. By iteratively finding the midpoint between the current point and a chosen vertex, the famous fractal shape emerges.

- Vertices: The vertices of the triangle are defined as (0, 0), (1, 0), and (0.5, 0.866).

- Transition Matrix: The probabilities for choosing the next vertex depend on the current vertex. This randomness adds the Markovian behavior to the generation process.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgements

This project was inspired by the Chaos Game algorithm, which shows how simple iterative rules can lead to surprisingly complex results, similar to Markov chains and fractal geometry.

## Authors

This project was developed by **Komeyl Kalhorinia**. For any inquiries or contributions, feel free to reach out at [Komylfa@gmail.com]

## Made with ❤️ by Komeyl Kalhorinia

