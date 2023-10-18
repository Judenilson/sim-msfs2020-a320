import flet as ft


def main(page: ft.Page):
    page.title = "A320 FBW Performance"
    page.window_resizable = False
    page.window_width = 500
    page.window_height = 880
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(
        color_scheme_seed="#5739ef",
    )

    def slope_calculate(e):
        if rwy_in_use.value == "" or opposit.value == "" or length_rwy_in_use.value == "":
            validate_entry(e)
            return
        a = int(rwy_in_use.value)
        b = int(opposit.value)
        c = int(length_rwy_in_use.value)
        if c == 0:
            validate_entry(e)
            return
        slope_result.value = str(round((((a-b)/c)*100), 2))
        page.update()
        
    def slope_reset(e):
        rwy_in_use.value = ""
        opposit.value = ""
        length_rwy_in_use.value = ""
        slope_result.value = ""
        page.update()

    def validate_entry(e):
        alert = ft.AlertDialog(title=ft.Text("Enter a valid number!", text_align=ft.alignment.center))
        e.control.page.dialog = alert
        alert.open = True
        e.control.page.update()

    def validate_only_real_number(e):
        count = len(e.control.value)
        # analisa apenas se existir algo digitado
        if count > 0:
            # verifica se não é um número negativo
            if e.control.value[0] != "-":
                if not e.control.value[-1].isdigit():
                    validate_entry(e)
                    e.control.value = e.control.value[:-1]
            # Se for negativo, queremos analisar após o sinal de menos.
            elif count > 1:
                if not e.control.value[-1].isdigit():
                    validate_entry(e)
                    e.control.value = e.control.value[:-1]
        page.update()

    def validate_only_positive_number(e):
        count = len(e.control.value)
        # analisa apenas se existir algo digitado
        if count > 0:
            if e.control.value[-1] == ",":
                if (e.control.value[-1] in e.control.value[:-1]):
                    validate_entry(e)
                    e.control.value = e.control.value[:-1]                
                    page.update()
                    return False
                return True
            if not e.control.value[-1].isdigit():
                validate_entry(e)
                e.control.value = e.control.value[:-1]                
                page.update()
                return False
        return True

    def validate_degrees(e):
        count = len(e.control.value)
        # analisa apenas se existir algo digitado
        if not validate_only_positive_number(e):
            return
        if count > 0:
            if int(e.control.value) < 1 or int(e.control.value) > 360:
                validate_entry(e)
                e.control.value = ""
        page.update()

# objetos ------------------------
    # Titulo -------------------------
    title = ft.Text(value="TakeOff Performance", style="displaySmall", )
    
    # Seção do Slope -------------------------
    rwy_in_use = ft.TextField(label="THR elevation in use", suffix_text="ft", width=150, max_length=5, on_change=validate_only_real_number)
    opposit = ft.TextField(label="Opposit THR elevation", suffix_text="ft", width=150, max_length=5, on_change=validate_only_real_number)
    length_rwy_in_use = ft.TextField(label="Length of RWY in use", suffix_text="ft", width=150, max_length=5, on_change=validate_only_real_number)
    slope_button = ft.ElevatedButton("Calculate", on_click=slope_calculate)
    slope_button_reset = ft.OutlinedButton("Reset", on_click=slope_reset)
    slope_result = ft.TextField(label="SLOPE", bgcolor=ft.colors.SECONDARY_CONTAINER, read_only=True, width=150, suffix_text="%", text_size=30)

    # Seção do Clima -------------------------
    wind_direction = ft.TextField(label="Wind Direction", suffix_text="°", width=150, max_length=3, on_change=validate_degrees)
    wind_speed = ft.TextField(label="Wind Speed", suffix_text="kt", width=150, max_length=2, on_change=validate_only_positive_number)
    oat = ft.TextField(label="OAT", suffix_text="°C", width=150, max_length=3, on_change=validate_only_real_number)
    qnh = ft.TextField(label="QNH", suffix_text="hPa", width=150, max_length=4, on_change=validate_only_positive_number)
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

    # Seção da Aeronave -------------------------
    tow = ft.TextField(label="TOW", suffix_text="Ton", width=100, on_change=validate_only_positive_number)
    tocg = ft.TextField(label="TOCG", suffix_text="%", width=100, on_change=validate_only_positive_number)
    thrust = ft.Dropdown(
        label="Thrust",
        width=100,
        options=[
            ft.dropdown.Option("FLEX"),
            ft.dropdown.Option("TOGA"),
        ])
    flaps = ft.Dropdown(
        label="Flaps",
        width=100,
        options=[
            ft.dropdown.Option("1+F"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
        ])
    air_cond = ft.Switch(
        label="Air Cond.",
        width=150,
        value=True,
        label_position=ft.LabelPosition.LEFT
        )
    anti_ice = ft.Switch(
        label="Anti Ice",
        width=150,
        value = False,
        label_position=ft.LabelPosition.LEFT
        )

# Render ------------------------
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
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            run_spacing=10,
        ),
        ft.Row(
            [
                tow,
                tocg,
                thrust,
                flaps,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            run_spacing=10,
        ),
        ft.Row(
            [                
                air_cond,
                anti_ice,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            run_spacing=10,
        )
    )


ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER, port=8550) # Executar o app no Browser
