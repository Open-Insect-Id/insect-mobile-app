import flet as ft

from utils.running_platform import running_platform


def main(page: ft.Page):

    picker = ft.FilePicker()
    ph = ft.PermissionHandler()

    page.overlay.append(ph)
    page.overlay.append(picker)

    photo_permission_granted = False
    storage_permission_granted = False
    supports_camera = True  # Have to replace  with real check

    current_platform = page.platform

    if current_platform == ft.PagePlatform.IOS or ft.PagePlatform.MACOS:
        exit("Cannot run on apple software")

    def on_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            image = ft.Image(src_base64=e.files[0].data, width=300, height=300)
            page.add(image)

    def browse_photo(e):
        """
        :param e: nothing, IDK what's that
        :return: nothing; just updates the permission granted state if not granted
        """
        nonlocal storage_permission_granted
        if storage_permission_granted or current_platform != ft.PagePlatform.ANDROID:
            picker.pick_files(
                allow_multiple=False,
                file_type=ft.FilePickerFileType.IMAGE,
            )
        else:
            storage_permission_granted = ph.request_permission(ft.PermissionType.MANAGE_EXTERNAL_STORAGE)

    def request_permission_and_take_photo(e):
        """
        Request android permission to access camera / take a photo
        (RN it only picks a photo using the file picker, but it should take a photo in real time)
        :param e: nothing
        """
        nonlocal photo_permission_granted
        photo_permission_granted = ph.request_permission(ft.PermissionType.CAMERA)
        if (photo_permission_granted and supports_camera) or current_platform != ft.PagePlatform.ANDROID:
            picker.pick_files(
                allow_multiple=False,
                file_type=ft.FilePickerFileType.IMAGE,
            )
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Camera permission not granted or not supported"))
            page.snack_bar.open = True
            page.update()

    picker.on_result = on_picker_result

    browse_photo_button = ft.ElevatedButton(
        "Browse photo" if photo_permission_granted else " Grand storage permission",
        on_click=browse_photo
    )

    take_photo_button = ft.ElevatedButton(
        "Take photo" if photo_permission_granted else " Grant Camera permission",
        on_click=request_permission_and_take_photo
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text(f"You are running {running_platform(page)}", size=30, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content = None,
                        height=50
                    ),
                    take_photo_button,
                    browse_photo_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
        )
    )


ft.app(main)
