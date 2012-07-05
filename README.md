#`dbscan`


Python implementation of 'Density Based Spatial Clustering of Applications with Noise'

## Setup

`python setup.py install`

## Usage

	import dbscan
	dbscan.dbscan(m, eps, min_points)
	
## Documentation

	┌───────────────────────────────────────────────────────────────────────────────────────────────┐
	| dbscan.dbscan: (m, eps, min_points)
	| Implementation of Density Based Spatial Clustering of Applications with Noise
	|    See https://en.wikipedia.org/wiki/DBSCAN
	| 
	|    scikit-learn probably has a better implementation
	|    Uses Euclidean Distance as the measure
	| 
	| Inputs:
	| m - A matrix whose columns are feature vectors
	| eps - Maximum distance two points can be to be regionally related
	| min_points - The minimum number of points to make a cluster
	| 
	| Outputs:
	| An array with either a cluster id number or dbscan.NOISE (None) for each 
	| column vector in m.
	└───────────────────────────────────────────────────────────────────────────────────────────────┘