"""
Single source of truth for your personal content.
Edit THIS file to update your bio, links, publications, and research themes —
every page reads from here, so you never touch the layout code.
"""

# --------------------------------------------------------------------------- #
# PROFILE
# --------------------------------------------------------------------------- #
PROFILE = {
    "name": "Inayat Ullah Irshad",
    "initials": "IUI",
    "role": "Theoretical & Computational Biophysics",
    "affiliation": "Department of Physics, IIT Jammu",
    "tagline": "Modeling the stochastic logic of protein synthesis.",
    "lede": (
        "I build statistical-physics models of translation — TASEP lattices, "
        "master equations, and ribosome-profiling analysis — to understand how "
        "cells set the rate, accuracy, and stoichiometry of protein production."
    ),
    "fellowship": "Prime Minister's Research Fellow (PMRF)",
    "advisor": "Prof. Ajeet K. Sharma",
    # Edit these links / email:
    "email": "your.email@iitjammu.ac.in",   # <-- put your real email here
    "scholar": "https://scholar.google.com/citations?user=hPcdyDEAAAAJ",
    "github": "https://github.com/samarnwinter",
    "profile_page": "https://iitjammu.ac.in/pmrf/inayat-ullah-irshad-pmrf",
}

# Headline metrics shown on the home page. Keep these easy to eyeball.
METRICS = [
    ("05", "Peer-reviewed papers"),
    ("Molecular Cell", "Latest venue (2025)"),
    ("PMRF", "Research fellowship"),
]

# --------------------------------------------------------------------------- #
# PUBLICATIONS  (newest first). "role" flags your contribution type.
# --------------------------------------------------------------------------- #
PUBLICATIONS = [
    {
        "year": "2025",
        "title": "HYPK promotes N-terminal protein acetylation through rapid "
                 "ribosome exchange of NatA",
        "authors": "Lentzsch AM, Fan Z, Irshad IU, O'Brien EP, Sharma AK, "
                   "Green R, Shan S",
        "venue": "Molecular Cell",
        "detail": "85(24), 4562–4574.e6",
        "doi": "10.1016/j.molcel.2025.11.017",
        "tags": ["Cotranslational biogenesis", "Kinetic modeling", "Experimental"],
        "summary": (
            "Kinetic and in-cell measurements show HYPK acts as a ribosome "
            "exchange factor for NatA: it accelerates NatA release from the "
            "ribosome so a sub-stoichiometric amount of enzyme can acetylate the "
            "whole nascent proteome — a 'Goldilocks' zone of binding kinetics."
        ),
    },
    {
        "year": "2024",
        "title": "Understanding the regulation of protein synthesis under stress "
                 "conditions",
        "authors": "Irshad IU, Sharma AK",
        "venue": "Biophysical Journal",
        "detail": "123(20), 3627–3639",
        "doi": "10.1016/j.bpj.2024.09.014",
        "tags": ["Stochastic modeling", "Translation control"],
        "summary": (
            "A stochastic model of translation dissects how cells re-tune "
            "initiation and elongation during stress, separating which molecular "
            "steps actually reshape protein output."
        ),
    },
    {
        "year": "2024",
        "title": "TIR predictor and optimizer: web-tools for accurate prediction "
                 "of translation initiation rate and precision gene design in "
                 "Saccharomyces cerevisiae",
        "authors": "Chakraborty S, Irshad IU, Mahima, Sharma AK",
        "venue": "Biotechnology Journal",
        "detail": "19(5), e202400081",
        "doi": "10.1002/biot.202400081",
        "tags": ["Web tool", "Gene design"],
        "summary": (
            "Introduces web tools that predict translation-initiation rate from "
            "sequence and optimize genes for a target expression level in yeast."
        ),
    },
    {
        "year": "2023",
        "title": "Decoding stoichiometric protein synthesis in E. coli through "
                 "translation rate parameters",
        "authors": "Irshad IU, Sharma AK",
        "venue": "Biophysical Reports",
        "detail": "3(4), 100131",
        "doi": "10.1016/j.bpr.2023.100131",
        "tags": ["Stochastic simulation", "Gene expression"],
        "summary": (
            "Combining sequencing data with TASEP simulations explains "
            "proportional synthesis in multi-protein complexes: initiation rates "
            "scale with subunit stoichiometry, enforcing balance without feedback."
        ),
    },
    {
        "year": "2021",
        "title": "Quantitative modeling of protein synthesis using ribosome "
                 "profiling data",
        "authors": "Yadav V*, Ullah Irshad I*, Kumar H, Sharma AK",
        "venue": "Frontiers in Molecular Biosciences",
        "detail": "8, 688700  ·  *equal contribution  ·  Review",
        "doi": "10.3389/fmolb.2021.688700",
        "tags": ["Review", "Ribosome profiling"],
        "summary": (
            "A review of the methods used to extract translation-initiation and "
            "codon translation rates from ribosome-profiling data for building "
            "quantitative models of protein synthesis."
        ),
    },
]

# --------------------------------------------------------------------------- #
# RESEARCH THEMES  (home + research page)
# --------------------------------------------------------------------------- #
RESEARCH = [
    {
        "eyebrow": "Non-equilibrium models",
        "title": "Stochastic dynamics of translation",
        "body": "TASEP lattices and master equations that treat the ribosome as "
                "a particle hopping along an mRNA, capturing initiation, "
                "elongation, and traffic effects.",
    },
    {
        "eyebrow": "Data-driven inference",
        "title": "Rates from ribosome profiling",
        "body": "Extracting absolute initiation and codon-level elongation rates "
                "from Ribo-seq data, and testing what mRNA features actually set "
                "them.",
    },
    {
        "eyebrow": "Cotranslational biology",
        "title": "Nascent-chain processing",
        "body": "How factors like NatA/HYPK engage translating ribosomes, and the "
                "kinetics that let sub-stoichiometric enzymes act proteome-wide.",
    },
    {
        "eyebrow": "Design principles",
        "title": "Proportional & precise synthesis",
        "body": "Why obligate complex subunits are made in proportion, and how to "
                "design genes for a target expression level.",
    },
]
