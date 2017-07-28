import Tkinter as tk
import tkMessageBox
import time

class Application(tk.Frame):
    mylist =[]
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title('Insert sort')
        tk.Label(self, text = "Please enter your nums, use ',' to seperate them ...").pack()
        self.createWidgets()

    def createWidgets(self):
        self.listInput = tk.Entry(self)
        self.listInput.pack()

        self.alertButton = tk.Button(self, text='Sort', command=self.hello)
        self.alertButton.pack()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        mylist = self.listInput.get().split(',', -1)
        mylist = map(int, mylist)
        start = time.time()
        self.insert_sort(mylist)
        stop = time.time()
        tkMessageBox.showinfo('Message', 'After sorting: %s' % mylist + '\n\n It costs: %s ms' % ((stop-start)/1000))

    def insert_sort(self,list1):
        for i in range(1, len(list1)):
            key = list1[i]
            j = i - 1

            while j >= 0 and list1[j] > key:
                list1[j + 1] = list1[j]
                j = j - 1
            list1[j + 1] = key


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()

