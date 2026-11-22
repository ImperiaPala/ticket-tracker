import json
from ticket import Ticket
from helpers import logged

class TicketStorage:

    def __init__(self, filename):
        self.filename = filename
        self.tickets = []

    def save(self):
        data = []
        for s in self.tickets:
            data.append(s.to_dict())
        with open (self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        self.tickets = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                raw = json.load(f)
            for i in raw:
                self.tickets.append(Ticket.from_dict(i))
        except FileNotFoundError:
            pass

    @logged        
    def add(self, ticket):
        self.tickets.append(ticket)
        self.save()

    @logged
    def delete(self, index):
        if 0 <= index < len(self.tickets):
            self.tickets.pop(index)
            self.save()
        else:
            raise IndexError('Заявки с таким номером нет')

    def sorted_tickets(self):
        order = {'новая': 0, 'в работе': 1, 'закрыта': 2}
        return sorted(self.tickets, key=lambda t: (order[t.status], t.priority))

    def filter_by_status(self, status):
        return [t for t in self.tickets if status == t.status]

    def filter_by_priority(self, priority):
        return [t for t in self.tickets if priority == t.priority]

    @logged
    def advance(self, index):
        if 0 <= index < len(self.tickets):
            self.tickets[index].change_status()
            self.save()
        else:
            raise IndexError("Заявки с таким номером нет")











