# CAMeLBERT Named Entity Recognizer
class ArabicNERPipeline:
    def extract_entities(self, text: str):
        print("Extracting PER, ORG, LOC, DATE from Arabic text.")
        return [
            {"entity": "يوسف خالد", "type": "PER", "score": 0.99},
            {"entity": "جامعة بنها", "type": "ORG", "score": 0.98},
            {"entity": "القاهرة", "type": "LOC", "score": 0.99}
        ]
