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
        if unitResults[0] != None:
            eligibility = self.checkEligibility(self, unitResults[0], unitResults[1])
            return eligibility
        else:
            NoStudentMsg = "Student Record not found."
            return NoStudentMsg
        

    
    # CheckEligibility checks the given, or retrieved scores, for the given honours criteria.
    def checkEligibility(self, uCodes, uScores):
        courseAverage = self.average(uScores)
        top8 = self.top8(uCodes, uScores)
        average8 = self.average(top8[1])
        eligibityMSG = self.eligibility(uCodes, uScores)
        
        
        # Current results to return
        print("Ave  : ", courseAverage)
        print("Top8 : ", top8)
        print("Ave8 : ", average8)
        

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
        units = uCodes
        scores = uScores
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
    def eligibility(self, UC, US, ):
        
        # Completed less than 16 units.
        



        # More than 6 failed results. 
        



        # Course Average > 70
        



        # Course Average >= 60 and Top 8 average >= 80
        
        
        
        
        # Course Average >= 65 and < 70, and Top 8 average >= 80
        



        # Otherwise, they do not qualify.
        


        # Unit then:
        pass
    



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
