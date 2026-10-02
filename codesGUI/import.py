

from nicegui import ui

ui.label("Testing...")

ui.label("This is Button!")
ui.button("BUTTON", on_click=lambda: ui.notify('button was pressed'))
ui.run
