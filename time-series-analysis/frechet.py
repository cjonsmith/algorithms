def frechet(P, Q, r):
    """Determines if there is a path along P and Q that never exceeds r."""
    # list of lists of Nones: 2D Matrix of |P| rows and |Q| columns.
    paths = [[None for _ in range(len(Q))] for _ in range(len(P))]
    paths[0][0] = distance(P[0], Q[0]) <= r
    # Initialize the first values of the rows.
    for i in range(1, len(P)):
        paths[i][0] = distance(P[i], Q[0]) <= r and paths[i-1][0]

    # Initialize the first values of the columns.
    for j in range(1, len(Q)):
        paths[0][j] = distance(P[0], Q[j]) <= r and paths[0][j-1]

    for i in range(1, len(paths)):
        for j in range(1, len(paths[i])):
            paths[i][j] = distance(P[i], Q[j]) <= r and \
                (paths[i-1][j-1] or \
                 paths[i-1][j]   or \
                 paths[i][j-1])
    
    return paths


def distance(start, end):
    """Calculates the distance between two catesian points."""
    return ((start[0] - end[0])**2 + (start[1] - end[1])**2) ** 0.5


def main():
    P = [(1, 1), (2, 1.5), (3, 2), (4, 2), (5, 1.5), 
         (5.1, 1.5), (5.1, 1.4), (6, 1)]
    Q = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
    r_3 = frechet(P, Q, 3)
    r_2 = frechet(P, Q, 2)
    print('frechet r = 3'.center(15, '-'))
    for i, line in enumerate(r_3):
        print([str(x).rjust(5) for x in line])
    print('frechet r = 2'.center(15, '-'))
    for i, line in enumerate(r_2):
        print([str(x).rjust(5) for x in line])


if __name__ == "__main__":
    main()
