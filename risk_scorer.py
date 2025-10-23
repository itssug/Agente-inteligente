# risk_scorer.py
class RiskScorer:
    def __init__(self, rules=None):
        self.rules = rules or {
            'riesgo_salud': 0.35,
            'riesgo_psicologico': 0.25,
            'abandono_previos': 0.20,
            'edad_menor': 0.10,
            'condiciones_vulnerables': 0.10
        }

    def score(self, case):
        score = 0.0
        score += self.rules['riesgo_salud'] * case.get('riesgo_salud', 0)
        score += self.rules['riesgo_psicologico'] * case.get('riesgo_psicologico', 0)
        score += self.rules['abandono_previos'] * (1.0 if case.get('abandono_previos') else 0.0)
        edad = case.get('edad')
        score += self.rules['edad_menor'] * (1.0 if edad and edad < 3 else 0.0)
        score += self.rules['condiciones_vulnerables'] * (1.0 if case.get('condiciones_vulnerables') else 0.0)
        return round(score, 4)

    def prioritize(self, cases, top_k=10):
        scored = [(self.score(c), c) for c in cases]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{'score': s, 'case': c} for s, c in scored[:top_k]]
