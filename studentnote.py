from typing_extensions import Self


class Student():
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def passnote(self):
        if self.score >=8:
            return (f"{self.name} has  {self.score}, {self.name} has pass")
        else:
            return(f"{self.name} has  {self.score}, {self.name} has not pass")

Pedro =(Student("Pedro", 3))
Lucia =(Student("Lucia", 8))

note = print(str(Pedro.passnote()))
note = print(Lucia.passnote())

