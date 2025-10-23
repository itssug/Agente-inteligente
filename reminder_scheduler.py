# reminder_scheduler.py
from datetime import datetime
import uuid

class ReminderScheduler:
    def __init__(self):
        self.reminders = []

    def schedule(self, when, message, destinatario):
        rid = str(uuid.uuid4())
        self.reminders.append({'id': rid, 'when': when, 'message': message, 'dest': destinatario})
        return rid

    def due(self, now=None):
        now = now or datetime.utcnow()
        due = [r for r in self.reminders if r['when'] <= now]
        self.reminders = [r for r in self.reminders if r['when'] > now]
        return due
