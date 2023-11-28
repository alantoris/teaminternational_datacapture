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
        self.num_counts = [0] * self.LENGHT
        self.total_count = 0

    def add(self, num: int) -> None:
        """
        Add a element to the internal structure, and increse the total count
        :param num: num that will be added to the array
        :return: (None)
        """
        if 0 <= num < self.LENGHT:
            self.total_count += 1
            self.num_counts[num] += 1
        else:
            raise ValueError(
                f"The value added to the DataCapture has to be a small integer between 0 and {self.LENGHT - 1}.")

    def build_stats(self) -> 'Stats':
        """
        Create a object Stats for calculating the variables related to a index
        :return: (Stats)
        """
        previous = 0
        stats = []
        for cant in self.num_counts:
            less = previous + cant
            stats.append(
                {
                    "cant": cant,
                    "less": less                 
                }
            )
            previous = less

        return Stats(self, stats)


class Stats:
    """
    Class to represent a Stats of a DataCapture
    """
    def __init__(self, data_capture: DataCapture, stats: list[dict]) -> None:
        """
        Create a Statis with a DataCapture and stats related
        :return: (None)
        """
        self.data_capture = data_capture
        self.stats = stats

    def less(self, value: int) -> int:
        """
        Return the amount of the elements lowers than the value
        :return: (int)
        """
        if 0 <= value < self.data_capture.LENGHT:
            if value == 0:
                return 0
            else:
                return self.stats[value-1]["less"]
        else:
            raise ValueError(
                f"The value to query the number of minor elements must be between 0 and {self.data_capture.LENGHT - 1}.")

    def greater(self, value: int) -> int:
        """
        Return the amount of the elements greater than the value
        :return: (int)
        """
        if 0 <= value < self.data_capture.LENGHT:
            if value == self.data_capture.LENGHT - 1:
                return 0
            else:
                return self.data_capture.total_count - self.less(value+1)
        else:
            raise ValueError(
                f"The value to query the number of greater elements must be between 0 and {self.data_capture.LENGHT - 1}.")

    def between(self, low: int, high: int) -> int:
        """
        Return the amount of the elements lower than the first element and
        greater than the second one
        :return: (int)
        """
        if high <= low:
            raise ValueError(
                f"The second argument has to be greater than the first one.")
        elif 0 <= low < self.data_capture.LENGHT or 0 <= high < self.data_capture.LENGHT:
            high_amount = self.data_capture.total_count if high == self.data_capture.LENGHT - 1 else self.less(high+1)
            low_amount = self.less(low)
            return high_amount - low_amount
        else:
            raise ValueError(
                f"The limit values to consult the number of elements in the middle must be between 0 and {self.data_capture.LENGHT - 1}.")
