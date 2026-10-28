"""Blood donation management system module."""

import os
import tempfile
from datetime import date, timedelta

OFFICER_PASSWORD = os.getenv("OFFICER_PASSWORD")
donors = []
stock = {
    "A+": 0, "A-": 0, "B+": 0, "B-": 0,
    "O+": 0, "O-": 0, "AB+": 0, "AB-": 0,
}
COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "A-": ["A-", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "B-": ["B-", "O-"],
    "AB+": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
    "AB-": ["AB-", "A-", "B-", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
}


def register_donor(
    donor_name, blood_group, age, last_donation=None, notes=None
):
    """Register a new donor if age and blood group are valid."""
    if notes is None:
        notes = []
    if blood_group not in stock:
        raise ValueError("Unknown blood group")
    if age < 18 or age > 65:
        notes.append(f"{donor_name} is not eligible because of age")
        return False
    donors.append(
        {"name": donor_name, "group": blood_group, "last": last_donation}
    )
    return True


def can_donate(donor):
    """Check if a registered donor is eligible to donate today."""
    if donor["last"] is None:
        return True
    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a blood donation and update inventory stock."""
    for donor in donors:
        if donor["name"] == donor_name and can_donate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Calculate total units available for a patient blood group."""
    if patient_group not in COMPATIBLE:
        return 0
    return sum(stock[group] for group in COMPATIBLE[patient_group])


def is_universal(blood_group):
    """Check if blood group is universal donor (O-) or recipient (AB+)."""
    return blood_group in {"O-", "AB+"}


def low_stock(threshold=2):
    """Return blood groups with units below the specified threshold."""
    return [group for group, units in stock.items() if units < threshold]


def donor_sheet_path():
    """Create a secure temporary file for the donor sheet and return path."""
    # Helper kept for the lab: not called by the demo
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".csv", delete=False
    ) as temp_file:
        return temp_file.name


def notify_donors(phone_list):
    """Notify donors via SMS safely without executing shell commands."""
    # Helper kept for the lab: not called by the demo
    for phone in phone_list:
        print(f"Sending notification SMS to {phone}")


def main():
    """Demonstrate blood donation management workflows."""
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)
    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")
    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())  # below 2 units
    eligible = [donor["name"] for donor in donors if can_donate(donor)]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
