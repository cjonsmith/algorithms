def dynamic_time_warping(P, Q):
    """Determines if there is a path along P and Q that never exceeds r."""
    # list of lists of Nones: 2D Matrix of |P| rows and |Q| columns.
    paths = [[None for _ in range(len(Q))] for _ in range(len(P))]
    paths[0][0] = distance(P[0], Q[0])

    # Initialize the first values of the rows.
    for i in range(1, len(paths)):
        paths[i][0] = paths[i-1][0] + distance(P[i], Q[0])

    # Initialize the first values of the columns.
    for j in range(1, len(paths[0])):
        paths[0][j] = paths[0][j-1] + distance(P[0], Q[j])

    for i in range(1, len(P)):
        for j in range(1, len(Q)):
            paths[i][j] = distance(P[i-1], Q[j-1]) + \
                min(paths[i-1][j-1],
                    paths[i-1][j],
                    paths[i][j-1])
    
    return paths


def distance(start, end):
    """Calculates the distance between two catesian points."""
    return ((start[0] - end[0])**2 + (start[1] - end[1])**2) ** 0.5


def main():
    P = [(1, 1), (2, 1.5), (3, 2), (4, 2), (5, 1.5), 
         (5.1, 1.5), (5.1, 1.4), (6, 1)]
    Q = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
    dtw = dynamic_time_warping(P, Q)
    print('dtw'.center(15, '-'))
    for i, line in enumerate(dtw):
        print([str(round(x, 2)).rjust(5) for x in line])

if __name__ == "__main__":
    main()
