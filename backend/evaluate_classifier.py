import json
import time
from collections import defaultdict
from pathlib import Path

from app.services.classifier import classify_email


DATASET_PATH = Path(__file__).parent.parent / "datasets" / "freight_emails.json"

REQUEST_DELAY_SECONDS = 4


def load_emails():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["emails"]


def evaluate():
    emails = load_emails()

    total = len(emails)
    correct = 0
    errors = 0

    category_stats = defaultdict(
        lambda: {"total": 0, "correct": 0}
    )

    results = []

    print(f"\nEvaluating {total} emails...\n")

    for index, email in enumerate(emails, start=1):
        expected = email["category"]

        category_stats[expected]["total"] += 1

        try:
            prediction = classify_email(
                subject=email["subject"],
                body=email["body"],
            )

            predicted = prediction.category.value
            is_correct = predicted == expected

            if is_correct:
                correct += 1
                category_stats[expected]["correct"] += 1

            results.append({
                "id": email["id"],
                "subject": email["subject"],
                "expected": expected,
                "predicted": predicted,
                "confidence": prediction.confidence,
                "correct": is_correct,
            })

            symbol = "PASS" if is_correct else "FAIL"

            print(
                f"[{index}/{total}] {symbol} | "
                f"Expected: {expected} | "
                f"Predicted: {predicted} | "
                f"Confidence: {prediction.confidence:.2f}"
            )

        except Exception as error:
            errors += 1

            results.append({
                "id": email["id"],
                "subject": email["subject"],
                "expected": expected,
                "predicted": None,
                "confidence": None,
                "correct": False,
                "error": str(error),
            })

            print(f"[{index}/{total}] ERROR | {error}")

        if index < total:
            time.sleep(REQUEST_DELAY_SECONDS)

    accuracy = (correct / total) * 100 if total else 0

    print("\n" + "=" * 60)
    print("HANDLER CLASSIFIER EVALUATION")
    print("=" * 60)

    print(f"Total emails:       {total}")
    print(f"Correct predictions:{correct}")
    print(f"API errors:         {errors}")
    print(f"Overall accuracy:   {accuracy:.2f}%")

    print("\nPER-CATEGORY ACCURACY")

    for category, stats in category_stats.items():
        category_accuracy = (
            stats["correct"] / stats["total"] * 100
            if stats["total"]
            else 0
        )

        print(
            f"{category:20} "
            f"{stats['correct']}/{stats['total']} "
            f"({category_accuracy:.2f}%)"
        )

    output_path = Path(__file__).parent / "evaluation_results.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)

    print(f"\nDetailed results saved to: {output_path}")


if __name__ == "__main__":
    evaluate()