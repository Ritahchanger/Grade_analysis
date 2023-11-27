import matplotlib.pyplot as plt
import statistics

# Define the Student class to manage individual student data and actions
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    # Method to calculate and display the average grade
    def getAverageGrade(self):
        try:
            totalGrades = []
            for subjectGrades in self.grades.values():
                totalGrades.extend(subjectGrades)
            average = sum(totalGrades) / len(totalGrades)
            print(f"{self.name} - Average Grade: {average:.2f}")
        except ZeroDivisionError:
            print(f"{self.name} has no grades.")

    # Method to find and display the highest grade in a subject
    def getHighestGrade(self, subject):
        try:
            highest = max([self.grades.get(subject, 0)])  # Convert to list for iterable
            print(f"Highest grade in {subject}: {highest}")
        except ValueError:
            print("No grades found for the given subject.")

    # Method to find and display the lowest grade in a subject
    def getLowestGrade(self, subject):
        try:
            lowest = min([self.grades.get(subject, 100)])  # Convert to list for iterable
            print(f"Lowest grade in {subject}: {lowest}")
        except ValueError:
            print("No grades found for the given subject.")

    # Method to sort and display grades in a subject
    def sortGrades(self, subject):
        try:
            grades = self.grades.get(subject, [])
            if isinstance(grades, list):
                sortedGrades = sorted(grades)
                print(f"Sorted grades in {subject}: {sortedGrades}")
            else:
                raise TypeError(f"Grades for {subject} not in proper format.")
        except TypeError as e:
            print(e)

    # Method to calculate and display the standard deviation of grades in a subject
    def getStandardDeviation(self, subject):
        try:
            grades = self.grades.get(subject, [])
            if len(grades) >= 2:
                stdDev = statistics.stdev(grades)
                print(f"Standard deviation in {subject}: {stdDev:.2f}")
            else:
                print(f"Insufficient data to get standard deviation for {subject}")
        except statistics.StatisticsError as e:
            print(e)

    # Method to calculate and display the variance of grades in a subject
    def getVariance(self, subject):
        try:
            grades = self.grades.get(subject, [])
            if len(grades) >= 2:
                variance = statistics.variance(grades)
                print(f"Variance in {subject}: {variance:.2f}")
            else:
                print(f"Insufficient data to get variance for {subject}")
        except statistics.StatisticsError as e:
            print(e)

    # Method to visualize grades using different plots
    def visualizeGrades(self, subject, visualizationType):
        try:
            grades = self.grades.get(subject, [])
            if isinstance(grades, list):
                visualizationOptions = {
                    'histogram': self.plotHistogram,
                    'boxplot': self.plotBoxplot,
                    'lineplot': self.plotLineplot
                }
                selectedVisualization = visualizationOptions.get(visualizationType.lower())
                if selectedVisualization:
                    selectedVisualization(grades, subject)
                else:
                    print("Invalid visualization type selected.")
            else:
                raise TypeError(f"Grades for {subject} not in proper format.")
        except TypeError as e:
            print(e)

    # Method to plot a histogram
    def plotHistogram(self, grades, subject):
        plt.figure(figsize=(8, 6))
        plt.hist(grades, bins=10, color='skyblue', edgecolor='black')
        plt.title(f'Grade Distribution in {subject}', fontsize=16, fontweight='bold')
        plt.xlabel('Grades', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.show()

    # Method to plot a boxplot
    def plotBoxplot(self, grades, subject):
        plt.figure(figsize=(8, 6))
        plt.boxplot(grades, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
        plt.title(f'Boxplot of Grades in {subject}', fontsize=16, fontweight='bold')
        plt.xlabel('Subjects', fontsize=12)
        plt.ylabel('Grades', fontsize=12)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.show()

    # Method to plot a line plot
    def plotLineplot(self, grades, subject):
        plt.figure(figsize=(8, 6))
        plt.plot(grades, marker='o', color='orange', linestyle='-', linewidth=2, markersize=8)
        plt.title(f'Lineplot of Grades in {subject}', fontsize=16, fontweight='bold')
        plt.xlabel('Index', fontsize=12)
        plt.ylabel('Grades', fontsize=12)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.show()


# Define the GradeAnalyzer class to perform analysis on a group of students
class GradeAnalyzer:
    @staticmethod
    def getClassAverages(students):
        all_subjects = set()
        all_grades = {subject: [] for student in students for subject in student.grades}

        for student in students:
            all_subjects.update(student.grades.keys())
            for subject, grades in student.grades.items():
                all_grades[subject].extend(grades)

        for subject in all_subjects:
            total_grades = sum(all_grades[subject])
            subject_avg = total_grades / len(all_grades[subject])
            print(f"Average for {subject}: {subject_avg:.2f}")
    def getOverallClassAverage(students):
        all_grades = [grade for student in students for grades in student.grades.values() for grade in grades]
        total_grades = sum(all_grades)
        overall_average = total_grades / len(all_grades)
        print(f"Overall class average: {overall_average:.2f}")
      
# Corrected student data structure
student_data = [
    {"name": "Alice", "grades": {"math": [85], "science": [90], "history": [78]}},
    {"name": "Bob", "grades": {"math": [90], "science": [88], "history": [92]}},
    {"name": "Charlie", "grades": {"math": [80], "science": [85], "history": [88]}}
]


# Create instances of students using provided data
students = []
for data in student_data:
    name = data["name"]
    grades = data["grades"]
    student = Student(name, grades)
    students.append(student)

# Display information
def displaySummaryGraphOrText():
    choice = input("WOULD LIKE TO SEE STUDENTS GRADES ANALYSIS GRAPHICALLY ?(yes/no): ").lower()
    
    if choice == "yes":
        # Code for displaying styled graphs
        for student in students:
            # Perform actions for styled graphs (e.g., visualizations)
            student.visualizeGrades("math", "histogram")  # Replace with appropriate visualization
        
        GradeAnalyzer.getClassAverages(students)
        GradeAnalyzer.getOverallClassAverage(students)
    else:
        # Display the data in textual form
        for student in students:
            student.getAverageGrade()
            student.getHighestGrade("math")
            student.getLowestGrade("science")
            student.sortGrades("history")
            student.getStandardDeviation("science")
            student.getVariance("math")
        
        GradeAnalyzer.getClassAverages(students)
        GradeAnalyzer.getOverallClassAverage(students)

# Call the function to initiate the display based on user preference
displaySummaryGraphOrText()