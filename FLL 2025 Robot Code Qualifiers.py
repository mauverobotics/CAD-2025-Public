# TO RUN CODE
''' 
pybricksdev run ble --name "CoachBot" "c:\Git\Robot_Testing\alphaTesting.py"
pybricksdev run ble --name "[CRTL ALT DEFEAT (THE DEFEATER)]" "[CODE_FILE_PATH]"
'''

'''
Import PyBricks
'''
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


'''
Initialization
'''
# Hub
hub = PrimeHub(front_side=Axis.Y)

# Attachment Motors
leftAttachmentMotor = Motor(Port.C)
rightAttachmentMotor = Motor(Port.E)

# Sensors
leftColorSensor = ColorSensor(Port.A)
rightColorSensor = ColorSensor(Port.D)
distanceSensor = None
forceSensor = None

# Drive motors
leftDriveMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightDriveMotor = Motor(Port.F)

# DriveBase
driveBase = DriveBase(leftDriveMotor, rightDriveMotor, 56, 80)


'''
Missions (Ctrl Alt Defeat)
'''

"""
ARIHANT
"""
def siloForgeHeavyliftingWOS():
    driveBase.settings(900, 500, 900, 500)

    driveBase.use_gyro(True)
    
    driveBase.settings(600, 600)
    driveBase.straight(-15)
    driveBase.straight(363)
    driveBase.turn(8)
    for i in range(3):
        rightAttachmentMotor.run_angle(700, -290) 
        rightAttachmentMotor.run_angle(250, 285)
    driveBase.straight(-29)
    driveBase.turn(-43)
    driveBase.straight(351)
    driveBase.turn(81)
    rightColorSensor.detectable_colors([Color.BLACK, Color.WHITE, Color.NONE, Color.BROWN, Color.GREEN, Color.GRAY])
    driveBase.drive(200, 0)
    while not rightColorSensor.color(True) == Color.BLACK:
        pass
    driveBase.straight(0, Stop.HOLD)
    driveBase.settings(400, 500, 700, 800)
    driveBase.straight(33)
    rightAttachmentMotor.run_angle(200, -275)
    rightAttachmentMotor.run_angle(340, 305)
    # driveBase.turn(5)
    leftAttachmentMotor.run_angle(800, -950)
    driveBase.straight(-150)
    # driveBase.settings(900,900,900,900)
    driveBase.turn(-52)
    driveBase.straight(-125)
    driveBase.turn(-30)
    driveBase.straight(-700)

"""
SMITHI
"""
def whatsOnSaleTipTheScale():
    driveBase.settings(550, 550)
    driveBase.straight(-20)
    driveBase.use_gyro(True)   
    #driveBase.straight(300,Stop.HOLD, False)  
    #leftAttachmentMotor.run_angle(200, -160, Stop.HOLD, False)
    driveBase.straight(500)
    #-driveBase.straight(300)
    #-driveBase.turn(10)
    #driveBase.straight(246)
    #wait(8000)
    #driveBase.straight(546)
    #leftAttachmentMotor.run_angle(200, -80, Stop.HOLD, False)
    rightAttachmentMotor.run_angle(1200, 167)
    driveBase.straight(10)
    driveBase.settings(680,680)
    leftAttachmentMotor.run_angle(300, -80, Stop.HOLD, False)
    leftAttachmentMotor.run_until_stalled(700,Stop.COAST,80) # Hooks into the scalepan
    driveBase.straight(2)
    leftAttachmentMotor.run_angle(600, -120) #pulls out the scalepan 
    # driveBase.turn(3)
    # driveBase.settings(300,300)
    driveBase.straight(-190) #160, 300
    wait(10)
    rightAttachmentMotor.run_angle(600,-50)
    driveBase.straight(40)
    rightAttachmentMotor.run_angle(600, -140, Stop.HOLD)
    # leftAttachmentMotor.run_angle(400, -80, Stop.HOLD, False)
    # leftAttachmentMotor.run_angle(400, 140) # Hooks into the scalepan
    # driveBase.straight(2)
    # leftAttachmentMotor.run_angle(400, -120) #pulls out the scalepan 
    #driveBase.turn(-47)
    driveBase.settings(950,1250,950,1250)
    leftAttachmentMotor.run_angle(200,140, wait=False)
    # driveBase.straight(-200)
    # driveBase.turn(-20,Stop.HOLD,False)
    # driveBase.straight(-300)
    # driveBase.straight(-400)
    # driveBase.turn(60)
    # driveBase.straight(-50)
   #driveBase.straight(-150)
    driveBase.straight(-600)
    #driveBase.arc(-400,-50)
    #leftAttachmentMotor.run_angle(500, -180)
   

