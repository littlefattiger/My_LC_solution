
# if it is start, enter the stack, else pop up. we can calculate the time spend before. Only start would be in the stack
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
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
