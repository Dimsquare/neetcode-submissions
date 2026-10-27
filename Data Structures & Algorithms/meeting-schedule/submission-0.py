"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sint = sorted(intervals, key=lambda i: i.start)
        current_max=0
        for interval in sint:
            if current_max>interval.start:
                return False
            if interval.end>current_max:
                current_max=interval.end

        return True

