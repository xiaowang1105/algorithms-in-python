class Job:
    '''
    Job class has two input arguments, weight(how important) and length(how long)
    Methods:
        read_from_dict, class method, read job from a dictionary ( {index: (weight, length)...} )
        read_file, static method, process a txt file into a dictionary ( {index: (weight, length)...} )
        sort, static method, sort job list according to different operator
        completion_time, static method, calculate the weighted completion time of job list 
    '''
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
    @classmethod
    def read_from_dict(cls, job_dict):
        job_list = []
        for item in job_dict.values():
            job_list.append(cls(item[0], item[1]))
        return job_list
    @staticmethod
    def read_file(path='jobs.txt'):
        with open(path) as f:
            num_jobs = int(f.readline().strip('\n'))
            jobs = {}
            for index, item in enumerate(f.readlines()):
                item = item.strip('\n').split(' ')
                jobs[index] = list(map(int, item))
        return (num_jobs, jobs)
    @staticmethod
    def sort(job_list, method):
        if method == 'minus':
            return sorted(job_list, key=lambda job: \
                (job.weight - job.length, job.weight), reverse=True)
        elif method == 'divide':
            return sorted(job_list, key=lambda job: \
                (job.weight / job.length, job.weight), reverse=True)
        else:
            raise SyntaxError('Input Sort Method Wrong')
    @staticmethod
    def completion_time(job_list):
        completion_time = 0
        current_time = 0
        for job in job_list:
            current_time += job.length
            completion_time += current_time * job.weight
        return completion_time

def main():
    job_list = Job.read_from_dict(Job.read_file()[1])
    job_list = Job.sort(job_list, 'minus')
    print('greedy method is minus completion time: ', Job.completion_time(job_list))
    job_list = Job.sort(job_list, 'divide')
    print('greedy method is didide completion time: ', Job.completion_time(job_list))

if __name__ == '__main__':
    main()
