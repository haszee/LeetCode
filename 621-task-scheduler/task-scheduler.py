class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        totaljobs = len(tasks)
        frequency = {}
        
        for task in tasks:
            if task in frequency:
                frequency[task] += 1
            else:
                frequency[task] = 1

        max_frequency = sorted(frequency.values())

        num_tasks_frequent = len([num for num in max_frequency if num == max_frequency[-1]])
    
        return max((n+1)*(max_frequency[-1]-1)+num_tasks_frequent,totaljobs)
