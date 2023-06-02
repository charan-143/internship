import flet as ft


def registered_succesful(page_):
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
                        ft.Image(src="2.png", width=300, height=300),
                        ft.Text(
                            "Registered Succesfully!",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.ElevatedButton(
                            "Login", width=300, on_click=lambda _: page_.go("/login")
                        ),
                    ],
                ),
            )
        ]
    )
