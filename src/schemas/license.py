from pydantic import BaseModel, EmailStr, Field


class LicenseValidationRequest(BaseModel):
    email: EmailStr
    mt5_account_id: str = Field(..., min_length=3, max_length=30)
    broker_name: str = Field(..., min_length=2, max_length=100)
    server_name: str = Field(..., min_length=2, max_length=100)
    ea_name: str = Field(..., min_length=2, max_length=100)
    ea_version: str = Field(..., min_length=1, max_length=30)


class LicenseValidationResponse(BaseModel):
    authorized: bool
    customer_status: str
    license_status: str
    mt5_account_allowed: bool
    message: str