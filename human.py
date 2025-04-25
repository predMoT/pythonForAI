class Human:
    def __init__(self, name):  # This is the constructor method.
        self.name = name
        print("bir human instance oluşturuldu.")
    def __str__(self):
        return f"STR fonksiyonuna dönen değer" (self.name)    
    def talk(self, message):
        print(f'{self.name} says: {message}')
    def walk(self):
        print(f'{self.name} is walking.')
