def hourglassSum(arr):
    for p in range(len(arr)):
        for r in range(len(arr[p])):
            assert -9 <= arr[p][r] <= 9
        assert len(arr[p]) == 6

    unseparated_matrixes = []
    for hs in range(4):
        for vs in range(4):
            for v in range(3):
                for h in range(3):
                    unseparated_matrixes.append(arr[v + vs][h + hs])

    separated_matrix = []
    counter = 0

    for y in range(16):
        temp_list = []
        for z in range(9):
            temp_list.append(unseparated_matrixes[z + counter])
        separated_matrix.append(temp_list)
        counter += 9

    sum_of_each_matrixes = []
    for L in range(16):
        sum_of_each_matrixes.append(separated_matrix[L][0]
                                    + separated_matrix[L][1]
                                    + separated_matrix[L][2]
                                    + separated_matrix[L][4]
                                    + separated_matrix[L][6]
                                    + separated_matrix[L][7]
                                    + separated_matrix[L][8])

    sum_of_each_matrixes.sort()

    return sum_of_each_matrixes[-1]

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))
