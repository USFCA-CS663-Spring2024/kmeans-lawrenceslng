from cluster import *
import random
import math
import copy

class Own_KMeans(cluster):
    def __init__(self, k=5, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
    
    def fit(self, X):
        num_instances = len(X)
        if num_instances < 1:
            return
        num_dimensions = len(X[0])
        
        # place k num of centroids randomly and return a list of min and max values for dimensions
        min_dims, max_dims = self.get_max_min_dimensions(X, num_instances, num_dimensions)

        # we will create k nums centroids within 
        centroids_list = self.create_k_centroids(min_dims, max_dims)
        
        num_iterations = 0
        converged = False
        cluster_hypothesis = []  

        while not converged:
            orig_cluster_hypothesis = copy.deepcopy(cluster_hypothesis)
            cluster_hypothesis = []
            # assign each instance to the closest centroid
            cluster_hypothesis = self.assign_to_closest_centroid(centroids_list, cluster_hypothesis, X)           
            # update the centroid locations
            new_centroid_list = self.update_centroid_locations(num_dimensions, cluster_hypothesis, X)
            num_iterations += 1
            # check if cluster_hypothesis stays the same as original hypothesis
            if num_iterations >= self.max_iterations or cluster_hypothesis == orig_cluster_hypothesis:
                converged = True 
            else:
                centroids_list = new_centroid_list
        return [cluster_hypothesis,centroids_list]

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
                centroid_dim.append(random.uniform(min_dims[j],max_dims[j]))
            centroids_list.append(centroid_dim)
        return centroids_list
    
    def assign_to_closest_centroid(self, centroids_list, cluster_hypothesis, X):
        for instance in X:
            # assign instance to closest centroid
            # compute distances to all centroids
            distance_list = []
            for centroid in centroids_list:
                distance = 0
                for i in range(len(instance)):
                    distance += (centroid[i] - instance[i])**2
                distance = math.sqrt(abs(distance))
                distance_list.append(distance)
            cluster_hypothesis.append(distance_list.index(min(distance_list)))
        return cluster_hypothesis
    
    def update_centroid_locations(self, num_dimensions, cluster_hypothesis, X):
        new_centroid_list = []
        total_counts = []
        for i in range(self.k):
            new_centroid_list.append([0,0]) 
            total_counts.append(0)
        for instance, point in zip(cluster_hypothesis, X):
            curr_centroid = new_centroid_list[instance] 
            for i in range(num_dimensions):
                curr_centroid[i] += point[i]
            new_centroid_list[instance] = curr_centroid
            total_counts[instance] += 1
        
        for new_centroid, counts in zip(new_centroid_list, total_counts):
            curr_count = counts
            for i in range(num_dimensions):
                new_centroid[i] /= curr_count
        return new_centroid_list

if __name__ == "__main__" :
    kmeans = Own_KMeans(2, 100)
    X = [[0,0],[2,2],[0,2],[2,0],[10,10],[8,8],[10,8],[8,10]]
    cluster_hyp, cluster_centroids = kmeans.fit(X)
    print("returned cluster hypothesis: ", cluster_hyp)
    print("returned cluster centroid: ", cluster_centroids)