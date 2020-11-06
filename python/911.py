# https://leetcode.com/problems/online-election/
# it is to use a lead to know what is the current winning and insert it into the result, then use a binary search to get the reuslt. Here I use binary search right, to get the position on right, then minus 1, in case the number exist

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.result = defaultdict(int)
        self.times = times
        N = len(persons)
        self.result2 = [-1] *N
        lead = -1
        for i in range(N):
            self.result[persons[i]] += 1
            if  self.result[persons[i]] >= self.result[lead]:
                lead = persons[i]         
            self.result2[i] = lead

    def q(self, t: int) -> int:
        index = bisect.bisect_right (self.times, t)
        return self.result2[index - 1]
        
