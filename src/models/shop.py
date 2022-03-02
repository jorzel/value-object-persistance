from typing import Optional

from value_objects.email import Email


class Shop:
    def __init__(self):
        self.email_address: Optional[str] = None

    @property
    def email(self) -> Optional[Email]:
        return Email(self.email_address)

    @email.setter
    def email(self, email_address: str) -> None:
        self.email_address = Email(email_address).address
