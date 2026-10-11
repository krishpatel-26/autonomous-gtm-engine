import re
import unicodedata

def normalize_email(email: str) -> str:
    return unicodedata.normalize("NFKC", email).strip().casefold()

def normalize_company_name(name: str) -> str:
    value = unicodedata.normalize("NFKC", name).casefold()
    value = re.sub(r"[^\w\s]", " ", value)
    return re.sub(r"\s+", " ", value).strip()

def is_duplicate_prospect(candidate: dict, existing: list[dict]) -> bool:
    email = normalize_email(str(candidate.get("email", "")))
    company = normalize_company_name(str(candidate.get("company", "")))
    for prospect in existing:
        other_email = normalize_email(str(prospect.get("email", "")))
        other_company = normalize_company_name(str(prospect.get("company", "")))
        if email and other_email and email == other_email:
            return True
        if company and other_company and company == other_company:
            return True
    return False
