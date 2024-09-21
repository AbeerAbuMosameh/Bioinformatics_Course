from collections import Counter

def count_sequences(file_path, sequences):
    counts = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            # Skip headers in FASTA/FASTQ
            if line.startswith(">") or line.startswith("@") or line.startswith("+"):
                continue
            # Strip newlines and process the line
            line = line.strip()
            # Count each sequence
            for seq in sequences:
                counts[seq] += line.count(seq)
    return counts

def main():
    # Sequences to count
    sequences = ["A", "C", "G", "T", "AA", "AC", "AG", "AT",
                 "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT",
                 "TA", "TC", "TG", "TT"]

    # Count in dummy.fasta
    fasta_counts = count_sequences("data/dummy.fasta", sequences)
    print("dummy.fasta:")
    for sub_seq in sequences:
        print(f"{sub_seq}: {fasta_counts[sub_seq]}")

    print("***********************")

    # Count in dummy.fastq
    fastq_counts = count_sequences("data/dummy.fastq", sequences)
    print("dummy.fastq:")
    for sub_seq in sequences:
        print(f"{sub_seq}: {fastq_counts[sub_seq]}")

if __name__ == "__main__":
    main()
