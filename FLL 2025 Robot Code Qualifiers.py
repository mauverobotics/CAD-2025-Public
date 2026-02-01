# TO RUN CODE
''' 
pybricksdev run ble --name "CoachBot" "c:\Git\Robot_Testing\alphaTesting.py"
pybricksdev run ble --name "[ROBOT_NAME]" "[CODE_FILE_PATH]"
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
Mission Functions
'''

'''
Moves robot straight for 1000 mm
'''
def sample1():
    driveBase.straight(1000, Stop.COAST)
'''
Turns robot 90 degrees right
'''
def sample2():
     driveBase.straight(-1000, Stop.COAST)

'''
Moves robot in an arc with a radius of 100mm and for 90 degrees right
'''
def sample3():
     driveBase.arc(500, 90)

"""
SMYAN
"""
def mapReveal():
    driveBase.settings(800, 850, 670, 500)
    driveBase.straight(-20)
    driveBase.use_gyro(True)
    rightAttachmentMotor.run_angle(400,253, Stop.HOLD, False)
    driveBase.straight(705, Stop.BRAKE) #moves to mission 2
    leftAttachmentMotor.run_angle(300, 80, Stop.HOLD, False)
    driveBase.turn(-53.125) #turn to align for mission 2
    #wait(1000)
    driveBase.straight(190, Stop.BRAKE) #moves into mission 2
    rightAttachmentMotor.run_angle(250, -230, Stop.HOLD, False) #lifts land thing
    driveBase.straight(-25, Stop.BRAKE) #comes back to lift land thing
def surfaceBrushing():
    #driveBase.settings(500,300,200,300)
    driveBase.straight(-200) #moves back
    leftAttachmentMotor.run_angle(200, -70)
    #print(driveBase.settings())
    driveBase.settings(100,100)
    driveBase.turn(-44) #hits lever 1
    driveBase.settings(800,2400,670,2100) 
    wait(500)
    driveBase.straight(75) #goes to pick up brush
    # while not driveBase.stalled():
    #     pass
    # driveBase.straight(0)
    leftAttachmentMotor.run_angle(300, 70) #picks up brush
    driveBase.straight(-30)
    driveBase.turn(-65) #turns towards home
    driveBase.straight(480) #goes home

"""
AADI
"""
def mineshaftexplorerCarefulrecovery():
    driveBase.use_gyro(True)   

    driveBase.settings(900, 900, 900, 900)
    driveBase.straight(-20)

    driveBase.straight(630)
    driveBase.turn(-1.5)

    rightAttachmentMotor.run_angle(400, 345)
    # return
    driveBase.straight(-30)
    rightAttachmentMotor.run_angle(450, -340)

        # driveBase.use_gyro(False)
        # driveBase.straight(410) #Align to wall
        # driveBase.use_gyro(True)
    driveBase.use_gyro(False)
    driveBase.straight(410)
    #wait(2500)
    driveBase.stop()
    driveBase.use_gyro(True)
    driveBase.straight(-69)

    driveBase.turn(91)
    driveBase.straight(-22)
    driveBase.settings(200, 200, 500, 500)
    leftAttachmentMotor.run_angle(300, -230.348, wait=False)
    rightAttachmentMotor.run_angle(300, 350)
        #leftAttachmentMotor.run_angle(100, 15)

    driveBase.straight(166)
        
    leftAttachmentMotor.run_angle(60, 49)
    rightAttachmentMotor.run_angle(100, -185)
    # leftAttachmentMotor.run_angle(80,-25)

    driveBase.straight(-160)
    driveBase.turn(108)
    leftAttachmentMotor.run_angle(180, 70, wait=False)
    driveBase.settings(900, 900, 900, 900)
    driveBase.straight(800)

