import WirelessNetworks
WN=WirelessNetworks.WirelessNetworks()
class Application:
    def __init__(self):
        self.listSensors=[]
        self._Path=[]
        self._SensorsInfoDic={}
    def createSensors(self):
        print("_*__*__*__*__*__*__*__*__*__*_")
        _sensorId=input("Enter the Sensor Id:")
        while True :
            if len(_sensorId)==1 and _sensorId.isupper():
                WN.setid(_sensorId)
                break
            else:
                print("This is an invalid entry for sensor Id!")
                print("_*__*__*__*__*__*__*__*__*__*_")
                _sensorId=input("Enter the Sensor Id:")
                continue
        _noOfneighbours=input("Enter the number of neighbours:")    
        while True:
            if _noOfneighbours.isdigit():
                _neighbourslist=[]
                for _neighbours in range(int(_noOfneighbours)):
                    _neighboursensor=input("Enter the neighbor for Sensor {}:".format(_sensorId))
                    while True:
                        if len(_neighboursensor)==1 and _neighboursensor.isupper():
                            break
                        else:
                            print("This is an invalid entry for the neighbour's name and/or distance!")
                            _neighboursensor=input("Enter the neighbor for Sensor {}:".format(_sensorId))
                            continue
                    _distance=input("Enter the distance to {}:".format(_sensorId))
                    while True:
                        if _distance.isdigit():
                            _neighbourslist+=[[_neighboursensor,int(_distance)]]
                            break
                        else:
                            print("This is an invalid entry for the neighbour's name and/or distance!")
                            _distance=input("Enter the distance to {}:".format(_sensorId))
                            continue
                break
            else:
                print("This is an invalid entry for the number of neighbours!")
                _noOfneighbours=input("Enter the number of neighbours:")
                continue
        _o2level=input("Enter the Oxygen level in %:")
        while True:
            if _o2level.isdigit():
                WN.setoxygenLevel(int(_o2level))
                break
            else:
                print("This is an invalid entry for the oxygen level!")
                _o2level=input("Enter the Oxygen level in %:")
                continue
        while True:    
            try:   
                _temp=float(input("Enter the temperature measurement:"))
                break
            except Exception:
                print("This is an invalid entry for the temperature!")
                _temp=input("Enter the temperature measurement:")
                continue   
        WN.settemperature(_temp)
        _sensorinfo=[[WN.getid(),WN.getoxygenLevel(),WN.gettemperature()],_neighbourslist]
        self.addtolistSensors(_sensorinfo)
    def convertToDictionary(self):
        self._SensorsInfoDic={}
        _list=self.listSensors
        for _sensors in range(len(_list)):
            self._SensorsInfoDic[_list[_sensors][0][0]]=_list[_sensors][1]    
    def findPath(self,X,Y,_path):
        l=[]
        for _sensors in self._SensorsInfoDic[X]:
            l.append(_sensors[1])
            m=max(l)
        for _Sensors in self._SensorsInfoDic[X]:    
            if _Sensors[0]==str(Y):
                _path.append(_Sensors[0])
                break
            elif (_Sensors[1]==m) and (_Sensors[0] not in _path):
                _path.append(_Sensors[0])
                self.findPath(str(_Sensors[0]),Y,_path)
            elif (_Sensors[1]==m) and (_Sensors[0] in _path):
                l.remove(_Sensors[1])
                if l==[]:
                    print("The destination is not found")
                else:
                    m=max(l)

    def addtolistSensors(self,_list):
        self.listSensors.append(_list)
    def getlistSensors(self):
        return self.listSensors    
App=Application()
WN.greetMessage()
_noOfSensors=input("Enter the number of sensors:")
while True:
    if _noOfSensors.isdigit():
        for i in range(int(_noOfSensors)):
            App.createSensors()
        break
    else:
        print("This is an invalid entry for the number of sensors!")
        _noOfSensors=input("Enter the number of sensors:")
        continue
App.convertToDictionary()
_sourceSensor=input("Enter the source sensor:")
while True:
    if (_sourceSensor.isupper) and (_sourceSensor in App._SensorsInfoDic):
        App._Path.append(_sourceSensor)
        break
    else:
        print("Invalid Sensor Entered!")
        _sourceSensor=input("Renter the source sensor:")
        continue
_destinationSensor=input("Enter the destination sensor:")
while True:
    if (_destinationSensor.isupper) and (_destinationSensor in App._SensorsInfoDic):
        App.findPath(_sourceSensor,_destinationSensor,App._Path)
        if _destinationSensor in App._Path:
            print("Path = ")
        break
    else:
        print("Invalid Sensor Entered!")
        _destinationSensor=input("Renter the destination sensor:")
        continue



