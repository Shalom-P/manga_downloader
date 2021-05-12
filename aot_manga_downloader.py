import os
import requests
import urllib.request
from PIL import Image
from fpdf import FPDF
import time
begin = time.time()
os.chdir(r"C:\Users\Lenovo\Desktop")
start = 29
end = 138
os.mkdir("AOT")
os.chdir("AOT")
for chapter in range(start, end):
    schapter = ''
    os.mkdir(str(chapter))
    os.chdir(str(chapter))
    if chapter < 100:
        schapter = '0'+str(chapter)
        print(schapter)
    else:
        schapter = str(chapter)
    # link1 = 'https://hot.leanbox.us/manga/Shingeki-No-Kyojin/0'+schapter+'-001.png'
    # link2 = 'https://official-hot.eorzea.us/manga/Shingeki-No-Kyojin/0'+schapter+'-001.png'
    # if ((requests.get(link1)).status_code == 404 or (requests.get(link2)).status_code == 404):
    #     break
    for pno in range(1, 100):

        try:
            spno = ''

            filename = "AOT"+str(chapter)+'_'+str(pno)+'.jpg'

            if pno < 10:
                spno = '0'+str(pno)
            else:
                spno = str(pno)
            link1 = 'https://hot.leanbox.us/manga/Shingeki-No-Kyojin/0'+schapter+'-0'+spno+'.png'
            link2 = 'https://official-hot.eorzea.us/manga/Shingeki-No-Kyojin/0' + \
                schapter+'-0'+spno+'.png'
            if((requests.get(link1)).status_code == 404 and (requests.get(link2)).status_code == 404):
                break
            elif (requests.get(link1)).status_code != 404:
                link = link1
            else:
                link = link2
            print(link)
            f = open(filename, 'wb')
            f.write(requests.get(link).content)
            f.close()
        except:
            print('ERROR')
    pdf = FPDF()
    sdir = "AOT"+str(chapter)+'_'
    w,h = 0,0
    for i in range(1,100):
        fname = sdir + str(i) + '.jpg'
        if os.path.exists(fname):
            if i == 1:
                cover = Image.open(fname)
                w,h = cover.size
                pdf = FPDF(unit = "pt",format = [w,h])
            image = fname
            pdf.add_page()
            pdf.image(image,0,0,w,h)
        else:
            print("file not found")
            break
    pdf.output(str(chapter)+'.pdf')
    os.chdir('..')
end = time.time()
tim = end-begin
minutes = 0
while tim > 60:
    tim -= 60
    minutes += 1
print('the program took '+str(minutes)+' minutes and '+str(tim)+' seconds  to download and convert all images to pdf')

#########################################################################################################################################################


# for chapter in range(start, end):
#     schapter = ''
#     os.mkdir(str(chapter))
#     os.chdir(str(chapter))
#     if chapter < 10:
#         schapter = '00'+str(chapter)
#     elif chapter<100:
#         schapter = '0'+str(chapter)
#     else:
#         schapter = str(chapter)
#     # link1 = 'https://hot.leanbox.us/manga/Shingeki-No-Kyojin/0'+schapter+'-001.png'
#     # link2 = 'https://official-hot.eorzea.us/manga/Shingeki-No-Kyojin/0'+schapter+'-001.png'
#     # if ((requests.get(link1)).status_code == 404 or (requests.get(link2)).status_code == 404):
#     #     break

#     for char in list(alphabet_string):
#         jklink='zjcdn.mangafox.me/store/manga/27861/'+schapter+'.0/compressed/'+char+'001.jpg'
#         if((requests.get(jklink)).status_code != 404):
#             character=char
#             break

#     if(charcter==''):
#         break


#     for pno in range(1, 61):

#         try:
#             spno = ''
#             character=''
#             filename = "JK"+str(chapter)+'_'+str(pno)+'.jpg'

#             # print('cp1')
#             if pno < 10:
#                 spno = '00'+str(pno)
#             elif pno<100:
#                 spno = '0'+str(pno)
#             else:
#                 spno = str(pno)

#             jklink='zjcdn.mangafox.me/store/manga/27861/'+schapter+'.0/compressed/'+character+spno+'.jpg'

#             print(link)
#             f = open(filename, 'wb')
#             f.write(requests.get(jklink).content)
#             f.close()
#         except:
#             print('ERROR')
#     os.chdir('..')
