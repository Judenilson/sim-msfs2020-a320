import flet as ft

def main(page: ft.Page):
    page.title = "A320 FBW Performance"
    page.bgcolor = "#1a1c1e"
    # page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    title = ft.Text(value="TakeOff Performance", text_align=ft.TextAlign.CENTER, size=20)
    
    slope = ft.TextField(label="THR elevation in use")
    opposit = ft.TextField(label="Opposit THR elevation")
    rwy_in_use = ft.TextField(label="Length of RWY in use")    

    # txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    
    page.add(
        title,
        ft.Row(controls=(slope,opposit,rwy_in_use), alignment=ft.alignment.center)
    )

ft.app(target=main)
