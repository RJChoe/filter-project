# --- Category Definitions ---
CATEGORY_FOOD = 'food'
CATEGORY_CONTACT = 'contact'
CATEGORY_FRAGRANCE = 'fragrance'
CATEGORY_PRESERVATIVE = 'preservative'
CATEGORY_BOTANICAL = 'botanical'
CATEGORY_SURFACTANT = 'surfactant'
CATEGORY_SUNSCREEN = 'sunscreen'
CATEGORY_ACID = 'acid'
CATEGORY_COLORANT = 'colorant'
CATEGORY_PROTEIN = 'protein'
CATEGORY_OTHER = 'other'

# --- 2. Category Choices (For the Model field) ---
CATEGORY_CHOICES = [
    (CATEGORY_FOOD, 'Food Allergens'),
    (CATEGORY_FRAGRANCE, 'Fragrance Allergens'),
    (CATEGORY_OTHER, 'Other Allergens'), # <-- Category label
]

# --- The actual Choices (Key-Value Pairs for the database) ---

# Food Allergens (example)
FOOD_ALLERGENS = [
    ("peanut", "Peanut"),
    ("tree_nut", "Tree Nut (General)"),
    ("gluten", "Gluten / Wheat"),
    ("dairy", "Dairy / Milk"),
    ("soy", "Soy"),
    ("shellfish", "Shellfish"),
]

# Contact/Topical Allergens (example)
CONTACT_ALLERGENS = [
    ("nickel", "Nickel"),
    ("latex", "Latex"),
    ("lanolin", "Lanolin"),
]

# Fragrance Allergens (based on your example)
FRAGRANCE_ALLERGENS = [
    ("linalool", "Linalool"),
    ("limonene", "Limonene"),
    ("geraniol", "Geraniol"),
    ("citronellol", "Citronellol"),
    ("eugenol", "Eugenol"),
    # ... and so on
]

# Preservatives
PRESERVATIVE_ALLERGENS = [
    ("parabens", "Parabens (Methylparaben, Propylparaben, etc.)"),
    ("formaldehyde", "Formaldehyde"),
    ("formaldehyde_releasers", "Formaldehyde Releasers"),
    ("methylisothiazolinone", "Methylisothiazolinone (MI)"),
    ("methylchloroisothiazolinone", "Methylchloroisothiazolinone (MCI)"),
    ("phenoxyethanol", "Phenoxyethanol"),
    ("benzalkonium_chloride", "Benzalkonium Chloride"),
    ("bronopol", "Bronopol"),
    ("iodopropynyl_butylcarbamate", "Iodopropynyl Butylcarbamate"),
]

# Botanical/Essential oils
BOTANICAL_ALLERGENS = [
    ("tea_tree_oil", "Tea Tree Oil"),
    ("lavender_oil", "Lavender Oil"),
    ("peppermint_oil", "Peppermint Oil"),
    ("eucalyptus_oil", "Eucalyptus Oil"),
    ("rose_oil", "Rose Oil"),
    ("chamomile", "Chamomile"),
    ("ylang_ylang", "Ylang Ylang"),
    ("sandalwood", "Sandalwood"),
    ("bergamot", "Bergamot Oil"),
    ("lemongrass", "Lemongrass Oil"),
]

# Surfactants and emulsifiers
SURFACTANT_ALLERGENS = [
    ("sls", "Sodium Lauryl Sulfate (SLS)"),
    ("sles", "Sodium Laureth Sulfate (SLES)"),
    ("cocamidopropyl_betaine", "Cocamidopropyl Betaine"),
    ("peg_compounds", "PEG Compounds (Polyethylene Glycol)"),
    ("polysorbates", "Polysorbates"),
    ("sodium_lauroyl_sarcosinate", "Sodium Lauroyl Sarcosinate"),
]

# UV filters/Sunscreen ingredients
SUNSCREEN_ALLERGENS = [
    ("oxybenzone", "Oxybenzone (Benzophenone-3)"),
    ("octinoxate", "Octinoxate (Octyl Methoxycinnamate)"),
    ("avobenzone", "Avobenzone"),
    ("octocrylene", "Octocrylene"),
    ("homosalate", "Homosalate"),
    ("titanium_dioxide", "Titanium Dioxide"),
    ("zinc_oxide", "Zinc Oxide"),
]

# Acids and exfoliants
ACID_ALLERGENS = [
    ("glycolic_acid", "Glycolic Acid"),
    ("salicylic_acid", "Salicylic Acid"),
    ("lactic_acid", "Lactic Acid"),
    ("citric_acid", "Citric Acid"),
    ("benzoic_acid", "Benzoic Acid"),
    ("sorbic_acid", "Sorbic Acid"),
]

# Colorants and dyes
COLORANT_ALLERGENS = [
    ("ci_dyes", "CI Dyes (Color Index)"),
    ("fd_c_dyes", "FD&C Dyes"),
    ("carmine", "Carmine (CI 75470)"),
    ("iron_oxides", "Iron Oxides"),
    ("mica", "Mica"),
]

# Proteins and extracts
PROTEIN_ALLERGENS = [
    ("lanolin", "Lanolin (Wool Alcohol)"),
    ("collagen", "Collagen"),
    ("keratin", "Keratin"),
    ("silk_protein", "Silk Protein"),
    ("wheat_protein", "Wheat Protein"),
    ("soy_protein", "Soy Protein"),
    ("beeswax", "Beeswax"),
    ("propolis", "Propolis"),
    ("royal_jelly", "Royal Jelly"),
]

# Other common allergens
OTHER_ALLERGENS = [
    ("retinol", "Retinol/Retinoids"),
    ("vitamin_c", "Vitamin C (L-Ascorbic Acid)"),
    ("niacinamide", "Niacinamide"),
    ("propylene_glycol", "Propylene Glycol"),
    ("butylene_glycol", "Butylene Glycol"),
    ("dimethicone", "Dimethicone"),
    ("tocopherol", "Tocopherol (Vitamin E)"),
    ("alcohol_denat", "Alcohol Denat"),
    ("isopropyl_alcohol", "Isopropyl Alcohol"),
]

# Combined choices with optgroups for forms
ALLERGIES_CHOICES = [
    ("Fragrances", FRAGRANCE_ALLERGENS),
    ("Preservatives", PRESERVATIVE_ALLERGENS),
    ("Botanicals & Essential Oils", BOTANICAL_ALLERGENS),
    ("Surfactants & Emulsifiers", SURFACTANT_ALLERGENS),
    ("Sunscreen Ingredients", SUNSCREEN_ALLERGENS),
    ("Acids & Exfoliants", ACID_ALLERGENS),
    ("Colorants & Dyes", COLORANT_ALLERGENS),
    ("Proteins & Extracts", PROTEIN_ALLERGENS),
    ("Other Ingredients", OTHER_ALLERGENS),
]

## going to remove for a define the individual categories
## and use them to define the choices for the category field.

# --- The Grouped Choice Constant ---
# list of 3-tuples: (database_key, human_readable_label, choice_list)
# useful django form rendering <optgroup> tags
# template iteration (require human readble category label)
ALLERGIES_CHOICES = [
    (CATEGORY_FOOD, 'Food Allergens', FOOD_ALLERGENS),
    (CATEGORY_CONTACT, 'Contact Allergens', CONTACT_ALLERGENS),
    (CATEGORY_FRAGRANCE, 'Fragrance Allergens', FRAGRANCE_ALLERGENS),
    (CATEGORY_OTHER, 'Other Allergens', OTHER_ALLERGENS),
]