"""Expense Report — starter code.

This script works. It reads transactions.csv, categorizes the rows,
and prints a report showing per-category totals.

It also has all of its logic crammed into one big main() function with
hard-coded filenames, a hard-coded category dict, and print() statements
woven into the calculations.

Your job is to refactor this code IN PLACE, by moving the right logic
into the four helper shapes below, in response to the change requests in
the README. Keep everything in this one file.

When you're done, the script should produce the SAME output (TOTAL = $613.87)
on the original inputs — the change requests should not change observable
behavior on the starting CSV.

DO NOT add any external libraries. Standard library only.
"""

import json
from pathlib import Path


# -----------------------------------------------------------------------------
# TODO Part 1 — fill these in. (See README "Part 1 — Add JSON support".)
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Skip lines that don't have 4 comma-separated fields.
    """
    lines = text.strip().splitlines()
    rows = []
    for line in lines[1:]:  # skip header
        parts = line.strip().split(",")
        if len(parts) != 4:
            continue
        date, vendor, amount, note = parts
        rows.append({"date": date, "vendor": vendor, "amount": amount, "note": note})
    return rows


def parse_json(text: str) -> list[dict]:
    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.
    Input is JSON text — same fields as the CSV, just JSON-shaped.
    """
    data = json.loads(text)
    rows = []
    for item in data:
        rows.append({
            "date": item["date"],
            "vendor": item["vendor"],
            "amount": item["amount"],
            "note": item["note"]
        })
    return rows


# -----------------------------------------------------------------------------
# TODO Part 2 — fill this in. (See README "Part 2 — Configurable categories".)
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    """Return the category for `vendor` based on `categories`.

    `categories` maps {category_name: [keyword, keyword, ...]}.
    A vendor matches a category if any of the keywords appears in the
    vendor name (case-insensitive). Return "other" if no category matches.
    """
    vendor_upper = vendor.upper()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.upper() in vendor_upper:
                return category
    return "other"

# -----------------------------------------------------------------------------
# TODO Part 3 — fill this in. (See README "Part 3 — A pure pipeline".)
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    """Return {category_name: total_amount} for a list of parsed rows.

    Pure: must NOT open files, read stdin, or print anything.
    """
    raise NotImplementedError("Part 3: implement build_report")


# -----------------------------------------------------------------------------
# main() — I/O lives here. Once Parts 1-3 are done, this should shrink to
# just the I/O glue: read files, call parse_*, call build_report, print.
# Right now it has everything inline.
# -----------------------------------------------------------------------------

def main():
    rows = []
    with open("data/transactions.csv") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            rows.append(parts)

    categories = json.loads(Path("data/categories.json").read_text())

    totals = {}
    for date, vendor, amount, _ in rows:
        cat = "other"
        for key, c in categories.items():
            if key in vendor.upper():
                cat = c
        totals[cat] = totals.get(cat, 0.0) + float(amount)

    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()
