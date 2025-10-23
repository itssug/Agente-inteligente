
import heapq

class Recommender:
    def __init__(self, weights=None):
        self.weights = weights or {
            'edad': 0.30,
            'idioma': 0.15,
            'tipo_adopcion': 0.20,
            'disponibilidad': 0.15,
            'compatibilidad_social': 0.20
        }

    def score_match(self, adoptante, nna):
        s = 0.0
        if 'edad' in nna:
            nna_edad = nna['edad']
            pref_min = adoptante.get('edad_min')
            pref_max = adoptante.get('edad_max')
            if pref_min and pref_max:
                edad_score = 1.0 if pref_min <= nna_edad <= pref_max else 0.5
            else:
                edad_score = 0.5
            s += self.weights['edad'] * edad_score

        adopt_langs = set(adoptante.get('idiomas', []))
        nna_langs = set(nna.get('idiomas', []))
        lang_score = len(adopt_langs.intersection(nna_langs)) / max(1, len(nna_langs))
        s += self.weights['idioma'] * lang_score

        type_score = 1.0 if nna.get('tipo_adopcion') in adoptante.get('tipos_adopcion', []) else 0.0
        s += self.weights['tipo_adopcion'] * type_score

        disp_score = 1.0 if adoptante.get('disponibilidad') and nna.get('disponibilidad') else 0.0
        s += self.weights['disponibilidad'] * disp_score

        adopt_tags = set(adoptante.get('tags_sociales', []))
        nna_tags = set(nna.get('tags_sociales', []))
        compat_score = len(adopt_tags.intersection(nna_tags)) / max(1, len(nna_tags))
        s += self.weights['compatibilidad_social'] * compat_score

        return round(s, 4)

    def recommend(self, adoptante, nna_list, top_k=5):
        heap = []
        for nna in nna_list:
            sc = self.score_match(adoptante, nna)
            heapq.heappush(heap, (-sc, nna))
        result = []
        for _ in range(min(top_k, len(heap))):
            score, nna = heapq.heappop(heap)
            result.append({'score': -score, 'nna': nna})
        return result
