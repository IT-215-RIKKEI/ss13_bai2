from pydantic import BaseModel, field_validator
from typing import Optional

class BoardingSlotCreateDTO(BaseModel):
    slot_number: str
    room_size: str
    price_per_day: float
    status: str = "VACANT"

    @field_validator("room_size")
    @classmethod
    def validate_room_size(cls, v):
        if v not in ("SMALL", "MEDIUM", "LARGE"):
            raise ValueError("room_size chỉ được nhận SMALL, MEDIUM hoặc LARGE")
        return v

    @field_validator("price_per_day")
    @classmethod
    def validate_price_per_day(cls, v):
        if v <= 0:
            raise ValueError("price_per_day phải lớn hơn 0")
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v):
        if v not in ("VACANT", "OCCUPIED"):
            raise ValueError("status chỉ được nhận VACANT hoặc OCCUPIED")
        return v

class BoardingSlotUpdateDTO(BaseModel):
    slot_number: Optional[str] = None
    room_size: Optional[str] = None
    price_per_day: Optional[float] = None
    status: Optional[str] = None

    @field_validator("room_size")
    @classmethod
    def validate_room_size(cls, v):
        if v is not None and v not in ("SMALL", "MEDIUM", "LARGE"):
            raise ValueError("room_size chỉ được nhận SMALL, MEDIUM hoặc LARGE")
        return v

    @field_validator("price_per_day")
    @classmethod
    def validate_price_per_day(cls, v):
        if v is not None and v <= 0:
            raise ValueError("price_per_day phải lớn hơn 0")
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v):
        if v is not None and v not in ("VACANT", "OCCUPIED"):
            raise ValueError("status chỉ được nhận VACANT hoặc OCCUPIED")
        return v

class BoardingSlotResponseDTO(BaseModel):
    id: int
    slot_number: str
    room_size: str
    price_per_day: float
    status: str

    class Config:
        from_attributes = True
