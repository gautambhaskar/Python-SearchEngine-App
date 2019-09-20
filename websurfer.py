from tkinter import *
import webbrowser

class WebSurfer:
    def __init__(self, master):
        self.master = master
        master.title("WebSurfer")

        self.chosen = 2
        self.label = Label(master, text="WebSurfer")
        self.label.pack()
        #Google Search Option
        self.instruct2 = Label(master, text="Search:")
        self.instruct2.pack()
        self.search = Entry(master)
        self.search.pack()
        self.choice = Label(master, text="Search Engine:")
        self.R1 = Radiobutton(master, text="Google", variable=self.chosen, value=1, command=self.change1)
        self.R2 = Radiobutton(master, text="DuckDuckGo", variable=self.chosen, value=2, command=self.change2)
        self.R1.pack(anchor=W)
        self.R2.pack(anchor=W)
        self.go = Button(master, text="Search", command=self.google)
        self.go.pack()
        self.check = Button(master, text="History", command=self.history)
        self.check.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.history = []
    def change1(self):
        self.chosen = 1
    def change2(self):
        self.chosen = 2
    def google(self):
        params = str(self.search.get()).split(" ")
        if params != [""]:
            self.history.append(params)
        query = ""
        if(self.chosen == 1):
            query += "https://www.google.com/search?q="
        elif(self.chosen == 2):
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
root = Tk()
my_gui = WebSurfer(root)
root.mainloop()
