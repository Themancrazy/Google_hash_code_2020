import numpy as np

class sortLibs:
    def __init__(self, list_books_total, list_lib, list_headers, tot_time, tot_books, tot_lib):
        """
        Args:
            - list_books_total: list of books and their scores
            - list_lib: all libraries and their books ids (sorted -> no doubles and id are sorted by biggest score to smallest)
            - list_headers: all headers (number of books in lib, time scanning lib, number books/day after signup)
            - tot_time: total amount of time available to process libs and store books
            - tot_books: total amount of books available
            - tot_lib: total amount of libraries
        """
        self.list_books = list_books_total
        self.list_lib = list_lib
        self.list_headers = list_headers
        self.tot_time = tot_time
        self.tot_books = tot_books
        self.tot_lib = tot_lib
        self.final_queue = []

    def add_library_to_queue(self, lib_node):
        new_queue = self.final_queue
        if len(new_queue) < 1:
            new_queue.append(lib_node)
        else:
            for index, lib in zip(range(len(self.final_queue) + 1), self.final_queue):
                if lib_node["total_score"] >= lib["total_score"]
                    new_queue.insert(index, lib_node)
                    break
        self.final_queue = new_queue

    def get_lib_score(self, library, lib_header):
        lib = sort_raw_lib(library)
        amount_books = len(lib)
        available_time = self.tot_time - lib_header[2]
        books_per_day = lib_header[2]
        total_slots_available = available_time * books_per_day
        total_score = 0
        list_books = []
        for _, book in zip(range(total_slots_available), lib):
            total_score += self.list_books_total[book]
            list_books.append(book)
        return list_books, total_score

    def parse_libraries(self):
        lib_id = 0
        lib_node = {}
        for lib, header in zip(self.list_lib, self.lib_headers):
            header = header.append(lib_id)
            lib_books, lib_score = get_lib_score(lib, header)
            lib_id += 1
            lib_node["library_id"] = lib_id
            lib_node["list_of_books"] = lib_books
            lib_node["total_score"] = lib_score
            add_library_to_queue(lib_node)
        
        