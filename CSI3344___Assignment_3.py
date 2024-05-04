
"""
CSI3344 - Assignment 3
Interface Component
Group 33
Tristan Gardiner
Kayl Grau
"""


## Works out the average of the unit scores.
## Takes a list and works out the average.
def Average(results):
    
    # Create a list of the values.
    #marks = results

    # Init
    total = 0
    gradeCounter = 0

    n = len(results)
    i = 0

    if (n == 0):
        return 0

    while results[i] != -1:
        gradeValue = results[i]
        total = total + gradeValue
        gradeCounter += 1
        i += 1

    if (gradeCounter != 0):
        average = total/gradeCounter
        return average
    else:
        return 0

"""
    Manual entry of the student unit and scores.
    Asks the user to enter their unit and results and returns list of Unit Codes and Scores.
    Must allow multiples of unit codes and scores.
    Checks if scores are correct at the end. 
"""
def StudentScores():

    unitCode = []
    unitScore = []

    while True:
        # Get correct input for Unit code and unit score.
        x = UCEntry()
        y = USEntry()

        if x and y:
            if x != -1 and y != -1:
                unitCode.append(x)
                unitScore.append(y)
                #scores[x] = y
            else:
                unitCode.append(x)
                unitScore.append(y)
                #scores[x] = y
                break

    # Print the code for review
    for i in range(len(unitCode) - 1):
        print("Unit Code: ", unitCode[i], "\tUnit Score: ", unitScore[i]) 

    ## If scores are not correct, re-enter values, or quit
    while True:
        correct = input("\nIs this correct? (y or n, or press q to Quit)")
        if correct == "y":
            return unitCode, unitScore
            break
        elif correct == "n":
            StudentScores()
            break
        elif correct == "q":
            break
        else:
            print("Please enter y or n")


"""
    Entry of correct Unit code
    A unit code needs to be a string with the length of 7 characters and numbers.
    Unless it is -1, to signify that the list is complete.
"""
def UCEntry():
    
    # Loop until the desired input is acheived.
    while True:
        unitCode = input("\nPlease enter unit code (enter -1 to finish): ")

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




## Yes or No - answers the question
## Just a simple y or n loop, return value y or n
def yesOrNo():

    while True:
        answer = input("\nPlease enter Yes(y) or No(n) (Enter q to Quit)")
        if answer == "y":
            return answer
            break
        elif answer == "n":
            return answer
            break
        elif answer == "q":
            return answer
            break
        else:
            print("Please enter y or n or q")


## Student information input
def studentInformation():

    while True:
        # Get an 8 digit number code.
        while True:
            studentID = input("\nPlease enter your 8-digit student ID number.")

            if len(studentID) == 8 and studentID.isdigit():
                break
            else:
                print("Incorrect input\n")
 
        fName = input("Please enter your first name: ")
        lName = input("Please enter your last name: ")
        email = input("Please enter your student email: ")

        print("\nStudent ID: ", studentID, "\nFirst name: ", fName, "\nLast Name: ", lName, "\nEmail: ", email, "\n")

        print("Is this information correct?")
        ans = yesOrNo()

        # If y = return results. If n = loop again. If q = break out of loop.
        if ans == "y":
            studentInfo = [studentID, fName, lName, email]
            return studentInfo
        elif ans == "q":
            break


###     Menu's      ###

# login / start menu
def login():
    
    print("Welcome to the HEPaS system for OUST students\n\n")
    print("Are you an existing student? (Former or Current)")
    ans = yesOrNo()

    if ans == "y":
        print("\nPlease enter the following information.")
        studentInfo = studentInformation()

        ## This is were we verify user information with the server 
        ## and then return the unit results on the system to display on screen.

    elif ans == "n":
        # Not a student, enter the information as well as their completed units and their results.
        print("\nPlease enter the following information.")
        studentInfo = studentInformation()
        
        ## for manual entry of unit codes and scores.
        studentScores = StudentScores()
        print(studentScores)

        ## average scores (Takes an a dictionary as a parameter)
        averageScore = Average(studentScores[1])
        print("Your average mark is ", averageScore)

        ## This is were we verify user information with the server 
        ## and then return the unit results on the system to display on screen.


        

### Main directory
""" 
Things to do:
    - Need to create/connect to server application to get student information, top 8 units and their average. 
    - No linked list in Python and dictionary does support duplicates, currently saved as two lists of unitCode and unitScore. 
      Could create a struct or class or something... or just keep as two lists
    - SQL database, I need to DL SQL and populate.
"""
def main():

    ## Start menu (login)
    login()


    

if __name__ == "__main__":
    main()


