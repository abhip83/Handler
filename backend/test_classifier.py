from app.services.classifier import classify_email


failed_emails = [
    {
        "id": 16,
        "subject": "POD Confirmation Needed – Delivery #90144",
        "body": """
 {
    "id": 16,
    "subject": "POD Confirmation Needed – Delivery #90144",
    "expected": "shipment_status",
    "predicted": "document_request",
    "confidence": 0.95,
    "correct": false
  }
""",
    },
    {
        "id": 21,
        "subject": "RE: Damaged Freight – Claim Reference Needed",
        "body": """
  {
    "id": 21,
    "subject": "RE: Damaged Freight – Claim Reference Needed",
    "expected": "shipment_status",
    "predicted": "document_request",
    "confidence": 0.95,
    "correct": false
  }
""",
    },
]


for email in failed_emails:
    print(f"\nTesting Email ID: {email['id']}")
    print(f"Subject: {email['subject']}")

    result = classify_email(
        subject=email["subject"],
        body=email["body"],
    )

    print(f"Predicted: {result.category.value}")
    print(f"Confidence: {result.confidence}")
    print(
        "Result:",
        "PASS" if result.category.value == "shipment_status" else "FAIL"
    )