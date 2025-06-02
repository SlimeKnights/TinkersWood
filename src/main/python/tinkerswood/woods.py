# wood config:

#   mod_id:       root mod, used for log/plank detection and prefixes the wood name
#   name:         name of the wood variant
#   override_log: if true, Tinkers' Construct ships a log recipe to override
#   palette:      mapping from grey values to hex colors for the generator

WOODS = [
    # vanilla
    {
        "name": "oak",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "4C3B20",
            102: "594426",
            140: "67502C",
            178: "7E6237",
            216: "967441",
            234: "AF8F55",
            255: "B8945F"
        }
    },
    {
        "name": "spruce",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "3A2815",
            102: "47301A",
            140: "553A1F",
            178: "5A4424",
            216: "614B2E",
            234: "7A5A34",
            255: "82613A"
        }
    },
    {
        "name": "birch",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "7F704F",
            102: "8C7B56",
            140: "9E8B61",
            178: "A59467",
            216: "AE9F76",
            234: "C8B77A",
            255: "D7C185"
        }
    },
    {
        "name": "jungle",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "4C3323",
            102: "593C29",
            140: "68462F",
            178: "785437",
            216: "976A44",
            234: "AA7954",
            255: "B88764"
        }
    },
    {
        "name": "dark_oak",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "160E06",
            102: "1E1309",
            140: "291A0C",
            178: "301E0E",
            216: "3A2411",
            234: "492F17",
            255: "4F3218"
        }
    },
    {
        "name": "acacia",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "703A21",
            102: "7A3F24",
            140: "884728",
            178: "8F4C2A",
            216: "99502B",
            234: "AD5D32",
            255: "BA6337"
        }
    },
    {
        "name": "mangrove",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "471617",
            102: "51191B",
            140: "5D1C1E",
            178: "642423",
            216: "6F2A2D",
            234: "773934",
            255: "7F4234"
        }
    },
    {
        "name": "cherry",
        "mod_id": "minecraft",
        "override_log": True,
        "palette": {
            63:  "CD8580",
            102: "DD9D97",
            140: "E1A8A1",
            178: "E6B3AD",
            216: "E7BAB4",
            234: "E7C2BB",
            255: "E7CAC5"
        }
    }
]