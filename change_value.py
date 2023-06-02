import flet as ft
from change_Txt import change_Txt_

d = ft.TextField(
    hint_text="Agfidr",
    width=150,
    color=ft.colors.WHITE,
    border_color=ft.colors.BLUE,
)

face = ft.TextField(
    hint_text="Agfidr",
    width=150,
    color=ft.colors.WHITE,
    border_color=ft.colors.BLUE,
)


def readonlyTrue(num):
    d.read_only = num


def change_value_(page_):
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
                                ft.Row([ft.Text("Index Finger", width=100), face]),
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
                                    "save",
                                    width=100,
                                    on_click=page_.go("change_Txt"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=300,
                        ),
                        ft.Column(
                            [
                                ft.Row([ft.Text("Face", width=100), d]),
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
