import time, tracemalloc, os, csv
from colors import Colors

colors = Colors()


def timer(no_print=False, csv_path=""):
    # Checking if csv file exists
    if csv_path:
        csv_path = os.path.abspath(csv_path)
        if not csv_path.strip().endswith(".csv"):
            csv_path = csv_path.strip() + ".csv"
        with open(csv_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(["function", "runtime", "memory_usage", "memory_peak"])

    def wrapper(func):
        def wrapped_function(*args, **kwargs):
            tracemalloc.start()
            time_start = time.perf_counter()
            func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            time_end = time.perf_counter()
            calc_mem = lambda mem: f"{mem / 10**6:.6f}"
            calc_time = f"{time_end - time_start:0.4f}"
            if not no_print:
                print(colors.pink("-" * 75))
                print(
                    f"{colors.purple(func.__name__)}{colors.yellow(args)}: took {colors.pink(calc_time)} seconds"
                )
                print(colors.pink("~" * 75))
                print(
                    f"Memory usage:\t\t {colors.green(calc_mem(current))} MB \n"
                    f"Peak memory usage:\t{colors.red(calc_mem(peak))} MB "
                )
            if csv_path:
                with open(csv_path, "a", newline="") as csvfile:
                    writer = csv.writer(csvfile, delimiter=",")
                    writer.writerow(
                        [
                            f"{func.__name__}{args}",
                            calc_time,
                            calc_mem(current),
                            calc_mem(peak),
                        ]
                    )

        return wrapped_function

    return wrapper
