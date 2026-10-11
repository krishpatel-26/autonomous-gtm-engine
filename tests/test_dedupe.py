from app.dedupe import is_duplicate_prospect, normalize_company_name, normalize_email

def test_email_deduplication_ignores_case_and_whitespace():
    assert normalize_email(" Sales@Example.com ") == "sales@example.com"

def test_company_name_normalization():
    assert normalize_company_name(" Acme, Inc. ") == "acme inc"

def test_duplicate_email_detected():
    assert is_duplicate_prospect({"email":"A@EXAMPLE.COM"}, [{"email":"a@example.com"}])

def test_blank_fields_do_not_match_every_record():
    assert not is_duplicate_prospect({}, [{"email":"", "company":""}])
