"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""

    return record[1]

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""

    return (coordinate[0], coordinate[1])

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""

    if convert_coordinate(azara_record[1]) == rui_record[1]:
        return True
    return False 

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""

    report = ""
    
    for item in combined_record_group: 
        name = item[0]
        location = item[2]
        coordinate = item[3]
        quadrant = item[-1]
        report += f"('{name}', '{location}', {coordinate}, '{quadrant}')\n"

    return report