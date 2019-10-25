import tkinter as tk
from datetime import datetime, timedelta

class Calendar(tk.Label):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.contents = tk.StringVar()
        self.contents.set(self.getDate())

    def write(self):
        self.config(textvariable=self.contents)
        self.contents.set(self.getDate())
        self.after(1000, self.write)

    def getDate(self):
        julian = datetime.today() - timedelta(days = 13)

        year = julian.year + 5508
        if julian.month > 8:
            year += 1
        date_string = str(julian.day) + " / " + self.romanize(julian.month) + " / " + str(year)
        time_string = str(julian.hour - 12 if julian.hour > 12 else (12 if julian.hour == 0 else julian.hour)) + " : " + str(julian.minute).zfill(2) + " : " + str(julian.second).zfill(2) + (" PM" if julian.hour > 11 else " AM")
        return date_string + "\n" + time_string

    def romanize(self, input):
        # bastardized from some o'reilly cookbook
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
        return ''.join(result)

root = tk.Tk()
root.tk_strictMotif()
root.title = "O.S. Anno Mundi"
#root.resizable(0,0)
root.wm_attributes("-topmost", True)

frame = tk.Frame(root)
frame.pack()

calendar = Calendar(frame)
calendar.pack()

calendar.write()
root.mainloop()