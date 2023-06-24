from helper_functions import *

# FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS
datafolder = "C:/Users/Admin/Downloads/assgn1code/assgn1code/images/"
imgpath = datafolder + "3.jpg"
# STARTER CODE
# Convert the colour image to grayscale and returns the grayscale pixels
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundry colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
# WRITE YOUR CODE HERE
# Create a data structure to store updated pixel information
new_pixel_values = [[0 for j in range(numb_colns)] for i in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))
# mask = ((-1,-1,-1), (-1,-8,-1), (-1,-1,-1))


# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values, rowPos, colPos):
    slicedList = [
        slice_2d[colPos - 1 : colPos + 2]
        for slice_2d in pixel_values[rowPos - 1 : rowPos + 2]
    ]
    return slicedList


# Implement a function to flatten a 2D list or a 2D tuple
def flaten(twoDimensionalList):
    # print(twoDimentionalList)
    oneDlist = [j for i in twoDimensionalList for j in i]
    return oneDlist


# For each of the pixel values, excluding the boundary values
for row in range(1, numb_rows + 1):
    for col in range(1, numb_colns + 1):
        # Create little local 3x3 box using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values, row, col)
        # Apply the mask
        flatted_mask = flaten(mask)
        pixels = flaten(neighbour_pixels)
        # print(pixels)
        mult_result = map(lambda row, col: row * col, flatted_mask, pixels)
        # mult_result = []
        # for i in range (9):
        #  mult_result.append(flatted_mask[i]*pixels[i])
        totalsum = sum(list(mult_result))
        # print(mult_result)
        new_pixel_values[row - 1][col - 1] = totalsum
    # Sum all the multiplied values and set the new pixel value
#
# ENd YOur COde HERE
# verify your result
verify_result(pixel_values, new_pixel_values, mask)
# view the original image and the edges of the image
view_images(imgpath, new_pixel_values)
