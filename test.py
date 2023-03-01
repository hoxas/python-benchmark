from timer import timer


@timer(csv_path="log.csv")
def generate_range(start, end):
    list(range(start, end + 1))


@timer(csv_path="log.csv")
def generate_save_return_range(start, end):
    var = list(range(start, end + 1))
    return var


@timer(csv_path="log.csv")
def generate_return_range(start, end):
    return list(range(start, end + 1))


@timer(csv_path="log.csv")
def iterate_range(start, end):
    for num in range(start, end + 1):
        pass


if __name__ == "__main__":
    generate_range(0, 10000000)
    generate_save_return_range(0, 10000000)
    generate_return_range(0, 10000000)
    iterate_range(0, 10000000)
