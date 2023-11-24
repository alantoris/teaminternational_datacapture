# teaminternational_datacapture

Solution for the Data Capture challenge for the international team recruitment process


# Time complexity

To achieve an implementation with a constant time complexity, 
an internal Fenwick Tree type structure had to be implemented. 
This tree manages to carry a sum of elements in subparts of the array 
depending on the bits of the required index.

Theoretically, adding an element, searching for the number of less and greater elements, 
and the range, are functions that have a time complexity of O(log N), with N being the length of the array. 
For practical purposes, since the array has a fixed size (1000) it can be considered as a constant time complexity.

# Intruccions

All the functions used in the script are from the python3 core so no extra steps are required, 
simply having python3 installed.

To run the tests, the following command is enough
`python3 -m unittest -v`

