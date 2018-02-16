# implementation by @kaba_y, https://korogba.github.io
from utils.file_operations import convert_file_to_jobs


def weighted_completion_time(file_path, is_score_quotient) -> int:
    """Use either the difference or the ratio(depending on is_score_quotient) between weight and length as the score"""
    jobs = convert_file_to_jobs(file_path, is_score_quotient)

    jobs[0].completion_time = jobs[0].length
    completion_time = jobs[0].weight * jobs[0].length

    for i in range(1, len(jobs)):
        jobs[i].completion_time = jobs[i].length + jobs[i - 1].completion_time
        completion_time += (jobs[i].completion_time * jobs[i].weight)

    return completion_time
