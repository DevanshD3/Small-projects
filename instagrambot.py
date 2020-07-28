import instaloader
import json
from datetime import datetime
from itertools import takewhile
import xlrd 
import os
import xlsxwriter
from PIL import Image 
import cv2
import os
import glob
import openpyxl
import xlwt
loc = ("instameta.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
# out_wb = xlsxwriter.Workbook(loc)
# out_sheet = out_wb.add_worksheet()
out_wb = xlwt.Workbook(loc)
out_sheet = out_wb.add_sheet('Sheet 1')

mod= instaloader.Instaloader(download_comments= False, download_video_thumbnails= False, compress_json= False, save_metadata= False)
# For row 0 and column 0 
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))
    
    profile = sheet.cell_value(i, 0)
    mod.download_profile(profile,profile_pic_only=True)
    profile = instaloader.Profile.from_username(mod.context, profile)

    #this can be altered for anydate and will be able to download all the posts(caption,videos,photos)
    SINCE = datetime(2020, 6, 4)
    
    #file will be saved as the username
    for post in takewhile(lambda p: p.date_utc > SINCE, profile.get_posts()):
        mod.download_post(post, target=sheet.cell_value(i, 0))
        
          
    print("*******folder has been made*********")

    img_dir = ("C:\\Users\\Dell\\"+ sheet.cell_value(i, 0))
    # Enter Directory of all images
    print(img_dir) 
    data_path = os.path.join(img_dir,'*g')
    files = glob.glob(data_path)
    
    
    column=1
    
    images = []
    for filename in files:
        img = cv2.imread(filename)
        if img is not None:
            images.append(img)
    
    
    for image in images:
        img = Image.fromarray(image, 'RGB')
        img.save("new.jpg")
        
        out_sheet.insert_image(i,column,"new.jpg",{'x_offset': 15, 'y_offset': 10,'x_scale': 0.5, 'y_scale': 0.5,'positioning':1} )
        # out_sheet.write(i,column,"hello")
        column=column+1
        out_wb.save(loc)
    
    print("******Sheet updated****************")