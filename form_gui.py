import flet as ft

def main(page: ft.Page):
    page.title = "ฟอร์มลงทะเบียน"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ช่องกรอกข้อมูล
    name_field = ft.TextField(label="ชื่อ", width=300)
    team_field = ft.TextField(label="ทีม", width=300)
    phone_field = ft.TextField(label="เบอร์โทรศัพท์", width=300, keyboard_type=ft.KeyboardType.PHONE)

    # ข้อความแสดงผล
    result_text = ft.Text("", size=16)

    # ฟังก์ชันเมื่อกด "ส่งข้อมูล"
    def submit_clicked(e):
        name = name_field.value.strip()
        team = team_field.value.strip()
        phone = phone_field.value.strip()

        if name and team and phone:
            result_text.value = f"✅ ลงทะเบียนสำเร็จ!\nชื่อ: {name}\nทีม: {team}\nเบอร์โทร: {phone}"
            result_text.color = "green"
        else:
            result_text.value = "⚠️ กรุณากรอกข้อมูลให้ครบถ้วน"
            result_text.color = "red"
        page.update()

    # ฟังก์ชันเมื่อกด "ล้างข้อมูล"
    def clear_clicked(e):
        name_field.value = ""
        team_field.value = ""
        phone_field.value = ""
        result_text.value = ""
        page.update()

    # ปุ่ม
    submit_button = ft.ElevatedButton(text="บันทึก", on_click=submit_clicked, icon=ft.Icons.CHECK)
    clear_button = ft.OutlinedButton(text="ล้างข้อมูล", on_click=clear_clicked, icon=ft.Icons.DELETE)

    # เพิ่ม widget ลงในหน้า
    page.add(
        ft.Column(
            [
                name_field,
                team_field,
                phone_field,
                ft.Row([submit_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
                result_text
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# รันแอป
ft.app(target=main)
