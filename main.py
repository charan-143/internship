import flet as ft
import flet_material as ftm
import cv2
from PIL import Image
from register import register
from login import login
from registered_succesful import registered_succesful
from select_option import select_option
from welcome import welcome
from button1 import button_page_
from change_value import change_value_


def main(page):
    page.title = "Hello World"
    page.theme_mode = ft.ThemeMode.DARK

    welcome_page = welcome(page)
    registered_succesful_page = registered_succesful(page)
    registerpage = register(page)
    loginpage = login(page)
    select_option_page = select_option(page)
    button_page = button_page_(page)
    change_value = change_value_(page)
    page.add(change_value)


ft.app(target=main, view=ft.WEB_BROWSER)
