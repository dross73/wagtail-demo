from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from django.shortcuts import (
    render,
)  # Used to return a page with a template and dynamic data (like the form)
import requests  # Used to send HTTP requests (like a form POST)
from django.http import HttpResponse
import json


class HomePage(Page):
    pass


class AboutPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.URLField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("body"),
        FieldPanel("button_text"),
        FieldPanel("button_link"),
        FieldPanel("image"),
    ]


class MagazineOrderPage(Page):
    # Optional rich text intro at the top of the page
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),  # Add the intro field to the page's admin interface
    ]

    def serve(self, request):
        from .forms import MagazineOrderForm

        # if the page was submitted with POST (the form was filled on and sent)
        if request.method == "POST":
            form = MagazineOrderForm(request.POST)  # Bind form to submitted data

            # Check if the form is valid (all required fields filled out correctly)
            if form.is_valid():
                # Send form data to Webhook.site
                requests.post(
                    "https://webhook.site/62101cd5-f41d-4357-ac18-012c32206c33",
                    json=form.cleaned_data,  # Use cleaned data from the form
                    headers={
                        "Content-Type": "application/json"
                    },  # Set the content type to JSON
                )

                # For now, re-render the page with a success message
                return render(
                    request,
                    "home/magazine_order_page.html",
                    {
                        "page": self,
                        "form": MagazineOrderForm(),  # Show a fresh form again
                        "success": True,  # Flag we'll use in the template
                    },
                )
        else:
            # If it's a GET request (first time visiting the page)
            # just show a blank form
            form = MagazineOrderForm()

            # Render the page with the blank form

        return render(
            request,
            "home/magazine_order_page.html",
            {
                "page": self,  # Pass the page context to the template
                "form": form,  # Include the empty form
            },
        )


class CDSFormPage(Page):
    # Use Wagtail's default content panels (no custom fields in the CMS for now)
    content_panels = Page.content_panels

    def serve(self, request):
        # Handle form submission (POST)
        if request.method == "POST":
            # Convert form POST data into a standard Python dictionary
            data = request.POST.dict()

            # Print the form data to the terminal for debugging
            print("CDS Form Submission Data:", data)

            try:
                # Send the form data as JSON to the external webhook endpoint
                requests.post(
                    "https://webhook.site/75c7d0b3-907e-4905-b925-35edce1b4177",
                    json=data,
                    headers={"Content-Type": "application/json"},
                )
                submitted = (
                    True  # Flag used to trigger a thank-you message in the template
                )
            except Exception as e:
                print("Webhook error:", e)
                submitted = False  # Only show thank-you if no error

            # Re-render the page after submission with the submitted flag
            return render(
                request,
                "home/cds_form_page.html",
                {"page": self, "submitted": submitted},
            )

        # For GET requests, just render the empty form
        return render(request, "home/cds_form_page.html", {"page": self})
