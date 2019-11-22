class SurveillanceCamera;

    self._servo1 = ""
    self._servo2 = ""
    self._camera = ""
    
    def __init__(self,servo1,servo2,camera):
        self._servo1 = servo1
        self._servo2 = servo2
        self._camera = camera
        self._servo1.reset()
        print("servo1 reset ready")
        self._servo2.reset()
        print("servo2 reset ready")
        
    def Surveillance(self):
        try:
            
    