"""
ALINA
"""
def unravelsandSitemarkingOilrig():
    driveBase.settings(straight_speed=900,straight_acceleration=900,turn_rate=500,turn_acceleration=500)
    leftColorSensor.detectable_colors([Color.BLACK, Color.BLUE, Color.NONE, Color.GRAY])
    #print(leftColorSensor.color(True))
    driveBase.use_gyro(True)

    driveBase.straight(-20)
    driveBase.straight(415)
    driveBase.turn(3.5)
    driveBase.straight(70)
    rightAttachmentMotor.run_angle(300, 327)
    driveBase.straight(-40)
    rightAttachmentMotor.run_angle(300, -327,Stop.HOLD, False)
    driveBase.straight(-100)
    driveBase.turn(-25)
    driveBase.straight(250)
    driveBase.turn(24)
    driveBase.settings(300,100,500,500)
    driveBase.straight(200)
    driveBase.settings(straight_speed=900,straight_acceleration=2000,turn_rate=500,turn_acceleration=500)
    driveBase.straight(-200)
    driveBase.turn(-30)
    driveBase.straight(250)
    driveBase.turn(30)
    driveBase.straight(300)
    driveBase.turn(120)
    driveBase.straight(130)
    driveBase.turn(-25)
    driveBase.straight(20)
    leftAttachmentMotor.run_angle(300, -800)
    driveBase.settings(900,2000,900,900)
    driveBase.straight(-200)
    driveBase.turn(-90)
    driveBase.straight(700)

"""
SMITHI
"""
def whatsOnSaleTipTheScale():
    driveBase.settings(500, 500)
    driveBase.straight(-20)
    driveBase.use_gyro(True)   
    #driveBase.straight(300,Stop.HOLD, False)  
    #leftAttachmentMotor.run_angle(200, -160, Stop.HOLD, False)
    #driveBase.straight(546)
    driveBase.straight(300)
    driveBase.turn(10)
    driveBase.straight(246)
    #wait(8000)
    #driveBase.straight(546)
    leftAttachmentMotor.run_angle(200, -80, Stop.HOLD, False)
    rightAttachmentMotor.run_angle(1000, 167)
    driveBase.straight(10)
    driveBase.settings(680,680)
    #leftAttachmentMotor.run_angle(400, -80, Stop.HOLD, False)
    leftAttachmentMotor.run_until_stalled(300) # Hooks into the scalepan
    driveBase.straight(2)
    leftAttachmentMotor.run_angle(400, -120) #pulls out the scalepan 
    # driveBase.turn(3)
    # driveBase.settings(300,300)
    driveBase.straight(-300) #160

    driveBase.straight(40)
    #driveBase.turn(-20)
    #driveBase.turn(20,Stop.HOLD,False)
    rightAttachmentMotor.run_angle(600, -140, Stop.HOLD)
    # leftAttachmentMotor.run_angle(400, -80, Stop.HOLD, False)
    # leftAttachmentMotor.run_angle(400, 140) # Hooks into the scalepan
    # driveBase.straight(2)
    # leftAttachmentMotor.run_angle(400, -120) #pulls out the scalepan 
    #driveBase.turn(-47)
    driveBase.settings(950,950,950,950)
    leftAttachmentMotor.run_angle(200,140, wait=False)
    driveBase.curve(-400,80)
    
    
   #driveBase.straight(-150)

"""
ARI
"""
def siloForgeHeavyliftingWOS():
    driveBase.settings(900, 500, 900, 500)

    driveBase.use_gyro(True)
    
    driveBase.settings(600, 600)
    driveBase.straight(-15)
    driveBase.straight(383)
    driveBase.turn(2)
    for i in range(3):
        rightAttachmentMotor.run_angle(900, -320) 
        rightAttachmentMotor.run_angle(300, 305)
    driveBase.turn(-33)
    driveBase.straight(340)
    driveBase.turn(75.5)
    rightColorSensor.detectable_colors([Color.BLACK, Color.WHITE, Color.NONE, Color.BROWN, Color.GREEN, Color.GRAY])
    driveBase.drive(200, 0)
    while not rightColorSensor.color(True) == Color.BLACK:
        pass
    driveBase.straight(0, Stop.HOLD)
    driveBase.straight(30)
    driveBase.turn(-3)
    rightAttachmentMotor.run_angle(200, -230)
    rightAttachmentMotor.run_angle(340, 220, wait=False)
    # driveBase.straight(10) 
    leftAttachmentMotor.run_angle(800, -900)
    driveBase.straight(-27.8)
    driveBase.turn(-40)
    driveBase.arc(725,-80) 
    # TO RUN CODE


