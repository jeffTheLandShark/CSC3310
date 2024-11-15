import time
import random
import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt


def partition(lst, low, high):
    pivot_index = random.randint(low, high)
    lst[pivot_index], lst[high] = lst[high], lst[pivot_index]
    pivot = lst[high]

    i = low
    for j in range(low, high):
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[high] = lst[high], lst[i]
    return i


def select(lst, low, high, k_smallest):
    if low == high:
        return lst[low]

    pivot_index = partition(lst, low, high)

    if k_smallest == pivot_index:
        return lst[k_smallest]
    elif k_smallest < pivot_index:
        return select(lst, low, pivot_index - 1, k_smallest)
    else:
        return select(lst, pivot_index + 1, high, k_smallest)


def quickselect(lst, k):
    if k < 1 or k > len(lst):
        raise ValueError("k is out of bounds")
    return select(lst, 0, len(lst) - 1, k - 1)


def sortselect(lst, k):
    return sorted(lst)[k - 1]


def benchmark(algorithm, input_list, k):
    input_list = input_list.copy()
    start_time = time.perf_counter()
    result = algorithm(input_list, k)
    end_time = time.perf_counter()
    return end_time - start_time


def estimate_slope(list_sizes, run_times):
    list_sizes = np.array(list_sizes)
    run_times = np.array(run_times)
    valid_indices = (list_sizes > 0) & (run_times > 0)
    list_sizes = list_sizes[valid_indices]
    run_times = run_times[valid_indices]

    if len(list_sizes) == 0 or len(run_times) == 0:
        return 0

    m, _, _, _, _ = linregress(np.log(list_sizes), np.log(run_times))
    return m


def get_complexity(m):
    if m == 0:
        return "Constant"
    elif m < 1:
        return "Sub-linear (e.g., log n)"
    elif m == 1:
        return "Linear"
    elif m > 1 and m < 2:
        return "Between linear and quadratic (e.g., n log n)"
    elif m == 2:
        return "Quadratic (e.g., n^2)"
    elif m > 2 and m < 3:
        return "Between quadratic and cubic (e.g., n^2 log n)"
    elif m == 3:
        return "Cubic (e.g., n^3)"
    else:
        return "Out of Scope"


if __name__ == "__main__":
    print("Begin!!")
    random.seed(42)

    list_sizes = [100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000]
    benchmark_lists = {
        "best": [list(range(n)) for n in list_sizes],
        "worst": [list(range(n, 0, -1)) for n in list_sizes],
        "random": [random.sample(range(n), n) for n in list_sizes]
    }

    benchmark_results = {
        "quickselect": {"best": [], "worst": [], "random": []},
        "sortselect": {"best": [], "worst": [], "random": []}
    }

    with open("benchmark_results.txt", "w") as out_file:
        out_file.write("Lab 4 Benchmarking:\n\n")

        for algo in [quickselect, sortselect]:
            for case, lists in benchmark_lists.items():
                for lst in lists:
                    n = len(lst)
                    out_file.write(f"Running {algo.__name__} with size {n} - case {case}\n")
                    k_values = range(n // 100, n, n // 100)
                    for k in k_values:
                        times = [benchmark(algo, lst, k) for _ in range(10)]
                        avg_time = np.mean(times)
                        k_fraction = k * 100 // n
                        if k_fraction % 20 == 0:
                            out_file.write(f"  k={k_fraction} took {avg_time:.6f} seconds\n")

                        benchmark_results[algo.__name__][case].append({
                            'size': n,
                            'k_value': k_fraction,
                            'time': avg_time
                        })

        # Analyze complexities
        out_file.write("\nComplexity Analysis:\n")
        for algo_name, cases in benchmark_results.items():
            out_file.write(f"\nAlgorithm: {algo_name}\n")
            for case, results in cases.items():
                df = pd.DataFrame(results)
                if df.empty:
                    continue
                m = estimate_slope(df['size'], df['time'])
                complexity = get_complexity(m)
                out_file.write(f"  Case: {case}: {complexity} (m={m:.2f})\n")

    # Plotting results
    markers = {'quickselect': 'o', 'sortselect': 's'}
    colors = {'quickselect': 'blue', 'sortselect': 'orange'}
    k_values_to_plot = range(20, 100, 15)

    plt.figure(figsize=(10, 6))
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xscale("log")
    plt.xlabel("List Size", fontsize=12)
    plt.ylabel("Run Time (s)", fontsize=12)
    plt.title("Comparison of Quickselect vs Sortselect by List Size")

    for algo_name, cases in benchmark_results.items():
        for case, results in cases.items():
            df = pd.DataFrame(results)
            if df.empty:
                continue
            size_results = df.groupby('size').mean().reset_index()
            plt.plot(size_results['size'], size_results['time'], label=f"{algo_name} - {case}",
                     marker=markers[algo_name], linestyle='-', linewidth=1.5)

    plt.legend(title="Algorithm")
    plt.ylim(bottom=0)
    plt.savefig("benchmark_results_list_size.png")

    plt.figure(figsize=(10, 6))
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlabel("k Value", fontsize=12)
    plt.ylabel("Run Time (s)", fontsize=12)
    plt.title("Comparison of Quickselect vs Sortselect by k Value")

    for algo_name, cases in benchmark_results.items():
        for case, results in cases.items():
            df = pd.DataFrame(results)
            if df.empty:
                continue
            k_results = df.groupby('k_value').mean().reset_index()
            plt.plot(k_results['k_value'], k_results['time'], label=f"{algo_name} - {case}",
                     marker=markers[algo_name], linestyle='-', linewidth=1.5)

    plt.legend(title="Algorithm")
    plt.ylim(bottom=0)
    plt.savefig("benchmark_results_k_value.png")
