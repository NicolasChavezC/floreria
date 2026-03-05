from PyQt6 import QtWidgets, uic

class LoginController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)
    def handle_login(self):
        username = self.window.txt_user.text()
        password = self.window.txt_key.text()
        if username == "Lily" and password == "1234":
            self.window.login_successful.emit()
        else:
            QtWidgets.QMessageBox.Warning(self.window, "Abarrotes TEC - ERROR", "Login Incorrecto")