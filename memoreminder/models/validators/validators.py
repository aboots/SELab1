from django.core.validators import RegexValidator, FileExtensionValidator

mobile_number_validator = RegexValidator(
    regex=r'^(09\d{9})$',
    message="شماره موبایل باید ۱۱ رقم(اعداد انگلیسی) و به فرم 09XXXXXXXXX باشد."
)