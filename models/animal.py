from dataclasses import dataclass

@dataclass
class Animal:
    id: int
    name: str
    species_id: int
    sex: str
    age: int | None
    status: str
    owner_id: int | None

    species_name: str | None = None
    owner_name: str | None = None
    owner_phone: str | None = None
    
