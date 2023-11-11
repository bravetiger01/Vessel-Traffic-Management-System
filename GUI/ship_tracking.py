from tkinter import *
from tkintermapview import TkinterMapView

root = Tk()
root.geometry('500x500')
root.title('Map')


# Map Widget
map_widget = TkinterMapView(root, width=600, height=600, corner_radius=0)
map_widget.pack(fill='both', expand=True)

# Google
map_widget.set_tile_server('https://mt0.google.com/vt/lyrs=m&h1=en&x={x}&y={y}&z={z}%s=Ga', max_zoom=22)
map_widget.set_address('India', marker=True)

root.mainloop()