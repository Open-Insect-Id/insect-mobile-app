import flet as ft


def running_platform(page: ft.Page) -> str:
    return page.platform.name