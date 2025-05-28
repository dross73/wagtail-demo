# wagtail_hooks.py

from wagtail.admin.userbar import (
    AccessibilityItem,
)  # Base class for the accessibility checker
from wagtail import hooks  # Used to register our custom behavior into the Wagtail admin


# Create a custom accessibility checker by extending the built-in AccessibilityItem
class CustomAccessibilityItem(AccessibilityItem):
    # Only run these rule sets from the axe-core engine (they map to WCAG standards)
    axe_run_only = [
        "wcag2a",  # Basic WCAG 2.0 A-level checks
        "wcag2aa",  # Includes AA-level checks like contrast
        "wcag21a",  # WCAG 2.1 A-level (includes newer rules)
        "wcag21aa",  # WCAG 2.1 AA-level
        "best-practice",  # Includes common-sense usability checks
    ]

    # Enable specific rules manually — even if they're normally skipped by default
    axe_rules = {
        "color-contrast": {"enabled": True},  # Flags low contrast text
        "image-alt": {"enabled": True},  # Flags missing alt attributes
    }


# Replace Wagtail's default accessibility item with our custom one
@hooks.register("construct_wagtail_userbar")
def replace_accessibility_item(request, items):
    # Replace only the default AccessibilityItem with our CustomAccessibilityItem
    items[:] = [
        CustomAccessibilityItem() if isinstance(i, AccessibilityItem) else i
        for i in items
    ]
