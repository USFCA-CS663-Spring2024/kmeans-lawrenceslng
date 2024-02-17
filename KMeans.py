from cluster import *
import random
import math

class KMeans(cluster):
    def __init__(self, k=5, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
    
    def fit(self, X):
        # print("X: ", X)
        # print("k: ", self.k)
        # print("max_it: ", self.max_iterations)

        num_instances = len(X)
        if num_instances < 1:
            return
        num_dimensions = len(X[0])
        # print("num_instances: ", num_instances)
        # print("num_dimensions: ", num_dimensions)
        
        # place k num of centroids randomly
        # return a list of min and max values for dimensions?
        min_dims, max_dims = self.get_max_min_dimensions(X, num_instances, num_dimensions)
        # print("min dims: ", min_dims)
        # print("max dims: ", max_dims)

        # we will create k nums centroids 
        centroids_list = self.create_k_centroids(min_dims, max_dims)
        
        # while not converged, 
        num_iterations = 0
        converged = False
        cluster_hypothesis = []
        

        while not converged:
            orig_cluster_hypothesis = cluster_hypothesis.copy()
            cluster_hypothesis = []
            for instance in X:
                # assign instance to closest centroid
                # compute distances to all centroids
                distance_list = []
                for centroid in centroids_list:
                    distance = 0
                    for i in range(len(instance)):
                        distance += (centroid[i]**2 - instance[i]**2)
                    distance = math.sqrt(abs(distance))
                    distance_list.append(distance)
                # print("distance list: ", distance_list)
                cluster_hypothesis.append(distance_list.index(min(distance_list)))

            new_centroid = [0] * num_dimensions
            # new_centroid_list = [new_centroid] * self.k
            new_centroid_list = [[0,0],[0,0]] 
            curr_centroid_count = 0
            # for centroid in centroids_list:
                # move centroid to mean location
                # calculate mean centroid location
                # replace centroid entry with new location
            curr_data = 0
            for instance, point in zip(cluster_hypothesis, X):
                curr_centroid = new_centroid_list[instance] 
                for i in range(num_dimensions):
                    curr_centroid[i] += point[i]
                new_centroid_list[instance] = curr_centroid
                curr_data += 1
            
            count = 0
            for new_centroid in new_centroid_list:
                for i in range(num_dimensions):
                    new_centroid[i] /= cluster_hypothesis.count(count)
                count += 1    

            num_iterations += 1
            if num_iterations >= self.max_iterations:
                converged = True 
        return [cluster_hypothesis,new_centroid_list] # placeholder

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
    kmeans = KMeans(2, 100)
    X = [[0,0],[2,2],[0,2],[2,0],[10,10],[8,8],[10,8],[8,10]]
    cluster_hyp, cluster_centroids = kmeans.fit(X)
    print("returned cluster hypothesis: ", cluster_hyp)
    print("returned cluster centroid: ", cluster_centroids)