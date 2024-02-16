import cluster

class KMeans(cluster):
    def __init__(self, k=5, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        cluster.__init__(self)
    
    def fit(self, X):
        pass