import flet as ft

from src.utils.user_popup import show_android_popup


def on_picker_result(e: ft.FilePickerResultEvent, page: ft.Page):
    if e.files:
        page.add(ft.Text(e.files))
        file_path = e.files[0].path
        # Read file bytes manually
        page.add(ft.Text(file_path))
        if file_path is not None:
            with open(file_path, "rb") as f:
                file_bytes = f.read()
            import base64
            base64_data = base64.b64encode(file_bytes).decode("utf-8")
            src_base64 = "data:image/png;base64," + base64_data
            image = ft.Image(src_base64=src_base64, width=300, height=300)
            page.add(image)
        else:
            show_android_popup(
                page = page,
                text = "File path selected is empty",
                title = "Error"
            )
        page.update()
