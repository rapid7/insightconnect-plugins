from dataclasses import dataclass, fields

from typing import Optional


@dataclass(frozen=True, eq=True)
class UserEvent:
    attributes: dict
    dataType: str
    Id: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    Alias: Optional[str] = None
    IsActive: Optional[bool] = None
    LoginTime: Optional[str] = None
    UserId: Optional[str] = None
    LoginType: Optional[str] = None
    LoginUrl: Optional[str] = None
    SourceIp: Optional[str] = None
    Status: Optional[str] = None
    Application: Optional[str] = None
    Browser: Optional[str] = None

    def __hash__(self):
        exclude_fields = ["attributes"]
        return hash(tuple(getattr(self, field.name) for field in fields(self) if field.name not in exclude_fields))
