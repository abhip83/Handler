from google import genai
from google.genai import types

from app.core.config import settings
from app.schemas.extraction import ShipmentExtraction

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def extract_shipment_information(
    subject: str,
    body: str,
) -> ShipmentExtraction:

    prompt = f"""
You are an AI assistant specialized in freight forwarding and logistics.

Extract shipment information from the email.

Return ONLY valid JSON.

Email Subject:
{subject}

Email Body:
{body}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ShipmentExtraction,
            temperature=0,
        ),
    )

    return ShipmentExtraction.model_validate_json(response.text)