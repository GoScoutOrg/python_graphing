import matplotlib.pyplot as plt
import sys


def read_file(filename):
    output = []
    f = open(filename)

    for line in f.readlines():
        split_line = line.split()
        output.append([split_line[0], split_line[1], split_line[2]])

    f.close()
    return output


def main():
    data = read_file(sys.argv[1])
    x = [int(x[0]) for x in data]
    y1 = [int(x[1]) for x in data]
    y2 = [int(x[2]) for x in data]
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.title('Transient-Response Analysis')
    plt.xlabel('Time(ticks)')
    plt.ylabel('Position')
    plt.legend(('Unit-Step Response',), loc=0)
    # plt.xlim(xmax=max(data_x))
    plt.grid()
    plt.show()
    # plt.plot(x, y)
    # plt.title("Simple Plot")
    # plt.ylabel("y-axis")
    # plt.xlabel("x-axis")
    # plt.show()


if __name__ == "__main__":
    main()
