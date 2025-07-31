#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import os
import datetime
import pandas as pd
import json
import csv


# In[3]:


isexist = False
while not isexist:
    inputfile = input('輸入路徑：').strip()
    inputfile = inputfile.strip('"').strip("'")
    inputpath = Path(inputfile)
    if not inputpath.exists():
        print("The path does not exist.")
    elif not inputfile.endswith("csv"):    
        print("The file isn't csv.")
    else:
        print("ok")
        isexist=True

print(inputfile)

# In[4]:


#地點關鍵字與代碼對應表
location_map = {
    "東京": "tokyo",
    "大阪": "osaka",
    "福岡": "fukuoka"
}

location = None  # 預設沒有找到

# 依照順序檢查每個關鍵字
for key, value in location_map.items():
    if key in inputfile:
        if '回' in inputfile:
            location = value+'back'
        else:
            location = value
        break  # 找到第一個符合的就結束

folder = os.path.dirname(inputpath)
today = datetime.date.today().strftime('%y%m%d')

if location != None:    
    jsonfile = folder + "\\flight_" + location + today + ".json"
else:
    jsonfile = inputfile.strip('.csv') + ".json"

print(jsonfile)


# In[5]:


datalist = []
# 開啟 CSV 檔案並讀取
with open(inputfile,"r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)  # 自動用第一列作為 key
    for row in csv_reader:
        datalist.append(row)

# 將資料寫入 JSON 檔案
with open(jsonfile, mode="w", encoding="utf-8") as f:
    json.dump(datalist, f, ensure_ascii=False, indent=4)


# In[ ]:
print("Job is done")




# In[6]:



# In[ ]:





# In[ ]:




