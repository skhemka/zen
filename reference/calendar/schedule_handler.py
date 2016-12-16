from google_sheet_handler import GoogleSheetHandler
from calendar_parser import CalendarParser
from datetime import datetime, date
import pytz


class ScheduleHandler:

    def __init__(self):
        self.google_sheet_handler = GoogleSheetHandler()
        self.calendar_parser = None

    def set_calendar(self, filepath):
        self.calendar_parser = CalendarParser(filepath)

    @staticmethod
    def parse_date_and_time(tdate, ttime):
        new_time = ttime.replace(" ", "")
        split_time = new_time.split("-")
        start_time = datetime.strptime(split_time[0], "%I:%M%p").time().replace(tzinfo=pytz.timezone('UTC'))
        end_time = datetime.strptime(split_time[1], "%I:%M%p").time().replace(tzinfo=pytz.timezone('UTC'))
        if tdate == "Today":
            new_date = datetime(2016, 12, 15).date()
        else:
            new_date = datetime.strptime(tdate, "%b %d, %Y").date()
        return datetime.combine(new_date, start_time), datetime.combine(new_date, end_time)

    def process_sheet_content(self, in_id, out_id):
        self.google_sheet_handler.read_sheet(in_id)
        content = self.google_sheet_handler.content_list
        data = []
        for row in content:
            start, end = ScheduleHandler.parse_date_and_time(row[3], row[2])
            data.append([
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            ])
            if self.calendar_parser:
                if self.calendar_parser.check_event_availability(start, end):
                    print(self.calendar_parser.check_event_availability(start, end))
                    self.google_sheet_handler.write_sheet(out_id, data)
            else:
                self.google_sheet_handler.write_sheet(out_id, data)


def main():
    sh = ScheduleHandler()
    sh.set_calendar("Test_1.ics")
    sh.process_sheet_content("1nb5wKk78xEReSKxjw6P0pe_tCRqhwh6-krjqpkuAVX4",
                             "1CAqx8xH81opQ1jJsa2a_dY8hzbWPG9kouUIvQWROM3I")

if __name__ == '__main__':
    main()
