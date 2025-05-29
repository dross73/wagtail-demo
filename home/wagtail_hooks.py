# wagtail_hooks.py

from wagtail.admin.userbar import AccessibilityItem
from wagtail import hooks

# Create a custom accessibility checker by extending the built-in AccessibilityItem
class CustomAccessibilityItem(AccessibilityItem):
    axe_run_only = [
        "wcag2a",  # Basic WCAG 2.0 A-level checks
        "wcag2aa",  # Includes AA-level checks like contrast
        "wcag21a",  # WCAG 2.1 A-level (includes newer rules)
        "wcag21aa",  # WCAG 2.1 AA-level
        "best-practice",  # Includes common-sense usability checks
    ]
    axe_rules = {
        "color-contrast": {"enabled": True},  # Flags low contrast text
        "image-alt": {"enabled": True},  # Flags missing alt attributes
    }

# Update the function to accept the `page` argument
@hooks.register("construct_wagtail_userbar")
def replace_accessibility_item(request, items, page):
    items[:] = [
        CustomAccessibilityItem() if isinstance(i, AccessibilityItem) else i
        for i in items
    ]
