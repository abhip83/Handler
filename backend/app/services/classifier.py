from google import genai
from google.genai import types

from app.core.config import settings
from app.schemas.classification import ClassificationResult


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def classify_email(subject: str, body: str) -> ClassificationResult:

    prompt = f"""
You are an email classification system for a freight and logistics company.

Classify the email into exactly one of these categories:

- quote_request:
  The sender is asking for freight rates, pricing, costs, or a quotation.

- shipment_status:
  The email concerns an existing shipment, delivery, or freight incident.
  This includes tracking, ETA, delays, delivery confirmation, POD confirmation,
  damaged freight, claims related to a shipment, and requests for a claim reference.

- booking_request:
  The sender wants to create, confirm, schedule, or change a freight booking.

- document_request:
  The sender is specifically asking for a shipping document or copy of a document,
  such as a bill of lading, commercial invoice, packing list, customs document,
  certificate, or other shipment paperwork.

- unrelated:
  The email is not related to freight or logistics operations.

IMPORTANT CLASSIFICATION RULES:

1. If the main purpose is to ask what happened to an existing shipment,
   delivery, damage incident, or claim, classify it as shipment_status.

2. A POD confirmation request about whether delivery occurred is shipment_status.
   A request for a copy of the POD document is document_request.

3. A request for the status or reference of a damaged-freight claim is
   shipment_status, even if words such as "reference" or "confirmation" appear.

4. Use document_request only when the main purpose is to obtain an actual
   document, file, certificate, or paperwork.

Analyze the sender's main intent, not individual keywords.

EMAIL SUBJECT:
{subject}

EMAIL BODY:
{body}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ClassificationResult,
        ),
    )

    return ClassificationResult.model_validate_json(response.text)