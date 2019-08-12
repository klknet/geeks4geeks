"""
Calculate the angle between hour hand and minute hand.
"""


def clock_angle(h, m):
    h = h % 12
    m = m % 60
    h_angle = (h * 60 + m) * 0.5
    m_angle = m * 6
    diff = int(abs(h_angle - m_angle))
    return min(diff, 360 - diff)


print(clock_angle(12, 30))
print(clock_angle(9, 60))
print(clock_angle(3, 30))
print(clock_angle(6, 0))
print(clock_angle(12, 0))
