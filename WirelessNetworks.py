ADHOC_Mode="ON"
BRAND_NAME="Cisco"
class WirelessNetworks:
    def __init__(self):
        self.id=""
        self.oxygenLevel=0
        self.temperature=0.0
    def  greetMessage(self):
        print("******************************************************************************")
        print("Welcome to the company's IoT-Based Health System")
        print("These are sensors of {} brand, and their Ad Hoc Mode is {}".format(BRAND_NAME,ADHOC_Mode))
        print("******************************************************************************")
    def setid(self,id):
        self.id=id  
    def getid(self):
        return self.id
    def setoxygenLevel(self,o2level):
        self.oxygenLevel=o2level
    def getoxygenLevel(self):
        return self.oxygenLevel
    def settemperature(self,temp):
        self.temperature=temp
    def gettemperature(self):
        return self.temperature            
