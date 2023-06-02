import flet as ft
import base64
import cv2

cap = cv2.VideoCapture(0)


class Countdown(ft.UserControl):
    def __init__(self):
        super().__init__()

    def did_mount(self):
        self.update_timer()

    def update_timer(self):
        while True:
            _, frame = cap.read()
            # frame = cv2.resize(frame,(400,400))
            _, im_arr = cv2.imencode(".png", frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        self.img = ft.Image(border_radius=ft.border_radius.all(10))
        return self.img


count = Countdown()


buttons = ft.Row(
    controls=[
        ft.ElevatedButton(
            "capture",
            width=300,
        ),
        ft.ElevatedButton("stop", width=300),
    ],
)

section = ft.ResponsiveRow(
    [
        ft.Container(
            margin=ft.margin.only(bottom=0),
            content=ft.Row(
                [
                    ft.Card(
                        elevation=5,
                        content=ft.Container(
                            bgcolor=ft.colors.WHITE24,
                            padding=10,
                            border_radius=ft.border_radius.all(20),
                            content=ft.Column([Countdown(), buttons]),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
        ft.Column(
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment="end",
            controls=[
                ft.Image(src="stack.png", width=70, height=70),
            ],
        ),
    ],
)


def main(page: ft.Page):
    page.padding = 50
    page.window_left = page.window_left + 10
    page.theme_mode = ft.ThemeMode.DARK
    page.add(section)


if __name__ == "__main__":
    ft.app(target=main)
    cap.release()
    cv2.destroyAllWindows()
