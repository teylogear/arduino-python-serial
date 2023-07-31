import tkinter as tk
from src.app import Application

def main():

  main_window = tk.Tk()
  app = Application(main_window)
  app.mainloop()


if __name__ == '__main__':
  main()