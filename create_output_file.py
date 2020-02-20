LIST_FORMAT = [
    {
        "library_id": 1,
        "list_of_books": [
            1, 2, 3, 4, 5
        ]
    },
    {
        "library_id": 2,
        "list_of_books": [
            6, 7, 8, 9, 10
        ]
    },
    {
        "library_id": 3,
        "list_of_books": [
            11, 12, 13, 14, 15
        ]
    },
]

def create_output_file(queue):
    file = open("output_file", "w+")
    file.write(str(len(queue)) + '\n')
    for q in queue:
        file.write(str(q["library_id"]) + " " + str(len(q["list_of_books"])) + "\n")
        for book in q["list_of_books"]:
            file.write(str(book) + " ")
        file.write('\n')

    file.close()
    return

if __name__ == "__main__":
    create_output_file(LIST_FORMAT)