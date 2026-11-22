class Ticket:

    def __init__(self, title, description, priority, status='новая'):
        if not 1 <= priority <= 3:
            raise ValueError("Приоритет от 1 до 3")
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def change_status(self):
        if self.status == 'новая':
            self.status = 'в работе'
        elif self.status == 'в работе':
            self.status = 'закрыта'
        elif self.status == 'закрыта':
            raise ValueError('Заявка уже закрыта')
        else: # вылетит если статус не подходит
            raise ValueError("Неверный статус") 

    def to_dict(self):
        return {'title': self.title, 'description': self.description, 'priority': self.priority, 'status': self.status}       

    def get_data(self):
        return f'----------\n{self.title}\nОписание -- {self.description}\nПриоритет -- {self.priority}\nСтатус -- {self.status}\n'

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['description'], data['priority'], data['status'])