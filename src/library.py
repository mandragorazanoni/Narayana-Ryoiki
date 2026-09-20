# Manuel gepflegtes Fachwissen aus eigenen Mindmaps & Notizen

MANUAL_LIBRARIES = {
    "SCHRIFTSETZER": {
        "jargon": ["Bleisatz", "Setzkasten", "Fliegenkopf", "Gutenberg-Geviert", "Ligatur", "Spationierung"],
        "prüfroutine": "Achtet auf Satzspiegel, Bleilabnutzung, Spationierung und typografische Unregelmäßigkeiten.",
        "mindmap_notizen": ""
    },
    "GEIGENBAUER": {
        "jargon": ["Resonanzfichte", "Ahornboden", "Spirituslack", "F-Löcher", "Ansprechverhalten", "Wölbung"],
        "prüfroutine": "Klopftest auf Eigenresonanz, Haptik der Zargen, Holzfaserverlauf, Lackzusammensetzung.",
        "mindmap_notizen": ""
    },
    "PINKERTON": {
        "jargon": ["Arcana Imperii", "Dossier", "Doppelidentität", "Logistik-Kette", "Tarnidentität", "Kanalisationsnetz"],
        "prüfroutine": "Filtert nach verdeckten Netzwerken, Informationslücken, Geldflüssen und Bewegungsprofilen.",
        "mindmap_notizen": ""
    }
}

def get_library_for_profession(profession_code):
    """Holt die manuell eingepflegten Fachdaten für einen Beruf."""
    return MANUAL_LIBRARIES.get(profession_code, {
        "jargon": [],
        "prüfroutine": "Standardmäßige Analyse nach Fachkriterien.",
        "mindmap_notizen": ""
    })
