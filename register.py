import flet as ft
from req_data import req_data


def register(page_):
    page_.theme_mode = ft.ThemeMode.DARK

    user_name = ft.TextField(
        label="Username",
        width=310,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE,
    )

    password = ft.TextField(
        label="Password",
        width=310,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE,
        password=True,
        can_reveal_password=True,
    )

    first_name = ft.TextField(
        label="First Name",
        width=150,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE,
    )

    last_name = ft.TextField(
        label="Last Name",
        width=150,
        color=ft.colors.WHITE,
        border_color=ft.colors.BLUE,
    )

    req_data_ = req_data(user_name, password, first_name, last_name)

    row = ft.Row(
        [first_name, last_name],
        alignment=ft.MainAxisAlignment.CENTER,
    )
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
                        ft.Text("Register", size=30, weight=ft.FontWeight.BOLD),
                        row,
                        user_name,
                        password,
                        ft.ElevatedButton(
                            "Register",
                            width=300,
                            on_click=lambda _: page_.go("/registered_succesful"),
                        ),
                        ft.ElevatedButton(
                            "Back",
                            width=300,
                            on_click=lambda _: [req_data_, page_.go("/")],
                        ),
                    ],
                ),
            )
        ]
    )
