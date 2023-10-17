import flet as ft

def main(page: ft.Page):
    page.title = "A320 FBW Performance"
    # page.bgcolor = "#1a1c1e"
    page.bgcolor = "#CCCCCC"
    # page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def slopeCalc(e):
        a = int(rwy_in_use.value)
        b = int(opposit.value)
        c = int(length_rwy_in_use.value)
        slopeResult.value = str(round((((a-b)/c)*100),2))
        page.update()   
    
    title = ft.Text(value="TakeOff Performance", text_align=ft.TextAlign.CENTER, size=20)
    
    rwy_in_use = ft.TextField(label="THR elevation in use")
    opposit = ft.TextField(label="Opposit THR elevation")
    length_rwy_in_use = ft.TextField(label="Length of RWY in use")   
    slopeButton = ft.TextButton(text="Calculate", on_click=slopeCalc) 
    slopeResult = ft.TextField(label="Slope")     

    # txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)
    
    page.add(
        title,
        ft.Row(controls=(rwy_in_use,opposit,length_rwy_in_use), alignment=ft.alignment.center),
        slopeButton,
        slopeResult
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
