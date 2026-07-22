class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hey {self.name}"


def main():
    name = input("Name: ")
    greet = Name(name)
    print(greet)


if __name__ == "__main__":
    main()