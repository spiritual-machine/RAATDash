import flet as ft

def Login(router):

    def validate(e):
        page = e.page
        if all([Username.value, Pass.value]):
            Submit.disabled = False
            page.update()
        else:
            Submit.disabled = True
            page.update()
    
    def submitform(e):
        page = e.page
        page.clean()
        page.add(ft.Text(value="Success!"))
        page.update()

    def registerclick(e):
        page = e.page
        page.route = "/register"
        page.update()

    
    WelcomeHeader = ft.Text("Login", size=30)
    Username = ft.TextField(label="Username", width = 400, bgcolor="white")
    Pass = ft.TextField(label = "Password", password=True, can_reveal_password=True, width = 400, bgcolor="white")
    Submit = ft.IconButton(icon="arrow_forward", icon_size=40, disabled=True)
    Register = ft.TextButton(text="Not yet registered? Click here to sign up.", on_click=registerclick)

    Username.on_change = validate
    Pass.on_change = validate
    Submit.on_click = submitform

    content = ft.Container(
            content=
                ft.Column(
                    controls = [WelcomeHeader, Username, Pass, ft.Container(content = Submit, alignment= ft.alignment.center_right),
                                ft.Container(content = Register, alignment=ft.alignment.center_left)],
                    alignment = ft.alignment.center
            ),
            padding = 40,
            bgcolor = "white",
            border_radius = 5,
            
        )
    return content
                