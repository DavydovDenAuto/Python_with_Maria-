import tkinter as tk

class View:
    _CANVAS_WIDTH = 500
    _CANVAS_HEIGHT = 300

    _CANVAS_BACKGROUND_COLOR = "orange"
    
    _WINDOW_TITLE = "Rover"

    def __init__(self):
        self._init_root()
        self._init_canvas()
        self._init_canvas_items()        
        self._init_event_handlers()


    def _init_root(self):
        self._root = tk.Tk()
        self._root.title(self._WINDOW_TITLE)
        self._root.resizable(width=False, height=False)


    def _init_canvas(self):
        self._canvas = tk.Canvas(self._root, 
                                 width=self._CANVAS_WIDTH, 
                                 height=self._CANVAS_HEIGHT,
                                 background=self._CANVAS_BACKGROUND_COLOR)
        self._canvas.pack()


    def _init_canvas_items(self):
        self._rover = RoverView(self._canvas, 
                                self._CANVAS_WIDTH / 2,
                                self._CANVAS_HEIGHT / 2)


    def _init_event_handlers(self):
        self._mouse_click_event_handler = None
        self._canvas.bind("<Button-1>", self._on_mouse_click)


    def set_mouse_click_event_handler(self, event_handler):
        self._mouse_click_event_handler = event_handler


    def show(self):
        self._root.mainloop()


    def move_rover_to(self, normal_x, normal_y):
        x = normal_x * self._CANVAS_WIDTH
        y = normal_y * self._CANVAS_HEIGHT

        self._rover.move_to(x, y)


    def _on_mouse_click(self, event):
        if not self._mouse_click_event_handler:
            return

        normal_x = event.x / self._CANVAS_WIDTH
        normal_y = event.y / self._CANVAS_HEIGHT

        self._mouse_click_event_handler(normal_x, normal_y)


class RoverView:
    _WIDTH = 30
    _HEIGHT = 30

    _BODY_COLOR = "black"

    def __init__(self, canvas, x, y):
        self._canvas = canvas
        self._body_item = self._canvas.create_oval(0, 0, 
                                                        self._WIDTH, self._HEIGHT, 
                                                        fill=self._BODY_COLOR, width=0)
        self.move_to(x, y)


    def move_to(self, x, y):
        self._x = x
        self._y = y

        self._canvas.moveto(self._body_item, x - self._WIDTH / 2, y - self._HEIGHT / 2)