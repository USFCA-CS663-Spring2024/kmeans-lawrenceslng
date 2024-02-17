from cluster import *
import random

class KMeans(cluster):
    def __init__(self, k=5, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
    
    def fit(self, X):
        print("X: ", X)
        print("k: ", self.k)
        print("max_it: ", self.max_iterations)

        num_instances = len(X)
        if num_instances < 1:
            return
        num_dimensions = len(X[0])
        print("num_instances: ", num_instances)
        print("num_dimensions: ", num_dimensions)
        
        # place k num of centroids randomly
        # return a list of min and max values for dimensions?
        min_dims, max_dims = self.get_max_min_dimensions(X, num_instances, num_dimensions)
        print("min dims: ", min_dims)
        print("max dims: ", max_dims)

        # we will create k nums centroids 
        centroids_list = self.create_k_centroids(min_dims, max_dims)
        
        # while not converged, 
        num_iterations = 0
        converged = False
        while not converged:
            
            num_iterations += 1
            if num_iterations >= self.max_iterations:
                converged = True 
        return [[0,0,0,0,1,1,1,1],[[1,1],[9,9]]] # placeholder

    def get_max_min_dimensions(self, X, num_instances, num_dimensions):
        min_dims = []
        max_dims = []
        for i in range (num_dimensions):
            list_val = []
            for j in range (num_instances):
                list_val.append(X[j][i])
            min_dims.append(min(list_val))
            max_dims.append(max(list_val))
        return min_dims, max_dims
    
    def create_k_centroids(self, min_dims, max_dims):
        centroids_list = []
        for i in range(self.k):
            centroid_dim = []
            for j in range(len(min_dims)):     
                centroid_dim.append(random.randint(min_dims[j], max_dims[j]))
            centroids_list.append(centroid_dim)
            
        print("centroids_list: ", centroids_list)
        return centroids_list

if __name__ == "__main__" :
    kmeans = KMeans(3, 10)
    X = [[0,0],[2,2],[0,2],[2,0],[10,10],[8,8],[10,8],[8,10]]
    cluster_hyp, cluster_centroids = kmeans.fit(X)
    print("cluster hypothesis: ", cluster_hyp)
    print("cluster centroid: ", cluster_centroids)