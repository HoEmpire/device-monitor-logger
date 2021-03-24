class Span():
    def __init__(self, name, loginfo_start, loginfo_end):
        self.name = name
        self.loginfo_start = loginfo_start
        self.loginfo_end = loginfo_end

    def report(self):
        output=""
        output+=(self.loginfo_start.time +" to "+self.loginfo_end.time+"  ")
        output+=(self.name.replace(" ","-") + " " * (40-len(self.name)))
        output+=((self.loginfo_end.time_split-self.loginfo_start.time_split).get_span())
        print(output)
        return output

class LogInfo():
    def __init__(self, time, time_split, info):
        self.time = time
        self.time_split = time_split
        self.info = info

    def print(self):
        print(self.time + ' ' + self.info)


class Date():
    def __init__(self, time):
        [time_ymd, time_hms] = time.split(':')
        time_ymd_list = time_ymd.split("-")
        time_hms_list = time_hms.split(".")
        self.month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.year = int(time_ymd_list[0])
        self.month = int(time_ymd_list[1])
        self.day = int(time_ymd_list[2])
        self.hour = int(time_hms_list[0])
        self.minute = int(time_hms_list[1])
        self.second = int(time_hms_list[2])

    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        day = self.day - other.day

        hour = self.hour - other.hour
        minute = self.minute - other.minute
        second = self.second - other.second

        if (second < 0):
            second += 60
            minute -= 1

        if (minute < 0):
            minute += 60
            hour -= 1

        if (hour < 0):
            hour += 24
            day -= 1

        if (day < 0):
            day += self.month_day[other.month - 1]
            month -= 1

        if (month < 0):
            month += 12
            year -= 1

        return (Date(
            str(year) + "-" + str(month) + "-" + str(day) + ":" + str(hour) +
            "." + str(minute) + "." + str(second)))

    def get_span(self):
        output = ""
        if (self.year > 0):
            output += (str(self.year) + " year ")

        if (self.month > 0):
            output += (str(self.month) + " month ")

        if (self.day > 0):
            output += (str(self.year) + " day ")

        if (self.hour > 0):
            output += (str(self.hour) + " hour ")

        if (self.minute > 0):
            output += (str(self.minute) + " minute ")

        if (self.second > 0):
            output += (str(self.second) + " second ")
        return output


class KeyWord():
    def __init__(self,keyword_list):
        self.keyword_list = keyword_list
        self.cursor = 0
        self.finish_search = False

    def update_cursor(self):
        self.cursor += 1
        if (self.cursor >= len(self.keyword_list)):
            self.finish_search = True