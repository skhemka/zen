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
                temp_start = vDatetime.from_ical(component.get("dtstart"))
                temp_end = vDatetime.from_ical(component.get("dtend"))
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


