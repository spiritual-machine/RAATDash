import flet as ft
from flet import Theme
from views.routes import router

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = Theme(color_scheme_seed='Orange')
    page.bgcolor = "Orange"
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/login')

ft.app(target=main, assets_dir="assets")