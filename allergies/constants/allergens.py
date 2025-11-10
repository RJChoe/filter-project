# Fragrance allergens (EU regulated fragrance allergens)
FRAGRANCE_ALLERGENS = [
    ("linalool", "Linalool"),
    ("limonene", "Limonene"),
    ("geraniol", "Geraniol"),
    ("citronellol", "Citronellol"),
    ("eugenol", "Eugenol"),
    ("cinnamal", "Cinnamal"),
    ("benzyl_alcohol", "Benzyl Alcohol"),
    ("benzyl_benzoate", "Benzyl Benzoate"),
    ("benzyl_salicylate", "Benzyl Salicylate"),
    ("coumarin", "Coumarin"),
    ("farnesol", "Farnesol"),
    ("citral", "Citral"),
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