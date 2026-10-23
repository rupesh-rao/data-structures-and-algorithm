from heapq import heappush, heappop

# http://takeuforward.org/practice/dsa/meeting-rooms-ii
# Time: O(NlogN), Space: O(N)
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort based on start time
        intervals.sort()
        # for storing end times in min heap
        endings = []
        n = len(intervals)
        # max room needed
        needed = 0
        for i in range(n):
            # if the current meeting starts after the minimum ending of a meetings
            if endings and intervals[i][0] >= endings[0]:
                # remove the minimum ending meeting, so that new meeting can take its place
                heappop(endings)
            # add the current meeting's ending time
            heappush(endings, intervals[i][1])
            # max rooms needed at any given point of time
            needed = max(needed, len(endings))
        return needed


