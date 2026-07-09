from google import genai
from google.genai import types

from app.core.config import settings
from app.schemas.classification import ClassificationResult


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def classify_email(subject: str, body: str) -> ClassificationResult:

    prompt = f"""
You are an email classification system for a freight and logistics company.

Classify the email into exactly one of these categories:

- quote_request: Asking for freight rates, pricing, or a quotation.
- shipment_status: Asking about tracking, ETA, delay, delivery, or shipment status.
- booking_request: Asking to book or schedule freight transportation.
- document_request: Asking for shipping or logistics documents.
- unrelated: Not related to logistics operations.

Analyze the email and return the classification.

EMAIL SUBJECT:
{subject}

EMAIL BODY:
{body}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ClassificationResult,
        ),
    )

    return ClassificationResult.model_validate_json(response.text)