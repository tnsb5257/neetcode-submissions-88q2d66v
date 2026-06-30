class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp={}
        for task in tasks:
            mp[task]=mp.get(task,0)+1
        max_freq_tasks = 0
        max_freq=-float("inf")
        for task,freq in mp.items():
            if freq==max_freq:
                max_freq_tasks+=1
            elif freq>max_freq:
                max_freq=freq
                max_freq_tasks=1
        return max((max_freq-1)*(n+1)+max_freq_tasks,len(tasks))