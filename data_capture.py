class FenwickTree:
    """
    Class to represent a FenwickTree
    """
    def __init__(self, size: int) -> None:
        """
        Create a FenwickTree with a fixed size
        :return: (None)
        """
        self.tree: list[int] = [0] * (size + 1)

    def update(self, idx: int) -> None:
        """
        Updates the Fenwick tree with the given value
        :param idx: index at which the update is to be made
        :return: None
        """
        while idx < len(self.tree):
            self.tree[idx] += 1
            idx += idx & -idx

    def query(self, idx: int) -> int:
        """
        Calculate the amount of the elements until the index
        :param idx: index until which the sum is calculated
        :return: (int)
        """
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result

class DataCapture:
    """
    Class to represent a DataCapture
    """
    LENGHT = 1000

    def __init__(self) -> None:
        """
        Create a DataCapture with a internal FenwickTree with a fixed length
        :return: (None)
        """
        self.num_counts = FenwickTree(self.LENGHT)
        self.total_count = 0

    def add(self, num: int) -> None:
        """
        Add a element to the internal tree, and increse the total count
        :param num: num that will be added to the tree
        :return: (None)
        """
        if num > 0  and num <= self.LENGHT:
            self.total_count += 1
            self.num_counts.update(num)
        else:
            raise ValueError(
                f"The value added to the DataCapture has to be a small integer between 0 and {self.LENGHT}")

    def build_stats(self) -> 'Stats':
        """
        Create a object Stats for calculating the variables related to a index
        :return: (Stats)
        """
        return Stats(self)


class Stats:
    """
    Class to represent a Stats of a DataCapture
    """
    def __init__(self, data_capture: DataCapture) -> None:
        """
        Create a Statis with a DataCapture related
        :return: (None)
        """
        self.data_capture = data_capture

    def less(self, value: int) -> int:
        """
        Return the amount of the elements lowers than the value
        :return: (int)
        """
        return self.data_capture.num_counts.query(value-1)

    def greater(self, value: int) -> int:
        """
        Return the amount of the elements greater than the value
        :return: (int)
        """
        return self.data_capture.total_count - self.less(value+1)

    def between(self, low: int, high: int) -> int:
        """
        Return the amount of the elements lower than the first element and
        greater than the second one
        :return: (int)
        """
        return self.less(high+1) - self.less(low - 1) if low > 0 else self.less(high+1)
