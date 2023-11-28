# teaminternational_datacapture

Solution for the Data Capture challenge for the international team recruitment process


# Time complexity

To achieve an implementation with a constant time complexity, 
an internal Array structure had to be implemented to store how many time a number is added.

After adding all the numbers, we can create the stats. Going through the array and saving not only the number of times element N was added, but also adding the number of minor elements there are. Starting with 0, which will have 0 minor elements, continuing with 1, which will have the number of times that 0 appeared as minor elements, then 2 will have the number of times that 1 appeared added to the number of elements less than 1. This way we can go through the array only once and create enough information so that the functions of the Stats class have constant time complexity.

# Intruccions

All the functions used in the script are from the python3 core so no extra steps are required, 
simply having python3 installed.

To run the tests, the following command is enough
`python3 -m unittest -v`

