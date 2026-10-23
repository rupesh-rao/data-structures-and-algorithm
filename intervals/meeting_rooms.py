# https://takeuforward.org/practice/dsa/meeting-rooms
class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):
            if intervals[i-1][1]>intervals[i][0]:
                return False

        return True