class Plant:
    def __init__(self, name, height, age):
        self.name = name;
        self.height = height;
        self.ageDays = age;
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.ageDays} days old")
    def grow(self):
        heightByDay = self.height / self.ageDays
        self.height = round(self.height + heightByDay, 1)
        self.ageDays += 1
    def age(self):
        startHeight = self.height
        print("=== Garden Plant Growth")
        self.show()
        for x in range(7):
            print(f"=== Day {x + 1} ===")
            self.grow()
            self.show()
        print(f"Growth this week: {round(self.height - startHeight,1)}cm")
    

def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.age()

if __name__ == "__main__":
    main()