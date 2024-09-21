import numpy as np
import matplotlib.pyplot as plt


def generate_comparison_matrix(seq1, seq2, e):
    len1 = len(seq1)
    len2 = len(seq2)

    # Initialize the comparison matrix (0 for black, 1 for white)
    matrix = np.zeros((len1, len2), dtype=int)

    # Compare each base within the range of 2e+1
    for i in range(len1):
        for j in range(len2):
            if abs(i - j) <= 2 * e:  # Check if within the window
                if seq1[i] == seq2[j]:  # Match case
                    matrix[i, j] = 1  # White cell (match)
                else:
                    matrix[i, j] = 0  # Black cell (mismatch)
            else:
                matrix[i, j] = 0  # Outside comparison range is black (not compared)

    return matrix


def plot_comparison_matrix(matrix, seq1, seq2):
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='gray')

    # Set ticks and labels for the sequences
    ax.set_xticks(np.arange(len(seq2)))
    ax.set_yticks(np.arange(len(seq1)))
    ax.set_xticklabels(list(seq2))
    ax.set_yticklabels(list(seq1))

    # Rotate the tick labels for better readability
    plt.xticks(rotation=90)

    # Show the grid
    ax.grid(False)

    plt.show()


# Input sequences and e value from user
seq1 = input("Enter the first sequence: ")
seq2 = input("Enter the second sequence: ")
e = int(input("Enter the value of e: "))

# Generate the comparison matrix
matrix = generate_comparison_matrix(seq1, seq2, e)

# Plot the result
plot_comparison_matrix(matrix, seq1, seq2)