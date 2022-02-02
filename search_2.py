class Search:
    size_arr: int = 0
    array: list = []
    search_elem: int = 0

    def __init__(self, size_arr: int, array: list, search_elem: int):
        self.size_arr = size_arr
        self.array = array
        self.search_elem = search_elem

    def bool_search(self) -> bool:
        for elem in range(len(self.array)):
            if self.array[elem] == self.search_elem:
                return True
        return False


def main():
    size_array = int(input())
    array = [int(i) for i in input().split()]
    search_element = int(input())
    search = Search(size_array, array, search_element)
    print(search.bool_search())


if __name__ == '__main__':
    main()
