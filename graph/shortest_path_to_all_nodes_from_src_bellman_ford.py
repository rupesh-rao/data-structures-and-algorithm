# https://leetcode.com/problems/network-delay-time
# Only works for Positive Weights
class Solution:
    def networkDelayTime(self, edges: list[list[int]], V: int, src: int) -> int:
        INT_MAX = int(1e9)
        dist = [INT_MAX] * (V+1)
        dist[src] = 0

        for i in range(V-1):
            for u, v, wt in edges:
                if dist[u]!=INT_MAX and dist[v] > dist[u]+wt:
                    dist[v] = dist[u] + wt

        # for i in range(V-1):
        #     for u, v, wt in edges:
        #         if dist[u]!=INT_MAX and dist[v] > dist[u]+wt:
        #             NOTE: NEGATIVE WEIGHTS PRESENT
        #

        minimum_time = max(dist[1:])
        return -1 if minimum_time==INT_MAX else minimum_time
