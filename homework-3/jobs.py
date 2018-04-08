"""
CSCI-665-01 Homework-3(jobs.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input the different intervals i.e.
 the different start and end times and the job
 number it is associated to (0 or 1) and gives the output the total
 number of jobs that can be scheduled

 Usage: python3 jobs.py
 n
 start finish employee
"""
class Job:
    '''
     Class Job will store start and finish time values for every job.
     '''
    __slots__ = "start","finish"
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish


class Job:
    '''
     Class Job will store start and finish time values for every job.
     '''
    __slots__ = "start","finish"
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish


def init(jobs_0,jobs_1):
    """  Function to sort according to finish time.
        @:param  jobs_0: list of times of job 0
        @:param  jobs_1: list of times of job 1

    """
    jobs_1 = sorted(jobs_1, key = lambda i: i.finish)
    jobs_0 = sorted(jobs_0, key = lambda i: i.finish)


    if (jobs_0[0].start < jobs_1[0].start):
        start_scheduling(jobs_0, jobs_1)
    else:
        start_scheduling(jobs_1, jobs_0)


def start_scheduling(jobs_0,jobs_1):
    """  Function to schedule according to the start and end times.
    This will run in O(n)as each list will be visited only once
               @:param  jobs_0: list of times of job 0
               @:param  jobs_1: list of times of job 1
               @return count: max number of jobs that can be scheduled
    """
    index_0 = 0
    index_1 = 0
    count = 1
    flag = 0

    while (index_0 < len(jobs_0) and index_1 < len(jobs_1)):
        if (flag == 0):
            finish_time = jobs_0[index_0].finish
            while (index_1 < len(jobs_1)):
                start_time = jobs_1[index_1].start
                if (start_time >= finish_time):
                    count = count + 1
                    break
                index_1 += 1
            flag = 1
        else:
            finish_time = jobs_1[index_1].finish
            while (index_0 < len(jobs_0)):
                start_time = jobs_0[index_0].start
                if (start_time >= finish_time):
                    count = count + 1
                    break
                index_0 += 1

            flag = 0
    print(count)


def main():
    """  Main Function to  take inputs and put it in array.
    """
    n = int(input())
    jobs_0 = []
    jobs_1 = []
    for i in range(n):
        start,finish,employee = [int(x) for x in input().split(" ")]
        if employee == 0:
            jobs_0.append(Job(start,finish))
        elif employee == 1:
            jobs_1.append(Job(start,finish))
    init(jobs_0,jobs_1)




if __name__ == '__main__':
    main()