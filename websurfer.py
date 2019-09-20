from tkinter import *
import webbrowser

class WebSurfer:
    def __init__(self, master):
        self.master = master
        master.title("WebSurfer")

        self.chosen = "b"
        self.label = Label(master, text="WebSurfer")
        self.label.pack()
        #Google Search Option
        self.instruct2 = Label(master, text="Search:")
        self.instruct2.pack()
        self.search = Entry(master)
        self.search.pack()
        self.choice = Label(master, text="Search Engine:")
        self.R1 = Radiobutton(master, text="Google", variable=self.chosen, value="a")
        self.R2 = Radiobutton(master, text="DuckDuckGo", variable=self.chosen, value="b")
        self.R1.pack()
        self.R2.pack()
        self.go = Button(master, text="Search", command=self.google)
        self.go.pack()
        self.R2.select()
        self.check = Button(master, text="History", command=self.history)
        self.check.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.history = []
    def google(self):
        params = str(self.search.get()).split(" ")
        if params != "":
            self.history.append(params)
        query = ""
        if(self.chosen == "a"):
            query += "https://www.google.com/search?q="
        elif(self.chosen == "b"):
            query += "https://www.duckduckgo.com/?q="
        for param in params:
            query += param + "+"
        finalQuery = query[0:-1]
        webbrowser.open(finalQuery)
    def history(self):
        if len(self.history)>0:
            print("Search History Report:")
            for entry in self.history:
                print(entry)
        else:
            print("No search records available...")
            print(self.chosen.get())


root = Tk()
my_gui = WebSurfer(root)
root.mainloop()