import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลขทันสมัย"
    page.bgcolor = "#121212"
    page.window_width = 320
    page.window_height = 500
    page.window_resizable = False

    expression = ft.Text(value="", size=40, color="white", text_align="right")

    def button_click(e):
        btn = e.control.data
        if btn == "C":
            expression.value = ""
        elif btn == "=":
            try:
                expression.value = str(eval(expression.value))
            except:
                expression.value = "Error"
        else:
            expression.value += btn
        page.update()

    def create_button(text, color="#1f1f1f", text_color="white", col=1):
        return ft.Container(
            content=ft.TextButton(
                text,
                data=text,
                on_click=button_click,
                style=ft.ButtonStyle(
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    bgcolor=color,
                    color=text_color,
                ),
            ),
            width=70 * col + 10 * (col - 1),
            height=70,
        )

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    rows = []
    for row in buttons:
        r = ft.Row(
            controls=[
                create_button(btn, color="#2c2c2c" if btn not in "+-*/=C" else "#f57c00")
                for btn in row
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        rows.append(r)

    page.add(
        ft.Container(
            content=expression,
            padding=20,
            alignment=ft.alignment.center_right,
            height=100,
        ),
        *rows,
    )

ft.app(target=main)
