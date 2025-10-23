# document_classifier.py
import re
from collections import Counter, defaultdict
import math

def normalize_text(t):
    t = t.lower()
    t = re.sub(r'[^a-z0-9áéíóúüñ\s]', ' ', t)
    return [w for w in t.split() if len(w) > 1]

class DocumentClassifier:
    def __init__(self):
        self.class_token_counts = defaultdict(Counter)
        self.class_doc_counts = Counter()
        self.vocab = Counter()
        self.total_docs = 0

    def train(self, docs):
        for text, label in docs:
            tokens = normalize_text(text)
            self.class_doc_counts[label] += 1
            self.total_docs += 1
            for t in tokens:
                self.class_token_counts[label][t] += 1
                self.vocab[t] += 1

    def predict(self, text):
        tokens = normalize_text(text)
        best_label, best_logprob = None, -1e9
        vocab_size = len(self.vocab) or 1
        for label in self.class_doc_counts:
            prior = math.log(self.class_doc_counts[label] / self.total_docs)
            logprob = prior
            total_tokens_in_label = sum(self.class_token_counts[label].values()) + vocab_size
            for t in tokens:
                count = self.class_token_counts[label].get(t, 0) + 1
                logprob += math.log(count / total_tokens_in_label)
            if logprob > best_logprob:
                best_logprob, best_label = logprob, label
        return best_label
