class BS:

    def __init__(self, array):

        n = len(array)
        sot = False

        while not sot:
            sot = True
            for i in range (n-1):
                if array[i] > array[i+1]:
                    swap(i,i+1,array)
                    sot = False
        print (array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


arr = [23, 25, 65, 24, 58, 69, 95, 31, 5, 7, 44, 27, 32]

res = BS(arr)

