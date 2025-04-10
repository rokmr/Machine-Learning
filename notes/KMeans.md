# K-means Clustering

## Process
- Initialize number of k
- Randomly choose k points in the data as centroids 
- While points do not change: (centroids do not change or max number of iter)
    - Assign each data point to its nearest centroid.
    - Recompute the centroids of each cluster 


## K

### Optimal K
To find the optimal number of clusters (k), we use the Elbow Method:
1. Calculate the Within-Cluster Sum of Squares (WSS) for different values of k
2. Plot WSS vs k
3. Look for the "elbow" point - where increasing k starts giving diminishing returns
4. Choose k at this elbow point

<div align='center'>
<img src='https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9ihLnBj-RV2h4e-VEimEbw.png'>
</div>

## Advantages

1. **Simple and Intuitive**: Easy to understand and implement; works well for basic clustering tasks; widely used in practice.

2. **Fast and Efficient**: Linear time complexity O(nkd) where n is samples, k is clusters, d is dimensions; scales well with large datasets.

3. **Memory Efficient**: Only stores centroids and cluster assignments; minimal memory requirements compared to other clustering methods.


## Drawbacks

1. **Sensitive to Initialization**: Results vary based on initial centroid positions, may get stuck in local optima; solution is to run multiple times with different initializations.

2. **Assumes Spherical Clusters**: Works best with spherical, similarly sized clusters; struggles with elongated or irregular shapes; not suitable for varying densities.

3. **Requires Pre-specification of k**: Number of clusters must be known beforehand; elbow method is subjective; different metrics may suggest different optimal k values.

4. **Sensitive to Outliers**: Outliers can significantly influence centroid positions; may create clusters just for outliers; solution is to pre-process data.


# DBSCAN 
DBSCAN is a density-based clustering algorithm.

## Process:
Parameters: ε (epsilon), n (min points)

1. Start with an arbitrary point p from the dataset
2. Find all points within ε radius of point p (ε-neighbors)
3. If number of ε-neighbors ≥ n:
   - Create a new cluster
   - Add point p and its ε-neighbors to the cluster
   - For each neighbor point:
     * Find its ε-neighbors
     * If ≥ n neighbors, add them to the cluster
     * Continue expanding until no more points can be added
4. Mark processed points as visited
5. Repeat steps 1-4 with unvisited points until all points are processed


**Pros:** Arbitrary cluster shapes

**Cons:** Two parameters to tune and fixed ε can't handle varying densities

# HDBSCAN:

Only needs n parameter
Handles varying densities
Slower than k-means but more versatile
Recommended as first clustering approach


# Hierarchical clustering 
- **Agglomerative (bottom-up):** Similar to flood filling, starts with individual points and merges closest pairs
- **Divisive (top-down):** Starts with all points in one cluster and recursively splits