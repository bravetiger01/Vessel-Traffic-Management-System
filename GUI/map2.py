from tkinter import *
from tkintermapview import TkinterMapView

root = Tk()
root.geometry('500x500')
root.title('Google Map View')

# Map Inside Window
map_widget = TkinterMapView(root, width=600, height=400
                            ,corner_radius=0)
map_widget.pack(fill='both', expand=True)

# Google Url
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)


root.mainloop()