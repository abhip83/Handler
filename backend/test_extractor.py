from app.services.extractor import extract_shipment_information

result = extract_shipment_information(
    subject="Rate Request | Mumbai to Hamburg | 40HC",
    body="""
Hi Team,

Please quote for one 40HC container.

Origin: Mumbai
Destination: Hamburg
Cargo: Textile Machinery
Weight: 8500 KG
Pickup Date: July 20

Regards,
ABC Logistics
""",
)

print(result)