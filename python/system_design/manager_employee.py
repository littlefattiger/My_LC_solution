# 2nd Q) 
# 
# Suppose you are implementing a really basic "corporate scoring system". Each employee has a score. Employees may have managers. Managers have their own score as well as a score that represents the average of those underneath them.
# 
# Provide a class / object definition for employees and managers.
# Define a way to "store" them into some sort of data structure; say which one you chose and why.
# Define an alogirthem to look up the "scores" of any employee.

class employee():
    def __init__(self, id, score, isManager,supervise):
        self.id = id
        self.score = score
        self.isManager = isManager
        self.Supervise = supervise
        self.direct_report = dict()
        self.average_score_direct_report = 0
        
    
    def getScore_direct_report(self):
        if self.isManager == False:
            return (self.score,1)
        
        cnt = 1
        tot_scorer = self.score
        
        for v in self.direct_report:
            direct_report_score, tot_direct_rreport = v.getScore_direct_report()
            tot_scorer += direct_report_score
            cnt += tot_direct_rreport
        return tot_scorer, cnt
    
    def get_average_score_direct_report(self):
        
        tot_score , tot_people = self.getScore_direct_report()
        if tot_people == 1:
            return 0 
        tot_score -= self.score
        tot_people -= 1
        return tot_score/tot_people