"""
ANOUSHKA
"""
def forumStatuerebuild():
    driveBase.settings(900,900,900,900)
    driveBase.straight(-15)
    rightAttachmentMotor.run_until_stalled(-275, duty_limit=70)
    rightAttachmentMotor.hold()
    driveBase.settings(900,600,900,900)
    driveBase.straight(700)
    driveBase.settings(200,100,200,200)
    driveBase.straight(300,Stop.NONE)
    rightColorSensor.detectable_colors([Color.BLACK,Color.WHITE,Color.NONE])
    leftColorSensor.detectable_colors([Color.BLACK,Color.WHITE,Color.NONE])
    while not rightColorSensor.color(True) == Color.BLACK and leftColorSensor.color(True) == Color.BLACK:
        pass
    #####driveBase.turn(27) #18 too little
    driveBase.straight(0)
    driveBase.turn(40)
    # leftDriveMotor.run_angle(100,90,Stop.NONE)
    # while not rightColorSensor.color(True) == Color.WHITE:
    #     pass
    # leftDriveMotor.stop()
    rightAttachmentMotor.run_until_stalled(300, Stop.COAST,40)
    driveBase.settings(900,900,500,900) #100 was too slow
    # driveBase.turn(10,wait=False)
    driveBase.straight(75)
    driveBase.settings(900,900,300,900)
    #rightAttachmentMotor.run_until_stalled(-275,Stop.COAST,120)
    rightAttachmentMotor.run_angle(235,-120)
    wait(250)
    driveBase.turn(8)
    rightAttachmentMotor.hold()
    #driveBase.turn(12)
    driveBase.turn(4)
    driveBase.straight(135)
    leftAttachmentMotor.run_angle(100,-220)
    driveBase.straight(-200)
    driveBase.settings(900,900,900,900)
    driveBase.turn(-57)
    driveBase.straight(750)

"""
ALINA
"""
def unravelsandSitemarkingOilrig():
    driveBase.settings(900,900,900,980)

    driveBase.straight(-20)
    driveBase.straight(200)
    driveBase.turn(7)
    driveBase.straight(285)
    driveBase.turn(7)
    driveBase.settings(100,100,900,980)
    driveBase.straight(130)
    driveBase.settings(900,900,900,980)
    driveBase.turn(7)
    driveBase.straight(-20)
    rightAttachmentMotor.run_angle(300, 210, Stop.HOLD)
    leftAttachmentMotor.run_angle(990, 3500, Stop.HOLD)
    rightAttachmentMotor.run_angle(990, -150, Stop.HOLD)
    driveBase.straight(-600)

"""
SMYAN
"""
def mapRevealSurfaceBrushing():
    driveBase.settings(800, 850, 670, 500)
    driveBase.use_gyro(True)
    driveBase.straight(-15) #going back to square against the wall
    driveBase.straight(742) #Approaching top soil
    driveBase.turn(-43.5) #turning to drop the attachment
    driveBase.straight(166) #dropping the attachment and pushing two top soils
    rightAttachmentMotor.run_angle(500, -230) #picking up top soil
    driveBase.settings(600,300,200,300) #Speed up
    driveBase.straight(-250) #moving away from top soil
    driveBase.settings(800, 850, 670, 500) #speed up
    driveBase.turn(-29.5) #turning to surface brushing
    driveBase.straight(100) #Hooking surface brushing
    leftAttachmentMotor.run_angle(300, 80) #pick up the brush
    driveBase.turn(-170) #Turn to deliver surface brushing & topsoil
    driveBase.straight(100) #goes forward to deliver surface brush and topsoil
    leftAttachmentMotor.run_angle(350, -100) #testing if this causes stall was 300 and stalling - changing to -100
    driveBase.straight(-100)
    driveBase.turn(-15)
    driveBase.straight(120)
    rightAttachmentMotor.run_until_stalled(350, Stop.COAST, 60) #was 200 amd stalling changed to 150 to verify going back to 200
    driveBase.straight(-100)
    leftAttachmentMotor.run_angle(350, 110) #Move arm backup
    driveBase.turn(110)
    driveBase.straight(525)
