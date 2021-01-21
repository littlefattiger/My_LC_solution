class Solution:
    def exclusiveTime(self, n: int, logs):
        stack = []
        time_spend = [0] * n
        last_time = 0
        for log in logs:
            process, typeOfAction, time = log.split(':')
            process, time = int(process), int(time)
             
            if   stack:
                time_spend[stack[-1]] += time - last_time
            last_time = time
            if typeOfAction == 'start':
                stack.append(process)
                
            else:
                p = stack.pop()
                time_spend[p] += 1
                last_time += 1
        return time_spend
    def inclusiveTime(self, n: int, logs):
        stack = []
        time_spend = [0] * n
         
        for log in logs:
            process, typeOfAction, time = log.split(':')
            process, time = int(process), int(time)
             
             
            if typeOfAction == 'start':
                stack.append((process, time))
                
            else:
                p, t = stack.pop()
                time_spend[p] += time + 1 - t
                
        return time_spend
s = Solution()

print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(s.inclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
