import numpy
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    matrix = numpy.array(list(csv.reader(open("test.csv", "rb"), delimiter=","))).astype("float")


    return matrix

