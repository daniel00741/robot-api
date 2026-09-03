from fastapi import APIRouter

from src.schemas.license import (
    LicenseValidationRequest,
    LicenseValidationResponse,
)
from src.services.license_service import validate_license_simulated


router = APIRouter(
    prefix="/v1/license",
    tags=["license"],
)


@router.post(
    "/validate",
    response_model=LicenseValidationResponse,
)
async def validate_license(
    request: LicenseValidationRequest,
) -> LicenseValidationResponse:
    return validate_license_simulated(request)