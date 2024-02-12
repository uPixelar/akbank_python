class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name

        # dosyayı açıp nesne değişkenine atıyoruz
        self.file = open(file_name, "a+", encoding="utf8")

    def __del__(self):
        # dosyayı kapatalım
        self.file.close()

    def get_lines(self):
        self.file.seek(0)
        content = self.file.read()
        lines = content.splitlines()
        return lines

    def list_books(self):
        print("List of books:")
        lines = self.get_lines()
        for line in lines:
            args = line.split(",")
            print(f"{args[0]} by {args[1]}")

    def add_book(self):
        title = input("Please enter book title: ")
        author = input("Please enter book author: ")
        year = input("Please enter book release year: ")
        pages = input("Please enter number of pages: ")

        line = ",".join((title, author, year, pages))

        self.file.write(line+"\n")

    def remove_book(self):
        # show what to remove
        self.list_books()
        title = input("Please enter book title to remove: ")

        lines = self.get_lines()

        for line in lines:
            args = line.split(",")
            if args[0] == title:
                lines.remove(line)
                content = "\n".join(lines)
                self.file.truncate(0)
                self.file.write(content+"\n")
                return

        print(f"The book with title '{title}' is not found!")





# testing
if __name__ == "__main__":
    lib = Library()
    lib.list_books()
    lib.add_book()
    lib.list_books()
    lib.remove_book()
    lib.list_books()
    del lib