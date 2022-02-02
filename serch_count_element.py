class Search:
    count = 0
    def __init__(self,size_array,array,search_element):
        self.size_array = size_array
        self.array = array
        self.search_element = search_element

    def search_count(self):
        for elem in range(len(self.array)):
            if self.search_element == self.array[elem]:
                self.count += 1
        return self.count

def main():
    size_array = int(input())
    array = [int(i) for i in input().split()]
    search_element = int(input())
    search = Search(size_array,array, search_element)
    print(search.search_count())


if __name__ == '__main__':
    main()