#!/bin/python3

# Given a square matrix of size N×NN×N, calculate the absolute difference
# between the sums of its diagonals.

# Input Format

# The first line contains a single integer, NN. The next NN lines denote the
# matrix's rows, with each line containing NN space-separated integers
# describing the columns.

# Output Format

# Print the absolute difference between the two sums of the matrix's diagonals
# as a single integer.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12


# Explanation

# The primary diagonal is:
# 11
#       5
#            -12

# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:
#            4
#      5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15


import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
