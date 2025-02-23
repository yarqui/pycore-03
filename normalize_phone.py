import re

raw_numbers = ["    +38(050)123-32-34  ", "++38067\\t12)(3 4567\\n", "     0503451234","(050)8889900","+1954-111-22-22","38050 111 22 11   "]

def normalize_phone(phone_number: str) -> str:
    sanitization_pattern = r'(?!^)\+|[^\d+]' # keep digits and "+" (only if it is at the start)
    phone_number = re.sub(sanitization_pattern, '', phone_number)

    if phone_number.startswith('+'):
        if phone_number.startswith('+380'):
            return phone_number
        return phone_number
    
    if phone_number.startswith('380'):
        return f'+{phone_number}'

    return f'+38{phone_number}'

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print(sanitized_numbers)

