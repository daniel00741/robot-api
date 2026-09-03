from src.schemas.license import (
    LicenseValidationRequest,
    LicenseValidationResponse,
)


AUTHORIZED_EMAIL = "test@deltabot.ai"
AUTHORIZED_MT5_ACCOUNT_ID = "12345678"
AUTHORIZED_EA_NAME = "DeltaBot-XAUUSD-Short"


def validate_license_simulated(
    request: LicenseValidationRequest,
) -> LicenseValidationResponse:
    """
    Validación simulada temporal.

    En la versión real esta función consultará PostgreSQL y validará:
    - cliente existente
    - email activo
    - licencia activa
    - cuenta MT5 asociada al email
    - robot autorizado para esa licencia
    - fecha de expiración
    - versión mínima permitida del EA
    """

    email_normalized = request.email.lower().strip()
    mt5_account_id_normalized = request.mt5_account_id.strip()
    ea_name_normalized = request.ea_name.strip()

    is_authorized = (
        email_normalized == AUTHORIZED_EMAIL
        and mt5_account_id_normalized == AUTHORIZED_MT5_ACCOUNT_ID
        and ea_name_normalized == AUTHORIZED_EA_NAME
    )

    if is_authorized:
        return LicenseValidationResponse(
            authorized=True,
            customer_status="active",
            license_status="active",
            mt5_account_allowed=True,
            message="License validation simulated successfully",
        )

    return LicenseValidationResponse(
        authorized=False,
        customer_status="unknown",
        license_status="invalid",
        mt5_account_allowed=False,
        message="Email, MT5 account, or robot is not authorized",
    )