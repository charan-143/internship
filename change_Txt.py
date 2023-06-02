import flet as ft


def change_Txt_(page_, face):
    return ft.ResponsiveRow(
        [
            ft.Container(
                width=450,
                height=700,
                padding=40,
                content=ft.Row(
                    alignment="center",
                    controls=[
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("grgtgvft Finger", width=100),
                                        ft.TextField(
                                            hint_text=face,
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                            read_only=True,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Thumb Finger", width=100),
                                        ft.TextField(
                                            hint_text="Agfidr",
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                            read_only=True,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Middle Finger", width=100),
                                        ft.TextField(
                                            hint_text="Agfidr",
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                            read_only=True,
                                        ),
                                    ]
                                ),
                                # TODO: complete the rediredction
                                ft.ElevatedButton(
                                    "save", width=100, on_click=lambda: page_.go()
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=300,
                        ),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("Face", width=100),
                                        ft.TextField(
                                            hint_text="Agfidr",
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Right hand", width=100),
                                        ft.TextField(
                                            hint_text="Agfidr",
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                            read_only=True,
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text("Left hand", width=100),
                                        ft.TextField(
                                            hint_text="Agfidr",
                                            width=150,
                                            color=ft.colors.WHITE,
                                            border_color=ft.colors.BLUE,
                                            read_only=True,
                                        ),
                                    ]
                                ),
                                ft.ElevatedButton("edit", width=100),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=300,
                        ),
                    ],
                ),
            )
        ]
    )
