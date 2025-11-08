"""Test module for Gemini AI integration review."""


def calculate_ratio(items_processed: int, total_items: int) -> float:
    """
    Calculate the ratio of processed items to the total number of items.

    Args:
        items_processed: The number of items that have been processed.
        total_items: The total number of items.

    Returns:
        The ratio as a floating-point number. Returns 0.0 if total_items is 0.
    """
    # A clear problem: what if total_items is 0?
    # Gemini should be able to spot this potential ZeroDivisionError.
    if total_items <= 0:
        raise ValueError("total_items must be a positive number.")
    return items_processed / total_items


def process_data(data_list: list[int]) -> list[int]:
    """
    Squares each number in a list of integers.

    Args:
        data_list: A list of integers.

    Returns:
        A new list containing the squared numbers.
    """
    # An inefficient way to create a list of squares.
    # Gemini might suggest a list comprehension: [x * x for x in data_list].
    # Ruff's PERF401 rule already caught this.
    return [x * x for x in data_list]
