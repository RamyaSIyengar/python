if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

    matrix = []
    for i in range(len(name)):
        matrix.append([])
        for j in range(len(name)):
            matrix[i].append(name[j], score[j])

    print(matrix)
