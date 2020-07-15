"""
Given two numbers, hour and minutes.
Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        hour_angle = (30 * hour) + (0.5 * minutes)
        minute_angle = (6 * minutes)
        ang = abs(minute_angle - hour_angle)
        return min(360 - ang, ang)


if __name__ == "__main__":
    hour = 12
    minutes = 30
    print(Solution().angleClock(hour, minutes))