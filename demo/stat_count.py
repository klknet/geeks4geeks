import datetime
import sys

import pymysql


class MessageStat(object):
    def __init__(self, date, total=0, meeting_count=0):
        self.date = date
        self.total = total
        self.meeting_count = meeting_count

    def __str__(self):
        return str(self.date) + "\t" + str(self.total) + "\t" + str(self.meeting_count)


def connection():
    host = sys.argv[1]
    user = sys.argv[2]
    pwd = sys.argv[3]
    db = sys.argv[4]
    mydb = pymysql.connect(host, user, pwd, db)
    return mydb.cursor()


def count_stat(n):
    if n < 0:
        return
    cursor = connection()
    sql = """
    select count(1) from im_message where sendtime between %s and %s
    """
    sql2 = """
    SELECT
        count(meeting_id), meeting_id
    FROM
        im_message
    WHERE
        sendtime BETWEEN %s
    AND %s
    group by meeting_id
    ORDER BY
        count(meeting_id) DESC;
    """
    res = []
    for i in range(n - 1, -1, -1):
        prev = datetime.datetime.now() - datetime.timedelta(i)
        date = prev.strftime("%Y-%m-%d")
        msg_stat = MessageStat(date)
        begin = prev.strftime("%Y-%m-%d 00:00:00")
        end = prev.strftime("%Y-%m-%d 23:59:59")
        cursor.execute(sql, (begin, end))
        result = cursor.fetchone()
        msg_stat.total = result[0]
        cursor.execute(sql2, (begin, end))
        result = cursor.fetchone()
        msg_stat.meeting_count = result[0]
        res.append(msg_stat)
    cursor.close()
    return res


if __name__ == "__main__":
    for msg in count_stat(10):
        print(msg)
