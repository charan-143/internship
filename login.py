import flet as ft


def login(page_):
    return ft.ResponsiveRow(
        [
            ft.Container(
                width=450,
                height=650,
                padding=20,
                content=ft.Column(
                    horizontal_alignment="center",
                    alignment="center",
                    controls=[
                        ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                        ft.TextField(
                            label="Username",
                            width=310,
                            color=ft.colors.WHITE,
                            border_color=ft.colors.BLUE,
                        ),
                        ft.TextField(
                            label="Password",
                            width=310,
                            color=ft.colors.WHITE,
                            border_color=ft.colors.BLUE,
                        ),
                        ft.ElevatedButton(
                            "login",
                            width=300,
                            on_click=lambda _: page_.go("/select_option"),
                        ),
                        ft.ElevatedButton(
                            "Back", width=300, on_click=lambda _: page_.go("/")
                        ),
                    ],
                ),
            )
        ]
    )
