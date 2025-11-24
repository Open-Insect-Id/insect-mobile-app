import sys

import flet as ft
import flet_permission_handler as fph

from utils.on_picker_result import on_picker_result
from utils.running_platform import running_platform


def main(page: ft.Page):

    picker = ft.FilePicker()
    ph = fph.PermissionHandler()

    page.overlay.append(ph)
    page.overlay.append(picker)

    storage_permission_granted = False

    current_platform = page.platform

    if current_platform == ft.PagePlatform.IOS or current_platform == ft.PagePlatform.MACOS:
        print("Cannot run on Apple software", file=sys.stderr)
        sys.exit(1)

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

    picker.on_result = lambda e: on_picker_result(e, page)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.PHOTO, on_click=browse_photo
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text(f"You are running {running_platform(page)}", size=30, weight=ft.FontWeight.BOLD),
                    # Need this one cause for some reason it makes the text above centered
                    ft.Container(
                        None,
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
