from tkinter import *
import maths

class GuiHandler:
    def __init__(self):
        self.createMainWindow()

    def createMainWindow(self):
        self.window = Tk()

        self.window.title("Small physics app by Zn0w")

        angleLbl = Label(self.window, text = "Enter angle in degrees: ")
        angleLbl.pack()

        self.angleTxt = Text(self.window, width = 10, height = 1)
        self.angleTxt.pack()

        speedLbl = Label(self.window, text = "Enter speed at the beggining in meters/second")
        speedLbl.pack()

        self.speedTxt = Text(self.window, width = 10, height = 1)
        self.speedTxt.pack()

        submitBut = Button(self.window, text = "Get results", command = self.submitInitialData)
        submitBut.pack()

        self.window.mainloop()

    def submitInitialData(self):
        angle = self.angleTxt.get(1.0, END)[:-1]
        speed = self.speedTxt.get(1.0, END)[:-1]

        self.mathHandler = maths.MathHandler(angle, speed)

        self.createResultsWindow()

    def createResultsWindow(self):
        resultsWindow = Tk()

        resultsWindow.title("Small physics app by Zn0w (Results)")

        time = Label(resultsWindow, text = "Fly time: " + str(self.mathHandler.flyTime))
        time.pack()

        distance = Label(resultsWindow, text = "Fly distance: " + str(self.mathHandler.flyDistance))
        distance.pack()

        height = Label(resultsWindow, text = "Max fly height: " + str(self.mathHandler.maxHeight))
        height.pack()

        self.x = Label(resultsWindow, text = "0 at 0 seconds")
        self.x.pack()

        self.y = Label(resultsWindow, text="0 at 0 seconds")
        self.y.pack()

        info = Label(resultsWindow, text = "Enter moment in seconds to get X and Y position")

        self.moment = Text(resultsWindow, width = 7, height = 1)
        self.moment.pack()

        button = Button(resultsWindow, text = "Get X and Y", command = self.getXandY)
        button.pack()

        resultsWindow.mainloop()

    def getXandY(self):
        time = self.moment.get(1.0, END)[:-1]

        if float(time) > self.mathHandler.flyTime:
            self.x.config(text=str(self.mathHandler.getXPosition(self.mathHandler.flyTime)) + " at " + time + " seconds")
            self.y.config(text=str(self.mathHandler.getYPosition(self.mathHandler.flyTime)) + " at " + time + " seconds")
        else:
            self.x.config(text=str(self.mathHandler.getXPosition(float(time))) + " at " + time + " seconds")
            self.y.config(text=str(self.mathHandler.getYPosition(float(time))) + " at " + time + " seconds")