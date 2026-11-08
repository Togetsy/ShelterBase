from dataclasses import dataclass

@dataclass
class Owner:
    id: int
    name: str
    phone: str
    address: str
    email: str | None
