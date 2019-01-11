def get_shingles(document, n=4):
    """ Generates n-shingles (n-grams) given a document """

    # The split function splits on whitespace
    split_document = document.split()

    # Shingles are easily made using list comprehension
    # Lists are not hashable so tuples are returned instead
    shingles = [tuple(split_document[i:i+n]) for i in range(len(split_document) - n + 1)]

    return shingles


def get_supershingles(sketch, hashing_function=hash, k=6):
    """
        Group list of shingles (sketch) into groups of k non-overlapping elements
        In the same step, the groups are hashed according to the specified hashing algorithm
    """
    if len(sketch) % k != 0:
        raise RuntimeError('Sketch size should be divisible by k')

    return [hashing_function(tuple(sketch[i:i+k])) for i in range(0, len(sketch), k)]


if __name__ == "__main__":
    print(get_shingles('This is a test of how shingles work', 4))
