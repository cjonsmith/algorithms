import math
del_cost, insert_cost, replace_cost = 1, 1, 1

def edit_distance(x, y):
    table = [[math.inf for _ in range(len(y))] for _ in range(len(x))]
    for i in range(len(x)):
        table[i][0] = i 
    for j in range(len(y)):
        table[0][j] = j 
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min(table[i-1][j] + del_cost,
                                  table[i-1][j-1] + replace_cost,
                                  table[i][j-1] + insert_cost)
    for line in table:
        print(line)

def main():
    edit_distance("AAhello", "AhelloA")

if __name__ == "__main__":
    main()
