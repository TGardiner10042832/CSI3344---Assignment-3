"""
CSI3344 - Assignment 3
HEPaS Server
Group 33
Tristan Gardiner
Kayl Grau
"""

# Import Pyro4 to get server functionality. 
import Pyro4

#Set SA2 Connection Details
SA2_PORT = 51516
SA2_SERVER = "localhost"

#Set SA1 Serving Details
SA1_PORT = 51515

"""
    Check with the database - when it's created...
    I'm just spitballing this one, need to create and fix... 
"""
@Pyro4.expose
class honorsCheck(object):

    # Lookup student in the database.
    def __getUserDetails(self, studentID, lastName, email):
        print("Extracting data from the OSCI database... ")

        # Connect to the OSCLR database with RMI
        OSCLRURI = "PYRO:honorsDb@" + OSCLR_SERVER + ":" + str(SA2_PORT)
        database = Pyro4.Proxy(OSCLRURI)

        # Request user details
        return database.getUserDetails(studentID, lastName, Email)







