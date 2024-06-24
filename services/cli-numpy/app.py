import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def calculate_sum(numbers):
    array = np.array(numbers)
    result = np.sum(array)
    return result.item()

def plot_data(numbers, output_file):
    array = np.array(numbers)

    plt.figure()
    plt.plot(array)

    plt.title('Plot of the provided numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')

    plt.savefig(output_file)
    plt.close()

def main():
    parser = argparse.ArgumentParser(description='Process some numbers.')
    parser.add_argument('action', choices=['sum', 'plot'], help='Action to perform: sum or plot')
    parser.add_argument('numbers', nargs='+', type=float, help='List of numbers')
    parser.add_argument('--output', '-o', type=str, help='Output file for the plot (required for plot action)')

    args = parser.parse_args()

    if args.action == 'sum':
        result = calculate_sum(args.numbers)
        print(f"Sum of the array: {result}")

    elif args.action == 'plot':
        if not args.output:
            default_output = os.path.join('/numpyResults', 'default_plot.png')
            print(f"No output file specified, using default: {default_output}")
            args.output = default_output
        plot_data(args.numbers, args.output)
        print(f"Plot saved to {args.output}")

    # Infinite loop to keep the container running
    while True:
        pass

if __name__ == '__main__':
    main()