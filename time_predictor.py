# time_predictor.py
class TimePredictor:
    def __init__(self):
        self.coeffs = None
        self.features = []

    def _design_matrix(self, X):
        F = []
        for x in X:
            row = [1.0]
            for f in self.features:
                row.append(float(x.get(f, 0.0)))
            F.append(row)
        return F

    def train(self, X, y, features):
        self.features = features
        A = self._design_matrix(X)
        m = len(A[0])
        ATA = [[0.0]*m for _ in range(m)]
        ATy = [0.0]*m
        for i in range(len(A)):
            ai, yi = A[i], y[i]
            for r in range(m):
                ATy[r] += ai[r]*yi
                for c in range(m):
                    ATA[r][c] += ai[r]*ai[c]
        M = [row[:] + [ATy[i]] for i, row in enumerate(ATA)]
        n = m
        for i in range(n):
            pivot = M[i][i] or 1e-12
            for k in range(i, n+1):
                M[i][k] /= pivot
            for j in range(n):
                if j == i: continue
                factor = M[j][i]
                for k in range(i, n+1):
                    M[j][k] -= factor * M[i][k]
        self.coeffs = [M[i][n] for i in range(n)]

    def predict(self, x):
        val = self.coeffs[0]
        for i, f in enumerate(self.features):
            val += self.coeffs[i+1]*float(x.get(f, 0.0))
        return val