"""
AADI
"""
def mineshaftexplorerCarefulrecovery():
    driveBase.settings(900, 900, 900, 900)
    driveBase.straight(-20)

    driveBase.straight(630)
    driveBase.turn(-1.85)

    rightAttachmentMotor.run_angle(400, 345)
        # return
    driveBase.straight(-30)
    rightAttachmentMotor.run_angle(450, -340)

            # driveBase.use_gyro(False)
            # driveBase.straight(410) #Align to wall
            # driveBase.use_gyro(True)
    driveBase.use_gyro(True)
    # driveBase.turn(4.6)
    driveBase.use_gyro(False)
    driveBase.straight(410)
        #wait(2500)
    driveBase.stop()
    driveBase.use_gyro(True)
    driveBase.straight(-78)
    driveBase.settings(300,200,200,200)
    driveBase.turn(90) #instead of 92
    driveBase.straight(-28)
    driveBase.settings(200, 200, 500, 500)
    # driveBase.straight(23)
    driveBase.use_gyro(True)


    #leftAttachmentMotor.run_angle(445, -240, wait=False)
    leftAttachmentMotor.run_until_stalled(-445,Stop.COAST,50)
    rightAttachmentMotor.run_angle(300, 330)
    leftColorSensor.detectable_colors([Color.BLACK, Color.NONE, Color.BROWN, Color.WHITE, Color.GREEN])
    rightColorSensor.detectable_colors([Color.BLACK, Color.NONE, Color.BROWN, Color.WHITE, Color.GREEN])
    driveBase.settings(175)
    driveBase.straight(10, Stop.NONE)
    while not ((leftColorSensor.color(True)==Color.WHITE) and (rightColorSensor.color(True)==Color.WHITE)):
        pass
    # driveBase.straight(33)
    # wait(3000)
    # ##driveBase.turn(-5)
    # wait(3000)
    # driveBase.straight(95)
    driveBase.straight(110)
    # wait(2000)
    #driveBase.straight(113)
    #driveBase.turn(-3)
    #50 for the lifting - sweet spot for taking it out
    leftAttachmentMotor.run_angle(100,51, wait=False)
    rightAttachmentMotor.run_angle(200,-280)
    # driveBase.straight(100)
    driveBase.settings(600, 600, 350, 350)
    driveBase.straight(-180)
    driveBase.turn(55)
    driveBase.straight(110)
    driveBase.turn(-43)
    driveBase.straight(350)
    driveBase.turn(-20)
    driveBase.straight(450)
    driveBase.leftAttachmentMotor.run_angle(100)
    driveBase.turn(-50)
    #driveBase.straight(300)
    driveBase.straight(100)


    
    
'''
Run Functions
'''
def run10():
    siloForgeHeavyliftingWOS()

def run20():
    whatsOnSaleTipTheScale()

def run30():
    forumStatuerebuild()
   
def run40():
    unravelsandSitemarkingOilrig()

def run50():
    mapRevealSurfaceBrushing()

def run60():
    mineshaftexplorerCarefulrecovery()


runs = [run10,run20,run30,run40,run50,run60]
runNames = [10,20,30,40,50,60]


'''
Menusystem
'''
class MenuSystem():
    # Setup
    def __init__(self, runs, runNames, hub, driveBase, rightAttachmentMotor, leftAttachmentMotor, rightColorSensor, leftColorSensor):
        # Check for misusage
        if len(runs) == 0 or len(runNames) == 0 or len(runs) != len(runNames):
            print("Menusystem not correctly initialized")
            SystemExit

        # Initialize
        self.runs = runs
        self.runNames = runNames
        self.hub = hub
        self.driveBase = driveBase
        self.stopwatch = StopWatch()
        self.rightAttachmentMotor = rightAttachmentMotor
        self.leftAttachmentMotor = leftAttachmentMotor
        self.rightColorSensor = rightColorSensor
        self.leftColorSensor = leftColorSensor
        self.runNumber = 0
        self.hub.system.set_stop_button({Button.LEFT, Button.RIGHT})
    
    # Changing runs
    def changeRun(self, buttonPressed = "LEFT"):
        if buttonPressed == "RIGHT":
            if self.runNumber == len(self.runs) - 1:
                    self.runNumber = 0
            else:
                    self.runNumber += 1
        else:
            if self.runNumber == 0:
                    self.runNumber = len(self.runs) - 1
            else:
                self.runNumber -= 1
        wait(300)

    # executing menusystem
    def execute(self):
        self.leftColorSensor.lights.off()
        self.rightColorSensor.lights.off()

        while True:
            #Always running code (displaying stats)
            self.hub.display.number(self.runNames[self.runNumber])
            
            #Changing runs
            if self.hub.buttons.pressed() == {Button.RIGHT}:
                self.changeRun("RIGHT")
            elif self.hub.buttons.pressed() == {Button.LEFT}:
                self.changeRun()
            
            #Execute Runs
            if self.hub.buttons.pressed() == {Button.CENTER}:
                print(f"Run #{self.runNames[self.runNumber]} attachment change time = {self.stopwatch.time()/1000}")
                self.driveBase.use_gyro(True)
                self.driveBase.reset()
                self.stopwatch.reset()
                driveBase.settings(500, [125, 125], 700, [350, 450])
                wait(500)
                self.runs[self.runNumber]()
                self.rightAttachmentMotor.stop()
                self.leftAttachmentMotor.stop()
                self.driveBase.stop()
                #self.driveBase.use_gyro(False)
                totalTime = self.stopwatch.time()/1000
                wait(500)
                print(f"Run {self.runNames[self.runNumber]} Time = {totalTime}")
                self.changeRun("RIGHT")


'''
Execute Code
'''
menuSystem = MenuSystem(runs, runNames, hub, driveBase, rightAttachmentMotor, leftAttachmentMotor, rightColorSensor, leftColorSensor)
menuSystem.execute()
