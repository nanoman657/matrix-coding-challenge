# Coding-challenge

 Write a function that takes a 2-dimensional array of integers as well as a distance threshold (I'll call it n), and returns the number of cells in the array that are within n steps of a positive value. Here "steps" means just up/down/left/right steps in the grid (but you can take a step one direction and then the next step in a different direction). By way of example, consider the following grid:

[ [ 0, 0, 0, 0, 0 ],
[ 0, 0, 1, 0, 0 ],
[ 0, 0, 1, 0, 0 ] ]

If we are given that grid, and the value n=1, the answer should be 7:
[ [ 0, 0, X, 0, 0 ],
[ 0, X, X, X, 0],
[ 0, X, X, X, 0] ]
