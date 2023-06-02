import flet as ft
from welcome import welcome
from register import register
from registered_succesful import registered_succesful
from login import login
from select_option import select_option
from change_value import change_value_
from change_Txt import change_Txt_


def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    welcome(page),
                ],
            )
        )
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        register(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/registered_succesful":
            page.views.append(
                ft.View(
                    "/registered_succesful",
                    [
                        registered_succesful(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        login(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/select_option":
            page.views.append(
                ft.View(
                    "/select_option",
                    [
                        login(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/change_value":
            page.views.append(
                ft.View(
                    "/change_value",
                    [
                        change_value_(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        if page.route == "/change_Txt":
            page.views.append(
                ft.View(
                    "/change_Txt",
                    [
                        change_value_(page),
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.theme_mode = ft.ThemeMode.DARK


ft.app(target=main, view=ft.WEB_BROWSER)
