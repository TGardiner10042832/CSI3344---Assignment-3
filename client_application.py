
"""
CSI3344 - Assignment 3
Client Application
Group 33
Tristan Gardiner
Kayl Grau
"""

# Import Pyro4
import Pyro4

# Set Server-1 connection details
PORT = 60000
SERVER = "localhost"


class Student:
    def __init__(self, ID, fName, lName, email):
        self.ID = ID
        self.fName = fName
        self.lName = lName
        self.email = email


class NewStudent: 
    def __init__(self, ID, uCode, uScore):
         self.ID = ID
         self.uCode = []
         self.uScore = []
         

        

"""
    This is the manual entry of a student's units and their scores.
    Asks the user to enter their unit and results and returns lists of both.
    
    Must allow: 
        - Multiples of unit codes and scores.
        - Checks the user if the units and scores are correct at the end.        
        - Can only accept 16 - 30 units. (see CheckScores(UC, US))
        - Cannot have a unit with more than 3 failed attempts. (see CheckScores(UC, US))
"""
def StudentScores():

    unitCode = []
    unitScore = []

    while True:
        # Get correct input for Unit code and unit score.
        x = UCEntry()
        y = USEntry()

        #if x and y:
        if x != -1 and y != -1:
            unitCode.append(x)
            unitScore.append(y)
        else:
            break

    # Print the code for review
    for i in range(len(unitCode)):
        print("Unit Code: ", unitCode[i], "\tUnit Score: ", unitScore[i]) 

    ## If scores are not correct, re-enter values, or quit
    while True:
        correct = yesOrNo()       
        if correct == "y":
            return unitCode, unitScore
            break
        elif correct == "n":
            StudentScores()
            break
        elif correct == "q":
            print("Goodbye")
            quit()
            break
        else:
            print("Please enter y or n")



""" 
    Checks the inputted scores to see if the criteria was correct. 
"""
def CheckScores(UC, US):
    
    length = len(UC)
    fail = False

    # We can only accept 16 - 30 units (inclusively)
    if length < 16:
        print("You have only completed", length, "units.")
        fail = True
    elif length > 30:
        print("You have entered over 30 units.")
        fail = True
    
    # Cannot have a unit with more than 3 failed attempts. 
    failedUnit = []  
    for i in range(length):
        count = 0
        for j in range(length):
            if UC[i] == UC[j] and US[j] <= 50:
                count = count + 1
        if count == 3:
            if UC[i] not in failedUnit:
                failedUnit.append(UC[i])
            fail = True

    if failedUnit:
        print("You have failed",failedUnit , " 3 times")

    # If conditions aren't met, then exit program. 
    if fail == True:
        print("You currently do not qualify for honours study.")
        quit()




"""
    Entry of correct Unit code
    A unit code needs to be a string with the length of 7 characters and numbers.
    Unless it is -1, to signify that the list is complete.
"""
def UCEntry():
    
    # Loop until the desired input is acheived.
    while True:
        unitCode = input("Please enter unit code (enter -1 to finish): ")

        if len(unitCode) == 7 or unitCode == "-1":
            return unitCode
            break
        else:
            print("Please enter a valid, 7 character unit code. Or -1 to finish the list.")




"""
    Entry of a Unit score
    A unit score must be a valid number between 0-100, as a percentage.
    It must be entered without an exception when converted to a double.
    To finalise the list, -1 must be entered. 
"""
def USEntry():
    
    ## Loop until the desired input is achieved.
    while True:

        unitScore = input("Please enter unit results (enter -1 to finish): ")

        try:
            if int(unitScore) < 101 and int(unitScore) >= -1:
                return int(unitScore)
                break
            else:
                print("Please enter a valid score as a percentage (between 0 and 100).")
        except:
            print("Please enter as a valid number")




"""
    Entry of a correct Student ID
    If not an existing student, the system only requires a student number.
"""
def IDEntry():
        
        # Get an 8 digit number code and check that they are numbers. 
        while True:
            studentID = input("\nPlease enter your 8-digit student ID number. (Enter 'q' to quit)")

            if len(studentID) == 8 and studentID.isdigit():
                return studentID
            elif studentID == "q":
                quit()
            else:
                print("Incorrect input\n")


"""
    Yes or No - answers the question
    Just a simple y or n loop, return value y or n
"""                
def yesOrNo():

    while True:
        answer = input("\nPlease enter Yes(y) or No(n) (Enter q to Quit)").lower()
        if answer == "y":
            return answer
            break
        elif answer == "n":
            return answer
            break
        elif answer == "q":
            quit()
        else:
            print("Please enter y or n or q")




## Student information input
def studentInformation():

    while True:
        # Get student ID
        studentID = IDEntry()
 
        fName = input("Please enter your first name: ")
        lName = input("Please enter your last name: ")
        email = input("Please enter your student email: ")

        print("\nStudent ID: ", studentID, "\nFirst name: ", fName, "\nLast Name: ", lName, "\nEmail: ", email, "\n")

        print("Is this information correct?")
        ans = yesOrNo()

        # If y = return results. If n = loop again. If q = exit the program.
        if ans == "y":
            studentInfo = [studentID, fName, lName, email]
            return studentInfo
        elif ans == "q":
            quit()


###     Menu's      ###

# login / start menu
def login():
    
    ## Banner
    print("|-------------------------------------------------------------|")
    print("|------- Welcome to the HEPaS system for OUST students -------|")
    print("|-------------------------------------------------------------|\n")

    ## Connect to server-1 using Pyro4
    uri = "PYRO:studentCheck@"+SERVER+":"+str(PORT)
    studentCheck=Pyro4.Proxy(uri)
    

    # Check if they're existing
    print("Are you currently on the existing student database? (Former or Current)")
    ans = yesOrNo()

    if ans == "y":
        print("\nPlease enter the following information.")
        studentInfo = studentInformation()
        student = Student(studentInfo[0], studentInfo[1], studentInfo[2], studentInfo[3])

        ## This is were we verify user information with the server 
        ## and then return the unit results on the system to display on screen.
        ## Something like:
        """ # Copied from demo code for client_demo...
        print("Connecting to server... ")
        qualification = honors_Check.getQualification(studentInfo)
        """


    elif ans == "n":
        # Currently not a student on the DB, enter the information as well as their completed units and their results.
        print("\nPlease enter the following information.")
        #studentID = IDEntry()
        studentID = 12345678

        ## for manual entry of unit codes and scores.
        print("\nPlease enter your Unit Code and Mark.")
        # studentScores = StudentScores()
        # CheckScores(studentScores[0], studentScores[1])                       << only while testing
        # uCodes = studentScores[0]
        # uScores = studentScores[1]

        uCodes = ["test001", "test002", "test003", "test004", "test005",
                  "test006", "test007","test008", "test009","test010", 
                  "test011", "test012", "test0013", "test014","test015", 
                  "test016", "test017", "test0018"]
        uScores = [55, 80, 66, 77, 88, 77, 76, 78, 89, 
                   87, 84, 66, 78, 43, 88, 55, 66, 77]

        ## This is were we verify the students eligibility with the server. 
        eligibility = studentCheck.checkEligibility(uCodes, uScores)
        print(eligibility)

### Main directory
""" 
Things to do:
    - Need to create/connect to server application to get student information, top 8 units and their average. 
    - No linked list in Python and dictionary does support duplicates, currently saved as two lists of unitCode and unitScore. 
      Could create a struct or class or something... or just keep as two lists
    - SQL database, I need to DL SQL and populate.
"""
def main():

    ## Start menu / login
    login()
    

if __name__ == "__main__":
    main()


