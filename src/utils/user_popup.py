import flet as ft

def show_android_popup(
    page: ft.Page,
    text: str,
    title: str = "Alert",
    confirm_text: str = "OK",
    on_confirm = None
):
    def close_dialog(e):
        page.dialog.open = False
        page.update()
        if on_confirm:
            on_confirm()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(text),
        actions=[
            ft.ElevatedButton(confirm_text, on_click=close_dialog)
        ]
    )
    page.dialog = dialog
    page.dialog.open = True
    page.update()
