import tkinter as tk
from tkinter import ttk
from threading import Thread
from src import arduino
from src.checkbox import Checkbox


class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.main_window.title('Comunicación serial Arduino - tkinter')
        self.main_window.protocol('WM_DELETE_WINDOW', self.close)
        self.grid()
        self.arduino = arduino.connect()
        self.isRun = False

        bar_container = ttk.Labelframe(self, text='Potenciometro')
        bar_container.grid(row=0, column=0, padx=30, pady=[30, 0], ipadx=20, ipady=10, sticky='w')
        self.bar_value = tk.IntVar()
        ttk.Progressbar(bar_container, variable=self.bar_value, length=200).grid(padx=[0, 20], pady=[10, 0])
        
        self.button = ttk.Button(bar_container, text='Mostrar', command=self.clicked)
        self.button.grid(row=0, column=2, pady=[10, 0])

        led_container = ttk.Labelframe(self, text='Leds')
        led_container.grid(row=1, column=0, padx=30, pady=30)

        self.led_1 = Checkbox(led_container, text='led 1')
        self.led_1.configure(command=lambda: self.send_led(self.led_1))
        self.led_1.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_2 = Checkbox(led_container, text='led 2')
        self.led_2.configure(command=lambda: self.send_led(self.led_2))
        self.led_2.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_3 = Checkbox(led_container, text='led 3')
        self.led_3.configure(command=lambda: self.send_led(self.led_3))
        self.led_3.grid(row=1, column=2, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_4 = Checkbox(led_container, text='led 4')
        self.led_4.configure(command=lambda: self.send_led(self.led_4))
        self.led_4.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_5 = Checkbox(led_container, text='led 5')
        self.led_5.configure(command=lambda: self.send_led(self.led_5))
        self.led_5.grid(row=2, column=0, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_6 = Checkbox(led_container, text='led 6')
        self.led_6.configure(command=lambda: self.send_led(self.led_6))
        self.led_6.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_7 = Checkbox(led_container, text='led 7')
        self.led_7.configure(command=lambda: self.send_led(self.led_7))
        self.led_7.grid(row=2, column=2, padx=10, pady=10, ipadx=10, ipady=10)

        self.led_8 = Checkbox(led_container, text='led 8')
        self.led_8.configure(command=lambda: self.send_led(self.led_8))
        self.led_8.grid(row=2, column=3, padx=10, pady=10, ipadx=10, ipady=10)


    def send_led(self, led):
      if self.arduino:
        arduino.write_led(self.arduino, led)
      else:
        print('Puerto serial no disponible')

    def show_pot_value(self):
      while self.isRun:
        value = arduino.read_potentiometer(self.arduino)
        if value: self.bar_value.set(value)
          
    def clicked(self):
      if self.isRun: return 
      if self.arduino:
        self.isRun = True
        Thread(target=self.show_pot_value).start()
      else: print('Puerto serial no disponible')

    def close(self):
      self.isRun = False
      if self.arduino: self.arduino.close()
      self.main_window.quit()
