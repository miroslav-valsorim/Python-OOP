from Shop.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"