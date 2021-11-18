'''
When this code runs, it checks for the input files. If the files are present then it asks the user to drag and select the regions 
where processing needs to take place. Once all the regions are marked, press ESC and the code will run. Once processing is done another window
is displayed to the user. This window shows the buildings present. The user then clicks on the buildings whose heights need to be determined and
then press ESC. The output of the code shows a dictionary with the coordinates of buildings as keys and the Lat-Lon and relative height of the buildings present
'''
import cv2
from matplotlib.pyplot import contour
import numpy as np
import tree_rect



poly_list = []
temp_poly = []
downscaled = 0



# Since we need a precise location on the downscaled image, we normalize the pixel location using the downscaled resolution
def normalizebb(box_list_val,shape):
    '''
    Function to normalize the coordinates

    Params
    box_list_val: 2D array with each element having the top-left and bottom-right coordinates of the downscaled ROI
    shape: The value bounds that will be used for normalization

    Returns
    norm_box_list: 2D array with each element being normalized
    '''
    norm_box_list = []
    for x in box_list_val:
        # print(x,shape)
        norm_box_list.append((x[0]/shape[1],x[1]/shape[0]))
    
    return norm_box_list

# When we process the DEM we need the actual pixel locations and not the downscaled one. So we reverse the normalization using the original image resolution
def reversenomarlize(box_list_val,shape):
    '''
    Function to upscale the coordinates to match the original Orthomosaic resolution

    Params
    box_list_val: 2D array with each element having the top-left and bottom-right coordinates of the downscaled ROI
    shape: The resolution to which the values need to be upscaled

    Returns
    upscaled_box_list: 2D array with each element having the top-left and bottom-right coordinates of the upscaled ROI
    '''
    upscaled_box_list = []
    for x in box_list_val:
        # print(x,shape)
        x1 = int(x[0]*shape[1])
        y1 = int(x[1]*shape[0])
        upscaled_box_list.append((x1,y1))
    
    return upscaled_box_list

'''
This function is called which lets the user define the ROI for further processing. Simply click the top-left of the ROI and then hold and drag
the mouse to the bottom-right of the ROI.
'''
def draw_rectangle_with_drag(event, x, y, flags, param):

    global ix, iy, drawing, temp_poly,fx,fy,downscaled
      
    if event == cv2.EVENT_LBUTTONDOWN:
        temp_poly.append((x,y))           

    elif event == cv2.EVENT_MOUSEWHEEL:
        pass

    elif event == cv2.EVENT_MBUTTONDOWN:
        poly_list.append(temp_poly)
        np_poly = np.array(temp_poly,dtype=np.int32)
        cv2.polylines(downscaled,[np_poly],1,(255,0,255),1)
        temp_poly = []

def draw_rects(image,rectangles):
    # print(len(rectangles))
    for x in rectangles:
        cv2.rectangle(image,(x[0][0],x[0][1]),(x[1][0],x[1][1]),(0,0,255),1)



def image_sel_method(image_name):
    global downscaled
    image = cv2.imread(image_name)
    image_copy = image
    height,width,_ = image.shape
    downscaled = cv2.resize(image,(width//2,height//2))
    scaled_polys = []
    cv2.namedWindow(winname = "Downscaled Orthomosaic")
    cv2.setMouseCallback("Downscaled Orthomosaic", 
                        draw_rectangle_with_drag)
    while True:
        cv2.imshow("Downscaled Orthomosaic", downscaled)
        if cv2.waitKey(10) == 27:
            shape_small = (height//2,width//2)
            for polys in range(0,len(poly_list)):
                scaled_polys.append(reversenomarlize(normalizebb(poly_list[polys],shape_small),(height,width)))

            del poly_list[:]
            rect_list = []
            for x in scaled_polys:
                rect_list.append(tree_rect.make_trees(x))
            
            # del final_poly[:]
            # for rects in rect_list:
            #     draw_rects(image_copy,rects)

            # cv2.imshow('tet',image)
            # cv2.waitKey(0)
            break
    
    cv2.destroyAllWindows()
    return rect_list