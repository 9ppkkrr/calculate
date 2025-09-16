import flet as ft
import math
import re

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__(
            text=text,
            expand=expand,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10
            )
        )

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        super().__init__(text, expand)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text):
        super().__init__(text)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text):
        super().__init__(text)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK

def main(page: ft.Page):
    expression = ft.Text(
        value="",
        size=30,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        expand=True
    )

    def button_click(e):
        btn_text = e.control.text

        if btn_text == "AC":
            expression.value = ""
        elif btn_text == "=":
            try:
                expr = expression.value
                expr = expr.replace("^", "**")
                expr = expr.replace("√", "math.sqrt")
                expr = expr.replace("÷", "/")
                expr = expr.replace("×", "*")
                expr = expr.replace("sin", "math.sin(math.radians")
                expr = expr.replace("cos", "math.cos(math.radians")
                expr = expr.replace("tan", "math.tan(math.radians")
                expr = expr.replace("log", "math.log10")
                expr = expr.replace("ln", "math.log")

                expr = re.sub(r'(math\.sin\(math\.radians)([^\)]+)', r'\1(\2))', expr)
                expr = re.sub(r'(math\.cos\(math\.radians)([^\)]+)', r'\1(\2))', expr)
                expr = re.sub(r'(math\.tan\(math\.radians)([^\)]+)', r'\1(\2))', expr)

                pattern = r'(\d+)!'
                while re.search(pattern, expr):
                    m = re.search(pattern, expr)
                    n = m.group(1)
                    expr = expr[:m.start()] + f"math.factorial({n})" + expr[m.end():]

                result = eval(expr, {"math": math})
                expression.value = str(result)
            except Exception:
                expression.value = "Error"
        elif btn_text == "+/-":
            try:
                val = float(expression.value)
                val = -val
                expression.value = str(val)
            except:
                pass
        else:
            expression.value += btn_text
        page.update()

    buttons = [
        ["AC", "+/-", "%", "÷", "√"],
        ["7", "8", "9", "×", "^"],
        ["4", "5", "6", "-", "sin"],
        ["1", "2", "3", "+", "cos"],
        ["0", ".", "=", "log", "tan"],
        ["(", ")", "!", "ln", "%"]
    ]

    def create_button(text):
        if text in ["AC", "+/-", "%", "÷", "×", "-", "+", "=", "^", "√", "sin", "cos", "tan", "log", "ln", "!", "(", ")"]:
            btn = ActionButton(text)
        else:
            btn = DigitButton(text)
        btn.on_click = button_click
        return btn

    rows = []
    for row in buttons:
        controls = [create_button(text) for text in row]
        rows.append(ft.Row(controls=controls, spacing=8))

    container = ft.Container(
        width=400,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.border_radius.all(20),
        padding=20,
        content=ft.Column(
            controls=[
                ft.Container(content=expression, alignment=ft.alignment.center_right, height=60),
                *rows
            ],
            spacing=10
        )
    )

    page.add(container)
    page.bgcolor = ft.Colors.BLACK
    page.update()

ft.app(target=main)
