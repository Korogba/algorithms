# implementation by @kaba_y, https://korogba.github.io


class JobDifference:
    """Representation of Jobs to be used in scheduling.
    Uses the difference between weight and length as scores for ranking"""

    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.completion_time = float('inf')

    def __lt__(self, other) -> bool:
        assert isinstance(other, JobDifference)

        scores = self.weight - self.length
        other_scores = other.weight - other.length

        if scores != other_scores:
            return scores > other_scores
        else:
            return self.weight > other.weight


class JobQuotient:
    """Representation of Jobs to be used in scheduling.
    Uses the ratio between weight and length as scores for ranking"""

    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.completion_time = float('inf')

    def __lt__(self, other) -> bool:
        assert isinstance(other, JobQuotient)
        scores = self.weight / self.length
        other_scores = other.weight / other.length

        return scores > other_scores