"""
CSI3344 - Assignment 3
HEPaS Server
Group 33
Tristan Gardiner
Kayl Grau
"""

# Import Pyro4 to get server functionality. 
import Pyro4

# This is the port for Server-1 and Client connection
S1_PORT = 60000


"""
    Check with the database - when it's created...
    I'm just spitballing this one, need to create and fix... 
"""
# @Pyro4.expose
# class honorsCheck(object):

#     # Lookup student in the database.
#     def __getUserDetails(self, studentID, lastName, email):
#         print("Extracting data from the OSCI database... ")

#         # Connect to the OSCLR database with RMI
#         OSCLRURI = "PYRO:honorsDb@" + OSCLR_SERVER + ":" + str(SA2_PORT)
#         database = Pyro4.Proxy(OSCLRURI)

#         # Request user details
#         return database.getUserDetails(studentID, lastName, email)


@Pyro4.expose
class StudentCheck(object):


    
    # CheckEligibility checks the given, or retrieved scores, for the given honours criteria.
    def checkEligibility(self, uCodes, uScores):
        courseAverage = self.average(uScores)
        # top8 = self.top8(uCodes, uScores)
        # average8 = self.average(top8[1])

        print("Ave  : ", courseAverage)
        # print("Top8 : ", top8)
        # print("Ave8 : ", average8)
        

    # Get the the averages of a list of numbers. 
    def average(self, uScore):
        
        numbers = uScore
        length = len(uScore)
        total = 0

        for i in range(length):
            total = total + numbers[i]
        
        average = total / length
        
        return average


    # Get the Top 8 units!              # not working need to re-Evaluate
    def top8(self, uCodes, uScores):
        units = uCodes
        scores = uScores
        top8Units = []
        top8Scores = []

        tempMax = scores[0]
        count = 0
        length = len(scores)

        if length <= 8:
            return None

        while count < 8:
            for i in range(length):
                if scores[i] >= tempMax:
                    tempMax = scores[i]
                    tempUnit = units[i]
                    del units[i]
                    del scores[i]
                    # length -1
                    
            print(i, tempUnit, tempMax, count)
            
            top8Units.append(tempUnit)
            top8Scores.append(tempMax)
            
            tempMax = 0
            # length = length - 1
            count = count + 1            
        
        return top8Units, top8Scores




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
