class dog: 
    def __init__(self, name, alter): 
        self.name = name 
        self.age = alter
        self.energy = 100 # Attribut für Energie

    def __str__(self): 
        return f"{self.name} ist {self.age} Jahre alt und hat noch {self.energy} Energie."
        
    def bark(self): 
        if self.energy > 0:
            self.energy -= 10
            return(f"{self.name} barks.") # Erstellen eines Objekts der Klasse Hund 
        else:
            return(f"{self.name} is too tired to bark.")

    def nap(self): 
        self.energy += 10
        return(f"{self.name} is taking a nap...")

    def feed(self):         
        self.energy += 50
        if self.energy > 100:
            self.energy = 100
        return(f"{self.name} is eating.")