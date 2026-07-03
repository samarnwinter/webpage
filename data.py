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
    "role": "Computational Biophysics",           # field label (sidebar + eyebrow)
    "position": "Postdoctoral Researcher",
    "affiliation": "Biozentrum, University of Basel",
    "group": "Zavolan Group",
    "tagline": "Modeling the stochastic logic of protein synthesis.",
    "lede": (
        "I build statistical-physics models of translation — TASEP lattices, "
        "master equations, and ribosome-profiling analysis — to understand how "
        "cells set the rate, accuracy, and stoichiometry of protein production."
    ),
    # A single, quiet line of background shown on the home page.
    "background": "Ph.D. in Physics, IIT Jammu.",
    # Edit these links / email:
    "email": "your.email@unibas.ch",   # <-- put your real Basel email here
    "scholar": "https://scholar.google.com/citations?user=hPcdyDEAAAAJ",
    "github": "https://github.com/samarnwinter",
    "linkedin": "https://www.linkedin.com/in/inayat-ullah-irshad-233a72a3",
    "profile_page": "https://www.biozentrum.unibas.ch/research/research-groups/"
                    "research-groups-a-z/group/unit/research-group-mihaela-zavolan",
}

# --------------------------------------------------------------------------- #
# HOME-PAGE SCIENCE EXPLAINER  (edit the copy freely)
# --------------------------------------------------------------------------- #
SCIENCE = {
    "intro": (
        "Protein synthesis is one of life's most fundamental and energy-expensive "
        "processes: ribosomes read messenger RNA codon by codon to build every "
        "protein a cell needs. How fast, how accurately, and how selectively this "
        "happens shapes growth, stress response, and disease — yet these dynamics "
        "unfold too quickly and at too small a scale to watch directly."
    ),
    "bridge": (
        "To study translation quantitatively, high-throughput experiments are "
        "paired with statistical and biophysical models. The experiments capture "
        "snapshots of the process; the models turn those snapshots into dynamical, "
        "multi-dimensional detail that no single measurement reveals on its own."
    ),
    "measured": [
        ("Ribosome profiling (Ribo-seq)",
         "A codon-resolution map of where ribosomes sit on every transcript — a "
         "snapshot of translation caught in the act."),
        ("RNA-seq",
         "Transcript abundances: the denominator that turns ribosome occupancy "
         "into translation efficiency."),
        ("pSILAC",
         "Pulsed isotope labelling read by mass spectrometry, measuring newly made "
         "protein — a direct handle on synthesis rates."),
    ],
    "inferred": [
        "Absolute protein synthesis rates",
        "Translation-initiation rates",
        "Codon dwell times and elongation velocity",
        "Ribosome density, current, and traffic",
        "How codon usage and mRNA structure tune them",
    ],
}

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
