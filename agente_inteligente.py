# agente_inteligente.py
from recommender import Recommender
from risk_scorer import RiskScorer
from document_classifier import DocumentClassifier
from time_predictor import TimePredictor
from chatbot_faq import ChatbotFAQ
from reminder_scheduler import ReminderScheduler

class AgenteInteligente:
    def __init__(self):
        self.recommender = Recommender()
        self.risk_scorer = RiskScorer()
        self.doc_classifier = DocumentClassifier()
        self.time_predictor = TimePredictor()
        self.chatbot = ChatbotFAQ()
        self.scheduler = ReminderScheduler()

    def preseleccionar(self, adoptante, nna_list, top_k=5):
        return self.recommender.recommend(adoptante, nna_list, top_k)

    def priorizar_casos(self, cases, top_k=10):
        return self.risk_scorer.prioritize(cases, top_k)

    def clasificar_documento(self, text):
        return self.doc_classifier.predict(text)

    def predecir_tiempo(self, features):
        return self.time_predictor.predict(features)

    def responder_pregunta(self, text):
        return self.chatbot.answer(text)

    def programar_recordatorio(self, when, message, destinatario):
        return self.scheduler.schedule(when, message, destinatario)
