import flet as ft


def main(page: ft.Page):
    page.title = "A320 FBW Performance"
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(
        color_scheme_seed="#5739ef",
    )

    alert = ft.AlertDialog(
        title=ft.Text("Put a valid number!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def slope_calculate(e):
        if rwy_in_use.value == "" or opposit.value == "" or length_rwy_in_use.value == "":
            validate_number(e)
            return
        a = int(rwy_in_use.value)
        b = int(opposit.value)
        c = int(length_rwy_in_use.value)
        if (a < -100) or (a > 5000) or (b < -100) or (b > 5000) or (c < 1) or (c > 20000):
            validate_number(e)
            return
        slope_result.value = str(round((((a-b)/c)*100), 2))
        page.update()

    def slope_reset(e):
        rwy_in_use.value = ""
        opposit.value = ""
        length_rwy_in_use.value = ""
        slope_result.value = ""
        page.update()

    def validate_number(e):
        e.control.page.dialog = alert
        alert.open = True
        e.control.page.update()

    title = ft.Text(value="TakeOff Performance", style="displaySmall", )

    rwy_in_use = ft.TextField(
        label="THR elevation in use", suffix_text="ft", width=150)
    opposit = ft.TextField(label="Opposit THR elevation",
                           suffix_text="ft", width=150)
    length_rwy_in_use = ft.TextField(
        label="Length of RWY in use", suffix_text="ft", width=150)
    slope_button = ft.ElevatedButton("Calculate", on_click=slope_calculate)
    slope_button_reset = ft.OutlinedButton("Reset", on_click=slope_reset)
    slope_result = ft.TextField(
        label="SLOPE", bgcolor=ft.colors.SECONDARY_CONTAINER, read_only=True, width=150, suffix_text="%", text_size=30)

    wind_direction = ft.TextField(
        label="Wind Direction", suffix_text="°", width=150)
    wind_speed = ft.TextField(label="Wind Speed", suffix_text="kt", width=150)
    oat = ft.TextField(label="OAT", suffix_text="°C", width=150)
    qnh = ft.TextField(label="QNH", suffix_text="hPa", width=150)
    rwy_condition = ft.Dropdown(
        label="RWY Condition",
        options=[
            ft.dropdown.Option("Dry"),
            ft.dropdown.Option("Wet"),
            ft.dropdown.Option("Water 6.3mm (1/4 inch)"),
            ft.dropdown.Option("Water 12.7mm (1/2 inch)"),
            ft.dropdown.Option("Slush 6.3mm (1/4 inch)"),
            ft.dropdown.Option("Slush 12.7mm (1/2 inch)"),
            ft.dropdown.Option("Comp. Snow"),
        ])

    tow = ft.TextField(label="TOW", suffix_text="Ton", width=150)
    thrust = ft.Dropdown(
        label="Thrust",
        width=150,
        options=[
            ft.dropdown.Option("FLEX"),
            ft.dropdown.Option("TOGA"),
        ])
    flaps = ft.Dropdown(
        label="Flaps",
        width=150,
        options=[
            ft.dropdown.Option("1+F"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
        ])
    air_cond = ft.Dropdown(
        label="Air Cond.",
        width=150,
        options=[
            ft.dropdown.Option("ON"),
            ft.dropdown.Option("OFF"),
        ])
    anti_ice = ft.Dropdown(
        label="Anti Ice",
        width=150,
        options=[
            ft.dropdown.Option("ON"),
            ft.dropdown.Option("OFF"),
        ])
    tocg = ft.TextField(label="TOCG", suffix_text="%", width=150)

    page.add(
        ft.Container(
            title,
            alignment=ft.alignment.top_center,
            margin=10
        ),
        ft.Row(
            [
                rwy_in_use,
                opposit,
                length_rwy_in_use
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            run_spacing=10,
        ),
        ft.Row(
            [
                slope_button,
                slope_button_reset,
                slope_result,
            ],
            alignment=ft.MainAxisAlignment.END
        ),
        ft.Row(
            [
                wind_direction,
                wind_speed,
                oat
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            run_spacing=10,
        ),
        ft.Row(
            [
                qnh,
                rwy_condition
            ],
        ),
        ft.Row(
            [
                tow,
                tocg,
                thrust,
            ],
        ),
        ft.Row(
            [
                flaps,
                air_cond,
                anti_ice,
            ],
        )
    )


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
