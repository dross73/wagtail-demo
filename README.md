# CDS Test Magazine - Wagtail Form Integration

## Overview

This project implements a modular, styled order form for **CDS Test Magazine**, built with **Wagtail (Django CMS)** and **Tailwind CSS**. It allows users to:

- Choose a subscription offer
- Enter billing and credit card details
- Submit the form
- Receive a confirmation message after submission

The form is rendered server-side and submits through Django, avoiding client-side CORS issues.

---

## Features

- **Wagtail page model (`CDSFormPage`)** with custom `serve()` logic
- **Tailwind CSS** for responsive, mobile-friendly layout
- **Form POST submission via Django backend**
- **Modular template structure** using `{% extends %}` and `{% include %}`
- **Offer card interactivity** using simple JavaScript
- **Backend submission to [webhook.site](https://webhook.site)** using Python `requests`
- **Success message rendering** using a `submitted` context flag

---

## File Structure

```
home/
├── models.py
├── templates/
│   └── home/
│       ├── cds_base.html           # Shared layout (HTML head, header, footer)
│       ├── cds_form_page.html      # The form page template
│       └── includes/
│           ├── offer_cards.html    # Subscription options
│           └── form_fields.html    # Name, address, and credit card inputs
```

---

## Template Logic

### Base Layout

`cds_base.html` provides a reusable structure with:

- `<head>` section including Tailwind
- Header and footer
- A `{% block content %}` placeholder for page-specific content

### Form Page

`cds_form_page.html`:

- Extends the base layout
- Renders a thank-you message if `submitted` is true
- Includes:
  - `offer_cards.html` (offer options with JS interactivity)
  - `form_fields.html` (buyer details)

---

## Data Flow

1. User selects an offer → JavaScript sets the `selected_offer` hidden input
2. User fills out the form and submits it
3. Django receives the `POST` request in `CDSFormPage.serve()`
4. Data is printed to the console and sent to `webhook.site` as JSON
5. The form re-renders with a thank-you message using `submitted=True`

---

## Notes

- The form uses `method="POST"` and `{% csrf_token %}` to comply with Django’s security model.
- JavaScript is **only used for offer card selection** — not for form submission.
- The webhook URL can be swapped out in `models.py` for real integrations later.
- File structure is modular and easy to maintain or extend.

---

## Setup Notes (Optional)

- Requires a running Wagtail project (`wagtail start`)
- All templates go under `home/templates/home/`
- Create a `CDSFormPage` via Wagtail admin to view the form

---
