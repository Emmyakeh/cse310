def implies(p, q):
    """Return True if p implies q."""
    return not p or q

def iff(p, q):
    """Return True if p if and only if q."""
    return (p and q) or (not p and not q)

# Function to print the truth table
def print_truth_table():
    print("p\tq\tp -> q\tp <-> q")
    for p in [True, False]:
        for q in [True, False]:
            print(f"{p}\t{q}\t{implies(p, q)}\t{iff(p, q)}")

# Call the function to display the truth table
print_truth_table()
