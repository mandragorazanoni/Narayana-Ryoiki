class ArchiveDocument:
    def __init__(self, doc_id, title, category, author, content, tags):
        self.doc_id = doc_id
        self.title = title
        self.category = category
        self.author = author
        self.content = content
        self.tags = tags

class ArchiveDatabase:
    def __init__(self):
        self.documents = {}
        self._load_default_entries()

    def _load_default_entries(self):
        # 1. Tacitus - Arcanum Imperii
        self.add_document(ArchiveDocument(
            doc_id="TAC_ANN_01",
            title="Arcanum Imperii (Annales)",
            category="Historiographia & Politica",
            author="Tacitus",
            content="Die sichtbare Macht verhandelt im Senat; die reale Herrschaft ruht in den Arcana Imperii — den verborgenen Notizen, Akten und Netzwerken der Kanzlei.",
            tags=["Tacitus", "Macht", "Rom", "Geheimdienst"]
        ))

        # 2. Jeremia - Kaufbrief zu Anathot
        self.add_document(ArchiveDocument(
            doc_id="JER_32_ANATHOT",
            title="Der Kaufbrief zu Anathot",
            category="Theologia & Jurisprudentia",
            author="Jeremia / Baruch",
            content="Und ich wog ihm das Geld dar, siebzehn Sekel Silber, und schrieb einen Kaufbrief und versiegelte ihn... und legte ihn in ein tonernes Gefäss, auf dass er lange bleibe.",
            tags=["Jeremia", "Anathot", "Silber", "Vertrag", "Acker"]
        ))

        # 3. Regnault & Strecker / Ernst Schmidt - Chemismus
        self.add_document(ArchiveDocument(
            doc_id="CHEM_REG_STRECKER",
            title="Anorganische Chemie & Alkaloid-Synthese",
            category="Anorganica & Pharmacia",
            author="Regnault / Strecker / Schmidt",
            content="Die Reinstoff-Isolierung erfordert die exakte Thermodynamik der Salze. Der Stickstoff-Heterocyclus bestimmt die pharmakologische Affinität am Rezeptor.",
            tags=["Chemie", "Alkaloid", "Regnault", "Schmidt"]
        ))

        # 4. Cheryl Pellerin - Neurochemie & Perzeption
        self.add_document(ArchiveDocument(
            doc_id="PELL_HALLUZ_01",
            title="Pharmakodynamik der Perzeption",
            category="Neurochemia & Perceptio",
            author="Cheryl Pellerin",
            content="Die Tryptamin-Struktur besetzt die 5-HT2A-Pfade des Cortex. Die Folge ist eine epistemologische Dekonstruktion der Alltagsperzeption.",
            tags=["Pellerin", "Halluzinogene", "Neurochemie"]
        ))

    def add_document(self, doc):
        self.documents[doc.doc_id] = doc

    def get_all(self):
        return list(self.documents.values())
