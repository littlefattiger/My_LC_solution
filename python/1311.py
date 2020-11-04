# https://leetcode.com/problems/get-watched-videos-by-your-friends/
# using hash table to check bfs to avoid go back to privious path
# bfs is a good choice to reach level k

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        seen = set()
        seen.add(id)
        cnt = 0
        queue = [id]
        
        while queue and cnt <level:
            temp = []
            for i in queue:
                for friend in friends[i]:
                    if friend not in seen:
                        seen.add(friend)
                        temp.append(friend)
            queue = temp
            cnt += 1
        watch = defaultdict(int)
        for node in queue:
            for movie in watchedVideos[node]:
                watch[movie] += 1
        res = list(watch.items())
        res.sort(key = lambda x: (x[1], x[0]))
        res2 = []
        for r in res:
            res2.append(r[0])
        return res2
            
