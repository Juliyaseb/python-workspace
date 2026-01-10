#!/usr/bin/env python3

import numpy as np
import pandas as pd

def main():
    print("=== Sample Python Data Script ===\n")

    # NumPy Example
    numbers = np.array([10, 20, 30, 40, 50])
    print("NumPy array:", numbers)
    print("Sum:", np.sum(numbers))
    print("Mean:", np.mean(numbers), "\n")

    # pandas Example
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [25, 30, 35, 28],
        "Score": [88, 92, 85, 95]
    }

    df = pd.DataFrame(data)
    print("Pandas DataFrame:")
    print(df, "\n")

    # Filter rows
    print("People with Score > 90:")
    print(df[df['Score'] > 90])

if __name__ == "__main__":
    main()
