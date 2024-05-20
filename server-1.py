"""
CSI3344 - Assignment 3
HEPaS Server
Group 33
Tristan Gardiner
Kayl Grau
"""

# Import Pyro4 to get server functionality. 
import Pyro4

# This is the port for Server-1 (S1_PORT) and the OSCLR database (S2_PORT)
S1_PORT = 60000
S2_PORT = 60001
OSCLR_SERVER = "localhost"

@Pyro4.expose
class StudentCheck(object):

    # Verify students with the database.
    def verifyStudent(self, studentID, fName, lName, email):
        print("Connecting to OCLR database... ")
        
        # Connect to the OSCLR database with RMI
        OSCLRURI = "PYRO:OSCLR@" + OSCLR_SERVER + ":" + str(S2_PORT)
        database = Pyro4.Proxy(OSCLRURI)

        # Request to verify user details and if correct, return unit codes and scores.
        unitResults = database.getUserDetails(studentID, fName, lName, email)
    
        # Then check the students eligibility if results returns.
        if unitResults != None:
            eligibility = self.checkEligibility(self, unitResults[0], unitResults[1])
            return eligibility
        else:
            NoStudentMsg = "Student Record not found."
            return NoStudentMsg    

    
    # CheckEligibility checks the given, or retrieved scores, for the given honours criteria.
    def checkEligibility(self, uCodes, uScores):
        UC = uCodes
        US = uScores

        courseAverage = self.average(US)
        top8 = self.top8(UC, US)
        average8 = self.average(top8[1])
        eligibilityMSG = self.eligibility(UC, US, courseAverage, average8)
        
        return courseAverage, top8, average8, eligibilityMSG
        

    # Get the the averages of a list of numbers. 
    def average(self, uScore):
        numbers = uScore
        length = len(uScore)
        total = 0

        for i in range(length):
            total = total + numbers[i]
        
        average = total / length
        
        return average


    # Get the Top 8 units!
    def top8(self, uCodes, uScores):
        units = uCodes.copy()
        scores = uScores.copy()
        top8Units = []
        top8Scores = []

        tempMax = 0
        count = 0
        length = len(scores)

        if length <= 8:
            return uCodes, uScores

        while count < 8:
            for i in range(length):
                if scores[i] >= tempMax:
                    tempMax = scores[i]
                    tempUnit = units[i]
                    tempIndex = i
        
            top8Units.append(tempUnit)
            top8Scores.append(tempMax)

            del units[tempIndex]
            del scores[tempIndex]
        
            tempMax = 0
            length = length - 1
            count = count + 1            
    
        return top8Units, top8Scores



    # Checks the eligibility and returns the message for the student to see.
    def eligibility(self, uCodes, uScores, courseAverage, average8):

        length = len(uCodes)

        # Determine the number for failed units.
        # Count each score below 50.
        fails = 0
        for i in range(length):
            if uScores[i] < 50:
                fails = fails + 1

        # Completed less than 16 units (or 15 or less)
        if length < 16:
            msg = "completed less than 16 units! DOES NOT QUALIFY FOR HONORS STUDY!"

        # If there are more than 6 fails.
        elif fails >= 6:
            msg = "with 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY!"

        # Course Average >= 70
        elif courseAverage >= 70:
            msg = "QUALIFIES FOR HONOURS STUDY!"

        # If course average is < 70 and >= 65 but average8 >= 80, return 'qualify' message.
        elif courseAverage < 70 and courseAverage >= 65 and average8 >= 80:
                msg = ", Top 8 average = " + str(average8) + ", QUALIFIES FOR HONOURS STUDY!"

        # If course average is < 70 and >= 65 but average8 < 80, return 'chance' message.
        elif courseAverage < 70 and courseAverage >= 65 and average8 < 80:
                msg = ", Top 8 average = " + str(average8) + ", MAY HAVE GOOD CHANCE! Need further assessment!"
    
        # Course average is < 65 and >= 60, but average8 is 80 or higher.    
        elif courseAverage < 65 and courseAverage >= 60 and average8 >= 80:
                msg = ", Top 8 average = " + str(average8) + ", MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator's permission!"
    
        # Otherwise, they do not qualify.
        else:
            msg = "DOES NOT QUALIFY FOR HONORS STUDY!"
    
        return msg


# Accept RMI
studentCheck = StudentCheck()
daemon = Pyro4.Daemon(port = S1_PORT)
uri = daemon.register(studentCheck, "studentCheck")
# ^ this is the URI name used to connect to it.


print()
print(" Server-1 : running ")
print(" Object uri =", uri)
print()
print("Ready... ")
daemon.requestLoop()
