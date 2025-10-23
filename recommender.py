# recommender.py
import heapq

class Recommender:
    def __init__(self, weights=None):
        # Pesos para cada criterio de compatibilidad
        self.weights = weights or {
            'edad': 0.4,
            'idioma': 0.2,
            'tipo_adopcion': 0.2,
            'disponibilidad': 0.1,
            'tags_sociales': 0.1
        }

    def _score(self, adoptante, nna):
        score = 0.0

        # Edad compatible
        if 'edad' in nna and 'edad_min' in adoptante and 'edad_max' in adoptante:
            if adoptante['edad_min'] <= nna['edad'] <= adoptante['edad_max']:
                score += self.weights['edad']

        # Idiomas compatibles
        idioma_match = len(set(adoptante.get('idiomas', [])) & set(nna.get('idiomas', [])))
        if adoptante.get('idiomas'):
            score += self.weights['idioma'] * (idioma_match / len(adoptante['idiomas']))

        # Tipo de adopción
        if nna.get('tipo_adopcion') in adoptante.get('tipos_adopcion', []):
            score += self.weights['tipo_adopcion']

        # Disponibilidad
        if adoptante.get('disponibilidad') and nna.get('disponibilidad'):
            score += self.weights['disponibilidad']

        # Tags sociales
        tags_match = len(set(adoptante.get('tags_sociales', [])) & set(nna.get('tags_sociales', [])))
        if adoptante.get('tags_sociales'):
            score += self.weights['tags_sociales'] * (tags_match / len(adoptante['tags_sociales']))

        return score

    def recommend(self, adoptante, nna_list, top_k=5):
        heap = []
        for nna in nna_list:
            sc = self._score(adoptante, nna)
            # Usamos id para desempatar en caso de score igual
            heapq.heappush(heap, (-sc, nna['id'], nna))

        top = [heapq.heappop(heap)[2] for _ in range(min(top_k, len(heap)))]
        return top
