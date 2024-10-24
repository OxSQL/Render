import tkinter, win32api
from win32gui import GetWindowLong, SetWindowLong, SetLayeredWindowAttributes, EnableWindow


class Overlay():
    Window = None
    OverlayName = None
    Render = None


    def __init__(self, OverlayName):
        self.OverlayName = OverlayName
        self.CreateOverlay()


    def CreateOverlay(self):
        self.Window = tkinter.Tk()
        self.Window.overrideredirect(True)
        self.Window.title(self.OverlayName)
        self.Window.wm_attributes("-topmost", True)
        self.Window.wm_attributes("-toolwindow", True)
        self.Window.wm_attributes("-transparentcolor", "white")
        self.Window.config(bg = "white")

        self.Render = tkinter.Canvas(self.Window, width = win32api.GetSystemMetrics(0), height = win32api.GetSystemMetrics(1), bg = "white", highlightthickness = 0, takefocus = 0)
        self.Render.pack(expand = True)


    def BeginRender(self):
        self.Render.delete("all")


    def EndRender(self):
        self.Render.pack()
        self.Render.update()


    def RGBtoHEX(self, R, G, B):
        return f'#{R:02x}{G:02x}{B:02x}'


    def DrawLine(self, x1, y1, x2, y2, Color):
        self.Render.create_line(x1, y1, x2, y2, fill = Color)


    def DrawRectangle(self, x1, y1, x2, y2, Color):
        self.Render.create_rectangle(x1, y1, x2, y2, outline = Color)


    def DrawRectangle(self, x, y, w, h, Color):
        self.DrawLine(x, y, x + w, y, Color)
        self.DrawLine(x, y, x, y + h, Color)
        self.DrawLine(x + w, y, x + w, y + h, Color)
        self.DrawLine(x, y + h, x + w, y + h, Color)


    def DrawFilledRectangle(self, x, y, w, h, h2, Color):
        self.Render.create_rectangle(x - 1, y - 1, x + w + 1, y + h + 1, outline = self.RGBtoHEX(0, 0, 0))
        self.Render.create_rectangle(x + w, y + h, x, y + (h - (h2)), fill = Color, outline = Color)


    def DrawText(self, x, y, text, Color):
        self.Render.create_text(x, y, text = text, fill = Color, font = ("Calibri bold", 10))


    def DrawCircle(self, x, y, r, Color):
        self.Render.create_oval(x - r, y - r, x + r, y + r, outline = Color)


        