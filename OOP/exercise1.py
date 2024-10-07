class Student:
    def __init__(self, name, age, tribe):
        self.name = name
        self.age = age
        self.tribe = tribe

    def display_info(self):
        naming = f"My name is {self.name}, I am {self.age} years old and I belong to the {self.tribe}."
        return naming

    def play_games(self):
        print(f"Since I am {self.tribe}, I like to play Chess.")

# student1 = Student("Angie", 23, "Kikuyu")
# student1.play_games()

student2 = Student("Mary", 25, "Kalenjin")
print(student2.display_info())

student2.play_games()