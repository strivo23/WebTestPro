"""Synthetic data used by tests; no real credentials or personal data."""
VALID_USER = {"name": "Alex Morgan", "email": "alex@example.com", "password": "DemoPass123"}
INVALID_USER = {"email": "alex@example.com", "password": "WrongPass123"}
REGISTRATION_USER = {"name": "Taylor Test", "email": "taylor@example.test", "password": "StrongPass123"}
INVALID_EMAILS = ["plainaddress", "missing-at.example.test", "user@invalid"]
WEAK_PASSWORDS = ["short", "1234567"]
