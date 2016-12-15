from google_sheet_handler import GoogleSheetHandler
from calendar_parser import CalendarParser
from datetime import datetime


class ScheduleHandler:

    def __init__(self):
        self.google_sheet_handler = GoogleSheetHandler()
        self.calendar_parser = None

    def set_calendar(self, filepath):
        self.calendar_parser = CalendarParser(filepath)

    def process_sheet_content(self, in_id, out_id):
        self.google_sheet_handler.read_sheet(in_id)
        content = self.google_sheet_handler.content_list
        data = []
        for row in content:
            start = row[2]
            end = row[3]
            rdt = datetime(2016,1,11,15,0) # THIS NEEDS TO BE CHANGED
            time_readable = rdt.strftime("%I:%M %p")
            date = rdt.strftime("%B %d, %Y")
            data.append([
                row[0],
                row[1],
                time_readable,
                date,
                row[4],
                row[5]
            ])
            if self.calendar_parser:
                if self.calendar_parser.check_event_availability(start, end):
                    self.google_sheet_handler.write_sheet(out_id, data)
            else:
                self.google_sheet_handler.write_sheet(out_id, data)


def main():
    sh = ScheduleHandler()
    sh.process_sheet_content("1CAqx8xH81opQ1jJsa2a_dY8hzbWPG9kouUIvQWROM3I", "1nb5wKk78xEReSKxjw6P0pe_tCRqhwh6-krjqpkuAVX4")

if __name__ == '__main__':
    main()
