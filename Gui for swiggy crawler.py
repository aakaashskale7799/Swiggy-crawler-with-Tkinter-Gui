# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:40:02 2020

@author: User
"""
import tkinter as tk
from swiggy_crawler import * 
#root=Tk()
#from swiggycr import *
#import Tkinter as Tk
master = tk.Tk()
def city_res():
    p=e1.get()
    link(p)
def all_city():
    q=e2.get()
    new(q)

tk.Label(master, 
         text="Enter city link to get all restraurant links ").grid(row=0)
tk.Label(master, 
         text="Enter swiggy link to download all city links  ").grid(row=1)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=10)
tk.Button(master, 
          text='get restraurant link of particular city ', command=city_res).grid(row=0, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(master, 
          text='get all city of india', command=all_city).grid(row=1, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.mainloop()
