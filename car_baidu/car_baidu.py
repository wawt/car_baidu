# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:50:26 2018

@author: wutao
"""

from aip import AipImageClassify

APP_ID = '11210591'
API_KEY = 'OdGI8MNII7egfaOC8tHpPUt9'
SECRET_KEY = '7dVT7KGNVBdLzbajuQtkT9DBsoXUAYw9'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
    
if __name__ == '__main__':      
    for i in range(4):
        filename ='car'+str(i)+'.jpg' 
        image = get_file_content(filename)
        print (client.carDetect(image, options = {"top_num":1})["result"])
        
        
        