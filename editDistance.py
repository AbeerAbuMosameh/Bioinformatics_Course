from tabulate import tabulate

def edit_distance(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)

    # Initialize DP table with 0's
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    track = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]  # To store the arrows

    # Fill the first row and first column (base case: converting from or to an empty string)
    for i in range(len1 + 1):
        dp[i][0] = i  # Deletion from seq1 to empty string
        track[i][0] = 2  # Arrow pointing up (deletion)

    for j in range(len2 + 1):
        dp[0][j] = j  # Insertion into seq1 to match seq2
        track[0][j] = 1  # Arrow pointing left (insertion)

    # Fill the DP table and tracking table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed (match)
                track[i][j] = 0  # Diagonal arrow (no change)
            else:
                insert = dp[i][j - 1] + 1  # Cost of insertion
                delete = dp[i - 1][j] + 1  # Cost of deletion
                substitute = dp[i - 1][j - 1] + 1  # Cost of substitution

                dp[i][j] = min(insert, delete, substitute)

                if dp[i][j] == insert:
                    track[i][j] = 1  # Left arrow (insertion)
                elif dp[i][j] == delete:
                    track[i][j] = 2  # Up arrow (deletion)
                else:
                    track[i][j] = 3  # Diagonal arrow (substitution)

    # Return both the DP table and the tracking table
    return dp, track

def print_combined_table(dp, track, seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    arrow_dict = {0: "↘", 1: "→", 2: "↓", 3: "↘"}

    # Create table data
    table_data = []

    # Header row
    header = [""] + [""] +list(seq2)
    table_data.append(header)

    # Data rows
    for i in range(len1 + 1):
        row = [seq1[i - 1] if i > 0 else " "]  # Row label
        for j in range(len2 + 1):
            # Format cell with both distance and arrow
            cell = f"{arrow_dict[track[i][j]]}{dp[i][j]}"
            row.append(cell)
        table_data.append(row)

    # Print the table using tabulate
    print(tabulate(table_data, tablefmt="grid"))

# Input sequences
seq1 = "CTCTAAAAGC"
seq2 = "CTCAAAAGCG"

# Calculate the edit distance and the DP table
dp_table, track_table = edit_distance(seq1, seq2)

# Print the combined table
print("Table (Edit Distances and Arrows):")
print_combined_table(dp_table, track_table, seq1, seq2)
