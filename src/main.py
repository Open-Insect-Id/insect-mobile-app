import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    picker = ft.FilePicker()
    page.overlay.append(picker)
    ph = ft.PermissionHandler()
    page.overlay.append(ph)

    def on_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            image = ft.Image(src_base64=e.files[0].data, width=300, height=300)
            page.add(image)

    def browse_photo(e):
        picker.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
            # with_data=True
        )

    def request_permissions(e):
        granted = ph.request_permission(ft.PermissionType.MANAGE_EXTERNAL_STORAGE)
        # Optionally handle permission result
        if granted:
            page.add(ft.Text("Permission granted"))
        else:
            page.add(ft.Text("Permission denied"))
        page.update()

    page.add(
        ft.ElevatedButton("Request Storage Permission", on_click=request_permissions)
    )


    picker.on_result = on_picker_result

    take_photo_button = ft.ElevatedButton(
        "Browse photo",
        on_click=browse_photo
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text("Welcome", size=30, weight=ft.FontWeight.BOLD),
                    take_photo_button,
                    ft.Container(
                        counter,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
        )
    )


ft.app(main)
