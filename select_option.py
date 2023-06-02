import flet as ft


def select_option(page_):
    row = ft.Row(
        [
            ft.ElevatedButton("BLE SIGNAL", width=205, height=50),
            ft.Text("or"),
            ft.ElevatedButton("GESTURE RECOGNITION", width=205, height=50),
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
                        row,
                    ],
                ),
            )
        ]
    )
