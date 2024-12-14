class Interval():
    def __init__(self,start,end):
        self.start=start
        self.end=end

    @staticmethod
    def canAttendMeetins(self):
        intervals.sort(key=lambda i : i.start)

        for i in range(1,len(intervals)):
            # prin t(intervals[i-1])
            i1=intervals[i-1]
            i2=intervals[i]

            if i1.end > i2.start:
                return False
        return True

# class MeetingScheduler():
#     def __init__(self,intervals):
#         self.intervals=[Interval(start,end) for start,end in intervals]
        
#     def canAttendMeetins(self):
#         self.intervals.sort(key=lambda i : i.start)

#         for i in range(1,len(self.intervals)):
#             # print(intervals[i-1])
#             i1=self.intervals[i-1]
#             i2=self.intervals[i]

#             if i1.end > i2.start:
#                 return False
#         return True


intervals= [Interval(0,30),Interval(5,10),Interval(15,20)]
canAttend=Interval.canAttendMeetins(intervals)
# intervals = [[0, 30], [5, 10], [15, 20]]
# scheduler=MeetingScheduler(intervals)
# canAttend=scheduler.canAttendMeetins()
print(canAttend)
