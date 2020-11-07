# This file contains a GPS "zoom in" mapper, used to truncate GPS cordinates. consider decimal place 3 for mapping covid outbreaks.
mapper = [
    {
        "decimal_places": 0,
        "unambiguously_recognition": "country or large region",
        "distances": [
            {"where": "at_equator", "distance": 111.32, "units": "km"},
            {"where": "ew@23ns", "distance": 102.47, "units": "km"},
            {"where": "ew@45ns", "distance": 78.71, "units": "km"},
            {"where": "ew@67ns", "distance": 43.496, "units": "km"},
        ],
    },
    {
        "decimal_places": 1,
        "unambiguously_recognition": "large city or district",
        "distances": [
            {"where": "at_equator", "distance": 11.132, "units": "km"},
            {"where": "ew@23ns", "distance": 10.247, "units": "km"},
            {"where": "ew@45ns", "distance": 7.871, "units": "km"},
            {"where": "ew@67ns", "distance": 4.3496, "units": "km"},
        ],
    },
    {
        "decimal_places": 2,
        "unambiguously_recognition": "town or village",
        "distances": [
            {"where": "at_equator", "distance": 1.1132, "units": "km"},
            {"where": "ew@23ns", "distance": 1.0247, "units": "km"},
            {"where": "ew@45ns", "distance": 787.1, "units": "m"},
            {"where": "ew@67ns", "distance": 434.96, "units": "m"},
        ],
    },
    {
        "decimal_places": 3,
        "unambiguously_recognition": "neighborhood, street",
        "distances": [
            {
                "where": "at_equator",
                "distance": 111.32,
                "units": "m",
            },
            {
                "where": "ew@23ns",
                "distance": 102.47,
                "units": "m",
            },
            {
                "where": "ew@45ns",
                "distance": 78.71,
                "units": "m",
            },
            {"where": "ew@67ns", "distance": 43.496, "units": "m"},
        ],
    },
    {
        "decimal_places": 4,
        "unambiguously_recognition": "individual street, land parcel",
        "distances": [
            {"where": "at_equator", "distance": 11.132, "units": "m"},
            {
                "where": "ew@23ns",
                "distance": 10.247,
                "units": "m",
            },
            {
                "where": "ew@45ns",
                "distance": 7.871,
                "units": "m",
            },
            {
                "where": "ew@67ns",
                "distance": 4.3496,
                "units": "m",
            },
        ],
    },
    {
        "decimal_places": 5,
        "unambiguously_recognition": "individual trees, door entrance",
        "distances": [
            {
                "where": "at_equator",
                "distance": 1.1132,
                "units": "m",
            },
            {"where": "ew@23ns", "distance": 1.0247, "units": "m"},
            {"where": "ew@45ns", "distance": 787.1, "units": "mm"},
            {"where": "ew@67ns", "distance": 434.96, "units": "mm"},
        ],
    },
    {
        "decimal_places": 6,
        "unambiguously_recognition": "individual humans",
        "distances": [
            {"where": "at_equator", "distance": 111.32, "units": "mm"},
            {"where": "ew@23ns", "distance": 102.47, "units": "mm"},
            {"where": "ew@45ns", "distance": 78.71, "units": "mm"},
            {"where": "ew@67ns", "distance": 43.496, "units": "mm"},
        ],
    },
    {
        "decimal_places": 7,
        "unambiguously_recognition": "practical limit of commercial surveying",
        "distances": [
            {"distance": 11.132, "units": "mm"},
            {"where": "ew@23ns", "distance": 10.247, "units": "mm"},
            {"where": "ew@45ns", "distance": 7.871, "units": "mm"},
            {"where": "ew@67ns", "distance": 4.3496, "units": "mm"},
        ],
    },
    {
        "decimal_places": 8,
        "unambiguously_recognition": "specialized surveying (e.g. tectonic plate mapping)",
        "distances": [
            {"distance": 1.1132, "units": "mm"},
            {"where": "ew@23ns", "distance": 1.0247, "units": "mm"},
            {"where": "ew@45ns", "distance": 787.1, "units": "μm"},
            {"where": "ew@67ns", "distance": 434.96, "units": "μm"},
        ],
    },
]
