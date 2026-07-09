from app.services.classifier import classify_email


result = classify_email(
    subject="Rate Request – FCL Shanghai to Los Angeles",
    body="""
    Hi team,

    Could you send us a rate for 2x40HC from Shanghai
    to Los Angeles? Cargo is ready around July 20.

    Thanks,
    Linda
    """
)


print(result)
print(result.category)
print(result.confidence)