def CyklEulera_MacierzSasiedztwa(matrix, size, edgesnumber, vertex=0):
    """
    :param matrix: macierz sąsiedztwa
    :param size: rozmiar macierzy sąsiedztwa, ilosc wierzchołków
    :param edgesnumber: ilość krawędzi
    :param vertex: index wierzchołka z którym pracujemy
    :return: tablica zawierająca konstruowany cykl Eulera
    """

    def Neighbours(matrix, vertex):
        """
            ZWRACA WSZYSTKICH SĄSIADÓW VERTEX zaczynając od 0

        :param matrix: macierz sąsiedztwa
        :param vertex: podany wierzchołek
        :return: lista sąsiedzi
        """
        result = []
        for i in range(len(matrix[vertex])):
            if matrix[vertex][i] == 1:
                result.append(i)
        return result

    def deleteEdge(matrix, A, B):
        """
            USUWA POŁĄCZENIE A-B

        :param matrix: macierz sąsiedztwa
        :param A: wierzchołek A
        :param B: wierzchołek B

        """
        matrix[A][B] = 0
        matrix[B][A] = 0

    def isConnected(matrix, A, B):
        """
            Sprawdza połączenie wierzchołka A i B

        :param matrix: macierz sąsiedztwa
        :param A: wierzchołek A
        :param B: wierzchołek B
        :return: True or nothing
        """
        if matrix[A][B] == 1 or matrix[B][A] == 1:
            return True

    def CyklEulera_recursive(matrix, path, visited, edgesnumber, vertex, old_matrix):
        """
        :param matrix: macierz sąsiedztwa
        :param path:  lista wynikowa
        :param visited: ostatnio odwiedzony wierzchołek
        :param edgesnumber: rozmiar $matrix
        :param vertex: obecny wierzchołek
        :param old_matrix: stara macierz sąsiedztwa do usuwania połączenia
        :return: path - tablica zawierająca konstruowany cykl Hamiltona
        """
        path.append(vertex)

        if Neighbours(matrix, vertex):
            visited += 1
            neighbour = Neighbours(matrix, vertex)[0]
            # print('У {} есть следующие соседи - {}, visited = {}/{}, запускаю для {}'.format(vertex+1,list(map(lambda x: x+1,Neighbours(matrix,vertex))),visited,edgesnumber,neighbour+1))
            deleteEdge(matrix, vertex, neighbour)
            if CyklEulera_recursive(matrix, path, visited, edgesnumber, neighbour, old_matrix):
                return True
        try:
            if visited == edgesnumber - 1 and isConnected(old_matrix, path[0], vertex):
                path.append(path[0])
                return True
        except:
            pass
        if not Neighbours(matrix, vertex):
            if visited == edgesnumber:
                # koniec)
                return True
            try:
                path.pop()
                previous = path.pop()
                visited -= 1
                # print('У {} нет непосещенных соседей, добавляю {} в result, иду к предыдущему = {}'.format(vertex,vertex,previous+1))
                # print('path = {}'.format(path))
                if CyklEulera_recursive(matrix, path, visited, edgesnumber, previous, old_matrix):
                    return True
            except:
                return False

    path = []
    visited = 0
    old_matrix = copy.deepcopy(matrix)
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                counter += 1
        if counter != 0 and counter % 2 == 0:
            counter = 0
        else:
            print("Nie jest spełniony warunek: stopień każdego wierzchołka jest parzysty")
            return
    succesful = CyklEulera_recursive(matrix, path, visited, edgesnumber, vertex, old_matrix)
    if edgesnumber < size:
        succesful = False
    if succesful:
        if path[0] == path[len(path) - 1]:
            print('Cykl Eulera: ')
            print(list(map(lambda x: x + 1, path)))
    else:
        print('Graf wejściowy nie zawiera cyklu')


def CyklHamiltona_MacierzSasiedztwa(matrix, size):
    """
    :param matrix: macierz sąsiedztwa
    :param size: rozmiar macierzy sąsiedztwa
    :return: returnSolution(path), lista wynikowa - tablica zawierająca konstruowany cykl Hamiltona
    """

    def canReach(matrix, vertex, position, path):
        """
        Czy jest polączenie miedzy position i vertex?
        :param matrix: macierz sąsiedztwa
        :param vertex: podany wierzchołek
        :param position: obecny wierzchołek
        :param path: lista wynikowa
        :return: True or False
        """
        if matrix[path[position - 1]][vertex] == 0:
            return False
        for v in path:
            if v == vertex:
                return False
        return True

    def CyklHamiltona_recursive(matrix, path, position, size):
        if position == size:
            if matrix[path[position - 1]][path[0]] == 1:
                return True
            else:
                return False
        for vertex in range(1, size):
            if canReach(matrix, vertex, position, path):
                # jeżeli polączenie istnieje to dodajemy vertex do path
                path[position] = vertex
                if CyklHamiltona_recursive(matrix, path, position + 1, size):
                    return True
                path[position] = -1
        return False

    def returnSolution(path):
        result = []
        for vertex in path:
            result.append(vertex)
        result.append(path[0])
        return result

    path = [-1] * size
    path[0] = 0
    if CyklHamiltona_recursive(matrix, path, 1, size) == False:
        return False
    return returnSolution(path)