
from collections import Counter
import re

def normalize_text(t):
    t = t.lower()
    t = re.sub(r'[^a-z0-9áéíóúüñ\s]', ' ', t)
    return [w for w in t.split() if len(w) > 1]

class ChatbotFAQ:
    def __init__(self, faq_pairs=None): #entranmiento incial
        self.faq = []
        if faq_pairs:
            for q,a in faq_pairs:
                self.faq.append((q, a, Counter(normalize_text(q))))

    def answer(self, text):
        tokens = Counter(normalize_text(text))
        best = (0, None)
        for q,a,ct in self.faq:
            score = sum(tokens[t]*ct.get(t,0) for t in tokens)
            if score > best[0]:
                best = (score, a)
        return best[1] or "No tengo respuesta para esa pregunta en este momento."
