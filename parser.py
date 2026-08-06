import fitz

class DocumentParser:
    def __init__(self,pdf_path: str):
        self.pdf_path=pdf_path

    def extract_structured_elements(self):
        doc=fitz.open(self.pdf_path)
        elements=[]
        for page in doc:
            page_extract=page.get_text("dict")["blocks"]
            for b in page_extract:
                if "lines" in b:
                    for line in b["lines"]:
                        text = " ".join([span["text"] for span in line["spans"]]).strip()
                        if text:
                            elements.append(text)

        return elements

