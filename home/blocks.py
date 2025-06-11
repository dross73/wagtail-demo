from wagtail import blocks


# This custom block creates a heading element that editors can insert anywhere on the page.
# It's based on StructBlock, which allows you to group fields into a structured, reusable block.
class HeadingBlock(blocks.StructBlock):
    heading_text = blocks.CharBlock(
        required=True, max_length=255, help_text="Enter the heading text to display."
    )

    # Meta class defines how this block behaves in the Wagtail admin
    class Meta:
        icon = "title"  # Wagtail icon in the editor
        label = "Heading"  # Shown in the block picker
        template = "blocks/heading_block.html"  # Template used to render this block


# A block representing a single offer card with its data
class SingleOfferCardBlock(blocks.StructBlock):
    issue_label = blocks.CharBlock(required=True, help_text="e.g., 6 issues")
    price = blocks.CharBlock(required=True, help_text="e.g. #12.95")
    offer_value = blocks.CharBlock(required=True, help_text="e.g., 6")
    features = blocks.ListBlock(
        blocks.CharBlock(label="Feature"), help_text="Add each bullet point shown on the card"
    )

    class Meta:
        icon = "Snippet"
        label = "Offer Card"
        template = "blocks/single_offer_card.html"


# A block that contains a list of offer cards.
class OfferCardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(SingleOfferCardBlock())

    class Meta:
        icon = "Placeholder"
        label = "Offer Cards"
        template = "blocks/offer_cards_block.html"
