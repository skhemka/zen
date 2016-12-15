from icalendar import Calendar, vDatetime
from datetime import datetime


class CalendarParser:

    def __init__(self, file_path):
        self.file_path = file_path
        self.calendar_events = []
        self.parse_and_store_calendar()

    def parse_and_store_calendar(self):
        f = open(self.file_path, 'rb')
        gcal = Calendar.from_ical(f.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                temp_start = component.get("dtstart").dt
                temp_end = component.get("dtend").dt
                self.calendar_events.append((temp_start, temp_end))
        f.close()

    def check_event_availability(self, event_start, event_end):
        for start, end in self.calendar_events:
            if event_start <= start < event_end:
                return False
            elif event_start >= start and event_end <= end:
                return False
            elif event_start < end <= event_end:
                return False
        return True


def main():
    c = CalendarParser("/Users/Derek/Desktop/Courses.ics")
    print c.calendar_events
    print(c.check_event_availability(datetime(2016,1,11,15,0), datetime(2016,1,11,15,10)))
    print datetime(2016,1,11,15,0).time()

if __name__ == '__main__':
    main()
