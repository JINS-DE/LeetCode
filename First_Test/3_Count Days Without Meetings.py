class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meeting_days = 0
        meetings.sort()
        now_meeting=meetings[0]

        for i in range(1,len(meetings)):
            if now_meeting[1] >= meetings[i][0]:
                now_meeting[1]=max(now_meeting[1],meetings[i][1])
            else:
                meeting_days += now_meeting[1]-now_meeting[0] + 1
                now_meeting = meetings[i]

        meeting_days += now_meeting[1]-now_meeting[0] + 1
        return days-meeting_days