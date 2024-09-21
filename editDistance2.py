from tabulate import tabulate

# Function to calculate the edit distance between two sequences
def edit_distance(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)

    # Initialize DP table with zeros
    # creates a list of size len2 + 1, filled with zeroes (0)  .. size of the matrix is (len1 + 1) x (len2 + 1)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)] # 2D list (or matrix)
    track = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]  # To store arrows for path

    # Fill the first row and column (for base case: converting empty string to the other)
    for i in range(len1 + 1):
        dp[i][0] = i  # Deletion from seq1 to empty string
        track[i][0] = 2  # Arrow   "↓"

    for j in range(len2 + 1):
        dp[0][j] = j  # Insertion into seq1 to match seq2
        track[0][j] = 1  # Arrow "→"

    # apply conditions if 2 Sequence base same no change and if not same apply min + 1
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:  # If characters match A = A
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                track[i][j] = 0  # Diagonal arrow (no change)
            else:
                insert = dp[i - 1][j] + 1  # Cost of insert "↓"
                delete = dp[i][j - 1] + 1  # Cost of delete "→"
                substitute = dp[i - 1][j - 1] + 1  # Cost of substitution

                # Choose the operation with the least cost
                dp[i][j] = min(insert, delete, substitute)

                # Track the direction of the chosen operation
                if dp[i][j] == insert:
                    track[i][j] = 2
                elif dp[i][j] == delete:
                    track[i][j] = 1
                else:
                    track[i][j] = 3

    # Return the DP table (costs) and track table (arrows)
    return dp, track

# Function to print the edit distance table and track the optimal path
def print_combined_table(dp, track, seq1, seq2, file_name):
    len1, len2 = len(seq1), len(seq2)

    arrow = {0: "↘", 1: "→", 2: "↓", 3: "↘"}

    # Prepare the combined table data with arrows and distances
    table_data = []

    # First row: header with indices for sequence
    index_row = [" "] + [" "] + [f"{x}" for x in range(len2 + 1)]  # j index
    table_data.append(index_row)

    # Second row: sequence2 characters
    seq2_row = [" ", "  " , " "] + list(seq2)
    table_data.append(seq2_row)

    # Fill the rest of the table with values from DP and arrow from track
    for i in range(len1 + 1):
        row = [f"{i}"]  # Add row index (i=)
        row.append(seq1[i - 1] if i > 0 else " ")  # Add seq1 character for current row
        for j in range(len2 + 1):
            cell = f"{arrow[track[i][j]]}{dp[i][j]}"  # Combine arrow and distance
            row.append(cell)  # Add cell to the row
        table_data.append(row)

    # Prepare data for the path table (showing optimal path)
    path_data = []
    path_index_row = [" "] + [" "] + [f"{idx}" for idx in range(len2 + 1)]  # Header for j indices
    path_data.append(path_index_row)
    path_seq_row = ["  ", " " , " "] + list(seq2)  # Second row with sequence2 characters
    path_data.append(path_seq_row)

    # Initialize the path table grid with spaces
    for i in range(len1 + 1):
        path_row = [f"{i}"]  # Add row index (i=)
        path_row.append(seq1[i - 1] if i > 0 else " ")  # Add seq1 character for current row
        path_row.extend([" " for _ in range(len2 + 1)])  # Empty cells for path
        path_data.append(path_row)

    # Trace the optimal path in the DP table
    i, j = len1, len2
    while i > 0 or j > 0:
        path_data[i + 2][j + 2] = f"({i},{j})"  # Mark the current position in the path

        # Move according to the direction in the track table
        if i > 0 and j > 0 and track[i][j] == 0:  # No operation (match)
            i -= 1
            j -= 1
        elif i > 0 and track[i][j] == 2:  # Insertion
            i -= 1
        elif j > 0 and track[i][j] == 1:  # Deletion
            j -= 1
        elif i > 0 and j > 0 and track[i][j] == 3:  # Substitution
            i -= 1
            j -= 1

    path_data[2][2] = "(0,0)"  # Start at (0,0)

    # Write the results to a file
    with open(file_name, 'w', encoding='utf-8') as file:
        # Write combined table (edit distances and arrows)
        file.write("Combined Table (Edit Distances and Arrows):\n")
        file.write(tabulate(table_data, tablefmt="grid") + "\n")

        # Write the path table
        file.write("\nPath Table:\n")
        file.write(tabulate(path_data, tablefmt="grid") + "\n")

# Example usage of the functions
seq2 = "ACGTGGCACTGATCA"
seq1 = "ATGTGGGCACTGAAT"

# Get the edit distance and track tables
dp_table, track_table = edit_distance(seq1, seq2)

# Save the output to a file
file_name = "edit_distance_output.txt"
print_combined_table(dp_table, track_table, seq1, seq2, file_name)
