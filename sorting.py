import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header,value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data
def selection_sort(seznam):
    minimum = seznam[0]
    for i in range(seznam[1]):
        if seznam[i]<seznam[0]:
            seznam

def main():
    my_data = read_data("numbers.csv")
    print(my_data["series_3"])

def bubble_sort(seznam):
    # loop to access each array element
    for i in range(len(seznam)):

        # loop to compare array elements
        for j in range(0, len(seznam) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if seznam[j] > seznam[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = seznam[j]
                seznam[j] = seznam[j + 1]
                seznam[j + 1] = temp

if __name__ == '__main__':
    main()
