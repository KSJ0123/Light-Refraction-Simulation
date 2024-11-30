import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def update_graph(*args):
    try:
        n1 = float(n1_var.get())
        n2 = float(n2_var.get())
        angle = float(angle_var.get())

        theta1 = np.radians(angle) 
        theta2 = np.arcsin(n1 * np.sin(theta1) / n2)

        x = [-10, 0, 10]
        y = [10 / np.tan(theta1), 0, -10 / np.tan(theta2)]
        xr = [0, 10]
        yr = [0, 10 / np.tan(theta1)]

        ax.clear()

        ax.plot(x, y, color='b', lw=3)  
        ax.plot(xr, yr, color='b', lw=2)  
        ax.axhline(y=0, color='k', ls='--')  
        ax.axvline(x=0, color='k', ls='--')  

        
        angle1 = np.linspace(0, theta1, 10) + np.pi / 2
        x1 = 2 * np.cos(angle1)
        y1 = 2 * np.sin(angle1)
        ax.plot(x1, y1, color='k')
        ax.plot(-x1, y1, color='k')

        angle2 = np.linspace(0, theta2, 10) + 3 * np.pi / 2
        x2 = 2 * np.cos(angle2)
        y2 = 2 * np.sin(angle2)
        ax.plot(x2, y2, color='k')

        ax.text(x1[-1], y1[0] + 1, r'$\theta_1$', size=15)
        ax.text(-x1[-1] / 2, y1[0] + 1, r"$\theta'_1$", size=15)
        ax.text(x2[-1] / 3, y2[-1] - 2, r'$\theta_2$', size=15)

        
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_xticks([])
        ax.set_yticks([])

        
        canvas.draw()

    except Exception as e:
        
        ax.clear()
        ax.set_title("pls check ur input")
        canvas.draw()



root = tk.Tk()
root.title("Light Refraction Simulation")
root.geometry("600x700")


fig = Figure(figsize=(6, 6))
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()


n1_var = tk.StringVar()
n2_var = tk.StringVar()
angle_var = tk.StringVar()


n1_var.trace("w", update_graph) 
n2_var.trace("w", update_graph)  
angle_var.trace("w", update_graph)  

tk.Label(root, text="n1 (굴절률 1)").pack()
tk.Entry(root, textvariable=n1_var).pack()

tk.Label(root, text="n2 (굴절률 2)").pack()
tk.Entry(root, textvariable=n2_var).pack()

tk.Label(root, text="Angle (입사각)").pack()
tk.Entry(root, textvariable=angle_var).pack()

# 초기값 설정
n1_var.set("1.5")
n2_var.set("1.0")
angle_var.set("45")

root.mainloop()