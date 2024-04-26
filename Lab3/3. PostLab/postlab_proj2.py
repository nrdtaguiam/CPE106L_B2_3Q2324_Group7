import random
class Student(object):

    def __init__(self, name, number):

        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def getName(self):
        return self.name 

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
         return max(self.scores)

    def __eq__(self,student):
        return self.name == student.name

    def __ge__(self,student):
        return self.name == student.name or self.name>student.name

 
    def __lt__(self,student):
        return self.name<student.name

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
            " ".join(map(str, self.scores))

 
def main():
    """A simple test."""
    students = [
        Student("Neal", 4),
        Student("Paulo", 3),
        Student("Ju Hyoung", 4),
        Student("Paolo", 5),
        Student("Kathryna", 2),
    ]
    print("Unsorted students:")
    for student in students:
        print(student)
    
    random.shuffle(students)
    print("\nShuffled students:")
    for student in students:
        print(student)
    
    students.sort()
    print("\nSorted students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()