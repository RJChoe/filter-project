from django.db import models
from django.contrib.auth.models import User
from .constants.choices import (
CATEGORY_CHOICES,
CATEGORY_OTHER,
FLAT_ALLERGEN_LABEL_MAP,
)

##CATEGORY_CHOICES define single field on Django model
## use: category field on AllergenExposure model
## structure: flat list of 2-tuples (database_key, human_label)
## database value: database_key (e.g., 'food', 'fragrance', 'other') saved to database
## purpose: categorize AllergenExposure model objects themselves

# Allergy model
# User model (Django's built-in User)
# UserAllergy model to link users to their allergies)
class AllergenExposure(models.Model):
    """
    Pre-defined list of common allergens/ingredients.
    Admins can manage this list, users select from it.
    """
    # Primary Selection: The broad category (User selects this first)   
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_OTHER,
        help_text='Generic allergen category'
    )
    
    # Secondary Selection: The specific allergen/ingredient KEY
    # selected based on the category chosen above
    allergen_name = models.CharField(
        max_length=50,
        choices=[],
        # leave choices=[] because the choices are category-dependent 
        # and are filtered dynamically in the forms.
        blank=True,
        null=True,
        help_text='Specific allergen (choices filtered via category)'
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Inactive allergies won't be shown in user selection"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Allergy"
        verbose_name_plural = "Allergies"
        ordering = ['category', 'allergen_name']
        
    def __str__(self):
        # Display as "Category: Allergen Label"
        category_display = self.get_category_display()
        
        if self.allergen_name:
            allergen_label = FLAT_ALLERGEN_LABEL_MAP.get(self.allergen_name, self.allergen_name)

            return f"{category_display}: {allergen_label}"
        else:
            return f"{category_display}: [No Allergen Selected]"
