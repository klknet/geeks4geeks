"""
Find day of the week for a given date.

Jan 1st 1 AD is a Monday in Gregorian Calendar.
Let us consider the first case which we don't have leap years, hence total number of days in each year is 365. January
has 31 days i.e 7*4+3 so the day of 1st feb will be 3 days ahead of the day on 1st January. Now February has 28 days
(excluding leap years) which is exact multiple of 7. Hence there will be no change in the month of march and it will also
be 3 days ahead of the 1st january of that respective year. Consider this pattern, If we create an array of the leading
number of days for each month then it will given us t[] = {0,3,3,6,1,4,6,2,5,0,3,5}.
Now let us look at the real case when there are leap years. Every 4 years, our calculation will gain one extra day. Except
every 100 years when it doesn't. Except every 400 years when it does. How do we put in these additional days? Well, just
add y+y/4-y/100+y/400. This adds exactly the required number of leap days. But there is a problem. the leap day is 29 Feb
and not 0 January. This means that the current year should not be counted for the leap day calculation for the first two
months. Suppose that if the month is january or february, we subtract 1 from the year. This means during this months, the
y/4 value would be the previous year and would not be counted. If we subtract 1 from the t[] values of every month after
february? That would fill the gap, and the leap problem is solved. That is, we need to make the following changes.
1)t[] now becomes {0,3,2,5,0,3,5,1,4,6,2,4}
2)if m corresponds to Jan/Feb(m<3), we decrement m by 1.
3)the annual increment inside the modulus is now y+y/4-y/100+y/400 in place of y.
"""


def day_of_week(d, m, y):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    return (y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7


d, m, y = 14, 7, 2019
print(day_of_week(d, m, y))