"""
ANOUSHKA
"""
# def forumStatuerebuild():
#     driveBase.settings(900,900,900,900)
#     driveBase.straight(-10)
#     driveBase.use_gyro(True)
#     driveBase.straight(200)
#     #driveBase.turn(12)
#     driveBase.turn(15)
#     driveBase.straight(400)
#     #driveBase.straight(600)
#     driveBase.settings(200,200,100,200)
#     driveBase.straight(300,Stop.NONE)
#     rightColorSensor.detectable_colors([Color.BLACK,Color.NONE])
#     while not rightColorSensor.color(True) == Color.BLACK:
#         pass
#     driveBase.straight(0)
#     #driveBase.turn(27)
#     rightAttachmentMotor.run_until_stalled(300)
#     driveBase.turn(15)
#     driveBase.drive(300,0)
#     wait(1150)
#     driveBase.straight(0)
#     #driveBase.straight(-9,Stop.COAST)
#     #driveBase.straight(-27)
#     driveBase.turn(18,Stop.HOLD,False)
#     #rightAttachmentMotor.run_angle(300,-170)
#     #rightAttachmentMotor.run_until_stalled(-300)
#     rightAttachmentMotor.run(-300)
#     wait(400)
#     rightAttachmentMotor.stop()
#     #driveBase.straight(155)
#     #driveBase.turn(-14)
#     driveBase.settings(900,900,500,900)
#     driveBase.straight(-20)
#     driveBase.turn(-14)
#     driveBase.straight(170)
#     wait(20)
#     driveBase.settings(900,900,300,900)
#     driveBase.straight(-200)
#     driveBase.turn(50)
#     driveBase.straight(400)
#     #driveBase.turn(45)
#     #driveBase.straight(50)
#     driveBase.arc(200,70)

def forumStatuerebuild2():
    driveBase.settings(900,900,900,900)
    driveBase.straight(-15)
    driveBase.straight(200)
    #driveBase.turn(12)
    driveBase.turn(15)
    driveBase.straight(400)
    #driveBase.straight(600)
    driveBase.settings(200,200,100,200)
    driveBase.straight(300,Stop.NONE)
    rightColorSensor.detectable_colors([Color.BLACK,Color.NONE])
    while not rightColorSensor.color(True) == Color.BLACK:
        pass
    driveBase.straight(0)
    #driveBase.turn(27)
    #rightAttachmentMotor.run_gle(300,240)
    rightAttachmentMotor.run_until_stalled(300)
    driveBase.settings(900,900,500,900) #100 was too slow
    driveBase.turn(18) #15 not enough
    driveBase.straight(150)
    #driveBase.drive(300,0)
    #wait(1150)
    #driveBase.straight(0)
    # #driveBase.straight(-18)
    driveBase.settings(900,900,300,900)
    rightAttachmentMotor.run_angle(600,-60)
    driveBase.turn(23)
    driveBase.straight(100)
    driveBase.straight(-200)
    driveBase.turn(37)
    driveBase.straight(470)
    driveBase.turn(50)
    driveBase.straight(150)
    #driveBase.turn(45)
    #driveBase.straight(50)
    #driveBase.arc(200,65)
    
    


    wait(1000)
    #wait(250)
    # rightAttachmentMotor.run(300)
    # wait(400)
    # rightAttachmentMotor.stop()
    # # rightAttachmentMotor.run_angle(200,-240,Stop.HOLD,False)
    # # driveBase.turn(33)
    # # wait(1000000)
    # #driveBase.straight(155)
    # #driveBase.turn(-14)
    # driveBase.settings(900,900,500,900)
    # driveBase.straight(-20)
    # driveBase.turn(-14)
    # driveBase.straight(170)
    # wait(20)
    # driveBase.settings(900,900,300,900)
    # driveBase.straight(-200)
    # driveBase.turn(50)
    # driveBase.straight(400)
    # #driveBase.turn(45)
    # #driveBase.straight(50)
    # driveBase.arc(210,70)
    
'''
Run Functions
'''
def run10():
    mapReveal()
    surfaceBrushing()

def run20():
    mineshaftexplorerCarefulrecovery()

def run30():
    unravelsandSitemarkingOilrig()
   
def run40():
    whatsOnSaleTipTheScale()

def run50():
    siloForgeHeavyliftingWOS()

def run60():
    forumStatuerebuild2()


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

