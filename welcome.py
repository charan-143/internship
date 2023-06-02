import flet as ft


def welcome(page_):
    row = ft.Row(
        [
            ft.ElevatedButton(
                "Register", width=110, on_click=lambda _: page_.go("/register")
            ),
            ft.Text("or"),
            ft.ElevatedButton(
                "Login", width=110, on_click=lambda _: page_.go("/login")
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    return ft.ResponsiveRow(
        [
            ft.Container(
                width=450,
                height=700,
                padding=40,
                content=ft.Column(
                    horizontal_alignment="center",
                    alignment="center",
                    controls=[
                        ft.Text("Welcome to Flet!", size=40, weight=ft.FontWeight.BOLD),
                        ft.Text("caption"),
                        row,
                    ],
                ),
            )
        ]
    )
