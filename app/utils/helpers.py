"""
Helper utility functions
"""

from datetime import datetime
from typing import Any, Dict, Optional
import re


def format_currency(amount: float) -> str:
    """Format amount as Philippine Peso currency."""
    return f"₱{amount:,.2f}"


def format_date(date: datetime) -> str:
    """Format datetime as readable string."""
    return date.strftime("%B %d, %Y at %I:%M %p")


def validate_phone_number(phone: str) -> bool:
    """Validate Philippine phone number format."""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Check if it's a valid Philippine mobile number
    # Should start with 09 and be 11 digits total
    if len(digits) == 11 and digits.startswith('09'):
        return True
    
    # Check if it's a valid Philippine landline
    # Should start with area code and be 10-11 digits total
    if len(digits) in [10, 11] and not digits.startswith('09'):
        return True
    
    return False


def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent XSS."""
    if not text:
        return ""
    
    # Remove potentially dangerous characters
    text = text.strip()
    text = re.sub(r'[<>"\']', '', text)
    
    return text


def calculate_total_amount(quantity: int, unit_price: float) -> float:
    """Calculate total amount for a sale."""
    return round(quantity * unit_price, 2)


def is_low_stock(quantity: int, min_stock_level: int) -> bool:
    """Check if stock is low."""
    return quantity <= min_stock_level


def generate_reference_number(prefix: str = "REF") -> str:
    """Generate a unique reference number."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{timestamp}"


def paginate_results(items: list, page: int = 1, per_page: int = 20) -> Dict[str, Any]:
    """Paginate a list of items."""
    total_items = len(items)
    total_pages = (total_items + per_page - 1) // per_page
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    paginated_items = items[start_index:end_index]
    
    return {
        "items": paginated_items,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }
    }
