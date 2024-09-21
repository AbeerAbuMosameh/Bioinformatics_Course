def banded_edit_distance(A, B, k):
    m, n = len(A), len(B)

    # Initialize the distance matrix with infinity
    D = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        for j in range(max(1, i - k), min(n, i + k) + 1):
            # Cost of substitution
            cost = 0 if A[i - 1] == B[j - 1] else 1
            D[i][j] = min(
                D[i - 1][j] + 1,  # Deletion
                D[i][j - 1] + 1,  # Insertion
                D[i - 1][j - 1] + cost  # Substitution
            )

    return D[m][n]

# Example usage
x = "ACGTGGCACTGATCA"
y = "ATGTGGGCACTGAAT"
k = 2  # You can adjust this band width as needed
print(f"Banded Edit Distance: {banded_edit_distance(x, y, k)}")
