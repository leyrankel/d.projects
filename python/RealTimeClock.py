import RealTimeClock as tk
import time

def update_clock():
    kel = time.strftime("%H:%M:%S")
    kel.config(text=kel)
    kel.after(1000, update_clock)
    
app = tk.Tk()
app.title("Ceas Python")

kel = tk.Label(app, text="", font=("Helvetica", 48))
kel.pack()

update_clock()
app.mainloop()
