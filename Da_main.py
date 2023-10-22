import random
import shutil
from da_function import *
import configparser
# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')


#input path
main_path=config['Paths']['Dataset'] 
ip=os.path.split(main_path)[0]
#train data output path
output_path="DA_Output/Dataset_Train"
#test data output path
target="DA_Output/Dataset_Test"
op=os.path.split(output_path)[0]
head_dir=os.listdir(main_path)


for dir in head_dir:
    di=os.listdir(main_path+"/"+dir)
    files = os.listdir(str(main_path)+"/"+str(dir)+"/")
    filenames = [f for f in files if os.path.isfile(str(main_path)+"/"+str(dir)+"/"+f)]
    filenames.sort()  # make sure that the filenames have a fixed order before shuffling
    random.seed(230)
    random.shuffle(filenames) # shuffles the ordering of filenames (deterministic given the chosen seed)
    split_2 = int(0.9 * len(filenames))
    train_filenames = filenames[:split_2]
    test_filenames = filenames[split_2:]
    print(test_filenames)
    for file_name in test_filenames:
        isExist = os.path.exists(target+"/"+str(dir)+"/")
        if not isExist:
            os.makedirs(target+"/"+str(dir)+"/")
        shutil.copy(str(main_path)+"/"+str(dir)+"/"+file_name, target+"/"+str(dir)+"/"+file_name)
    files=train_filenames
    count_files=len(files)
    if (count_files <=12):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                img15=dt_rotate(image,Out_Dir,15,filename)
                                img345=dt_rotate(image,Out_Dir,345,filename)
                                img35=dt_rotate(image,Out_Dir,35,filename)
                                img325=dt_rotate(image,Out_Dir,325,filename)
                                Me_blur_img = Me_blur(img325,(filen+"img325"+extension),Out_Dir)
                                G_blur_img = G_blur(img325,(filen+"img325"+extension),Out_Dir)
                                median_img = median(img325,(filen+"img325"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img325,(filen+"img325"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img325,(filen+"img325"+extension),Out_Dir)
                                noiseadd(img325,"s&p",0.3,Out_Dir,(filen+"img325"+extension))
                                noiseadd(img325,"pepper",0.2,Out_Dir,(filen+"img325"+extension))
                                noiseadd(img325,"salt",0.01,Out_Dir,(filen+"img325"+extension))
                                Me_blur_img = Me_blur(img35,(filen+"img35"+extension),Out_Dir)
                                G_blur_img = G_blur(img35,(filen+"img35"+extension),Out_Dir)
                                median_img = median(img35,(filen+"img35"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img35,(filen+"img35"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img35,(filen+"img35"+extension),Out_Dir)
                                noiseadd(img35,"s&p",0.3,Out_Dir,(filen+"img35"+extension))
                                noiseadd(img35,"pepper",0.2,Out_Dir,(filen+"img35"+extension))
                                noiseadd(img35,"salt",0.01,Out_Dir,(filen+"img35"+extension))
                                Me_blur_img = Me_blur(img15,(filen+"img15"+extension),Out_Dir)
                                G_blur_img = G_blur(img15,(filen+"img15"+extension),Out_Dir)
                                median_img = median(img15,(filen+"img15"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img15,(filen+"img15"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img15,(filen+"img15"+extension),Out_Dir)
                                noiseadd(img15,"s&p",0.3,Out_Dir,(filen+"img15"+extension))
                                noiseadd(img15,"pepper",0.2,Out_Dir,(filen+"img15"+extension))
                                noiseadd(img15,"salt",0.01,Out_Dir,(filen+"img15"+extension))
                                Me_blur_img = Me_blur(img345,(filen+"img345"+extension),Out_Dir)
                                G_blur_img = G_blur(img345,(filen+"img345"+extension),Out_Dir)
                                median_img = median(img345,(filen+"img345"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img345,(filen+"img345"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img345,(filen+"img345"+extension),Out_Dir)
                                noiseadd(img345,"s&p",0.3,Out_Dir,(filen+"img345"+extension))
                                noiseadd(img345,"pepper",0.2,Out_Dir,(filen+"img345"+extension))
                                noiseadd(img345,"salt",0.01,Out_Dir,(filen+"img345"+extension))
                                Me_blur_img = Me_blur(img335,(filen+"img335"+extension),Out_Dir)
                                G_blur_img = G_blur(img335,(filen+"img335"+extension),Out_Dir)
                                median_img = median(img335,(filen+"img335"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img335,(filen+"img335"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img335,(filen+"img335"+extension),Out_Dir)
                                noiseadd(img335,"s&p",0.3,Out_Dir,(filen+"img335"+extension))
                                noiseadd(img335,"pepper",0.2,Out_Dir,(filen+"img335"+extension))
                                noiseadd(img335,"salt",0.01,Out_Dir,(filen+"img335"+extension))
                                Me_blur_img = Me_blur(img25,(filen+"img25"+extension),Out_Dir)
                                G_blur_img = G_blur(img25,(filen+"img25"+extension),Out_Dir)
                                median_img = median(img25,(filen+"img25"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img25,(filen+"img25"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img25,(filen+"img25"+extension),Out_Dir)
                                noiseadd(img25,"s&p",0.3,Out_Dir,(filen+"img25"+extension))
                                noiseadd(img25,"pepper",0.2,Out_Dir,(filen+"img25"+extension))
                                noiseadd(img25,"salt",0.01,Out_Dir,(filen+"img25"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                hb=cv2.imread(Out_Dir+"hb_"+filename)
                                Me_blur_img = Me_blur(hb,(filen+"hb"+extension),Out_Dir)
                                G_blur_img = G_blur(hb,(filen+"hb"+extension),Out_Dir)
                                median_img = median(hb,(filen+"hb"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(hb,(filen+"hb"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(hb,(filen+"hb"+extension),Out_Dir)
                                noiseadd(hb,"s&p",0.3,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"pepper",0.2,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"salt",0.01,Out_Dir,(filen+"hb"+extension))
                                double_brightness(imgg,Out_Dir,filename)
                                db=cv2.imread(Out_Dir+"db_"+filename)
                                Me_blur_img = Me_blur(db,(filen+"db"+extension),Out_Dir)
                                G_blur_img = G_blur(db,(filen+"db"+extension),Out_Dir)
                                median_img = median(db,(filen+"db"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(db,(filen+"db"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(db,(filen+"db"+extension),Out_Dir)
                                noiseadd(db,"s&p",0.3,Out_Dir,(filen+"db"+extension))
                                noiseadd(db,"pepper",0.2,Out_Dir,(filen+"db"+extension))
                                noiseadd(db,"salt",0.01,Out_Dir,(filen+"db"+extension))
                                contrast(imgg,Out_Dir,filename)
                                ct=cv2.imread(Out_Dir+"ct_"+filename)
                                Me_blur_img = Me_blur(ct,(filen+"ct"+extension),Out_Dir)
                                G_blur_img = G_blur(ct,(filen+"ct"+extension),Out_Dir)
                                median_img = median(ct,(filen+"ct"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(ct,(filen+"ct"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(ct,(filen+"ct"+extension),Out_Dir)
                                noiseadd(ct,"s&p",0.3,Out_Dir,(filen+"ct"+extension))
                                noiseadd(ct,"pepper",0.2,Out_Dir,(filen+"ct"+extension))
                                noiseadd(ct,"salt",0.01,Out_Dir,(filen+"ct"+extension))
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                img_gray(image,filename,Out_Dir)
                                gray_img=cv2.imread(Out_Dir+"Gray"+filename)
                                gray_blur(gray_img,(filen+"gray"+extension),Out_Dir)

                                #G_blur_img = G_blur(gray_img,(filen+"gray"+extension),Out_Dir)
                                #median_img = median(gray_img,(filen+"gray"+extension),Out_Dir)
                                #Avg_Blur_img = Avg_blur(gray_img,(filen+"gray"+extension),Out_Dir)
                                #Bi_Blur_img = Bi_blur(gray_img,(filen+"gray"+extension),Out_Dir)
                                noiseadd(gray_img,"s&p",0.3,Out_Dir,(filen+"gray"+extension))
                                noiseadd(gray_img,"pepper",0.2,Out_Dir,(filen+"gray"+extension))
                                noiseadd(gray_img,"salt",0.01,Out_Dir,(filen+"gray"+extension))

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >12)and(count_files <=16)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                Me_blur_img = Me_blur(img335,(filen+"img335"+extension),Out_Dir)
                                G_blur_img = G_blur(img335,(filen+"img335"+extension),Out_Dir)
                                median_img = median(img335,(filen+"img335"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img335,(filen+"img335"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img335,(filen+"img335"+extension),Out_Dir)
                                noiseadd(img335,"s&p",0.3,Out_Dir,(filen+"img335"+extension))
                                noiseadd(img335,"pepper",0.2,Out_Dir,(filen+"img335"+extension))
                                noiseadd(img335,"salt",0.01,Out_Dir,(filen+"img335"+extension))
                                Me_blur_img = Me_blur(img25,(filen+"img25"+extension),Out_Dir)
                                G_blur_img = G_blur(img25,(filen+"img25"+extension),Out_Dir)
                                median_img = median(img25,(filen+"img25"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img25,(filen+"img25"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img25,(filen+"img25"+extension),Out_Dir)
                                noiseadd(img25,"s&p",0.3,Out_Dir,(filen+"img25"+extension))
                                noiseadd(img25,"pepper",0.2,Out_Dir,(filen+"img25"+extension))
                                noiseadd(img25,"salt",0.01,Out_Dir,(filen+"img25"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                hb=cv2.imread(Out_Dir+"hb_"+filename)
                                Me_blur_img = Me_blur(hb,(filen+"hb"+extension),Out_Dir)
                                G_blur_img = G_blur(hb,(filen+"hb"+extension),Out_Dir)
                                median_img = median(hb,(filen+"hb"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(hb,(filen+"hb"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(hb,(filen+"hb"+extension),Out_Dir)
                                noiseadd(hb,"s&p",0.3,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"pepper",0.2,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"salt",0.01,Out_Dir,(filen+"hb"+extension))
                                double_brightness(imgg,Out_Dir,filename)
                                db=cv2.imread(Out_Dir+"db_"+filename)
                                Me_blur_img = Me_blur(db,(filen+"db"+extension),Out_Dir)
                                G_blur_img = G_blur(db,(filen+"db"+extension),Out_Dir)
                                median_img = median(db,(filen+"db"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(db,(filen+"db"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(db,(filen+"db"+extension),Out_Dir)
                                noiseadd(db,"s&p",0.3,Out_Dir,(filen+"db"+extension))
                                noiseadd(db,"pepper",0.2,Out_Dir,(filen+"db"+extension))
                                noiseadd(db,"salt",0.01,Out_Dir,(filen+"db"+extension))
                                contrast(imgg,Out_Dir,filename)
                                ct=cv2.imread(Out_Dir+"ct_"+filename)
                                Me_blur_img = Me_blur(ct,(filen+"ct"+extension),Out_Dir)
                                G_blur_img = G_blur(ct,(filen+"ct"+extension),Out_Dir)
                                median_img = median(ct,(filen+"ct"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(ct,(filen+"ct"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(ct,(filen+"ct"+extension),Out_Dir)
                                noiseadd(ct,"s&p",0.3,Out_Dir,(filen+"ct"+extension))
                                noiseadd(ct,"pepper",0.2,Out_Dir,(filen+"ct"+extension))
                                noiseadd(ct,"salt",0.01,Out_Dir,(filen+"ct"+extension))
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >16)and(count_files <=31)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                hb=cv2.imread(Out_Dir+"hb_"+filename)
                                Me_blur_img = Me_blur(hb,(filen+"hb"+extension),Out_Dir)
                                G_blur_img = G_blur(hb,(filen+"hb"+extension),Out_Dir)
                                median_img = median(hb,(filen+"hb"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(hb,(filen+"hb"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(hb,(filen+"hb"+extension),Out_Dir)
                                noiseadd(hb,"s&p",0.3,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"pepper",0.2,Out_Dir,(filen+"hb"+extension))
                                noiseadd(hb,"salt",0.01,Out_Dir,(filen+"hb"+extension))
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >31)and(count_files <=39)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                hb=cv2.imread(Out_Dir+"hb_"+filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >39) and(count_files <=48)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                '''Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))'''
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >48) and(count_files <=59)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                #Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                '''median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))'''
                                noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                #Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                '''median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))'''
                                noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    if ((count_files >59) and(count_files <=76)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                    filen=os.path.splitext(filename)[0]
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                imgg = Image.open(filepath)
                                #Img_Quality = laplacian(image,filename)
                                img25=dt_rotate(image,Out_Dir,25,filename)
                                img335=dt_rotate(image,Out_Dir,335,filename)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                #Me_blur_img = Me_blur(img45,(filen+"img45"+extension),Out_Dir)
                                #G_blur_img = G_blur(img45,(filen+"img45"+extension),Out_Dir)
                                '''median_img = median(img45,(filen+"img45"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img45,(filen+"img45"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img45,(filen+"img45"+extension),Out_Dir)
                                noiseadd(img45,"s&p",0.3,Out_Dir,(filen+"img45"+extension))
                                noiseadd(img45,"pepper",0.2,Out_Dir,(filen+"img45"+extension))'''
                                #noiseadd(img45,"salt",0.01,Out_Dir,(filen+"img45"+extension))
                                #Me_blur_img = Me_blur(img45,(filen+"img315"+extension),Out_Dir)
                                #G_blur_img = G_blur(img315,(filen+"img315"+extension),Out_Dir)
                                '''median_img = median(img315,(filen+"img315"+extension),Out_Dir)
                                Avg_Blur_img = Avg_blur(img315,(filen+"img315"+extension),Out_Dir)
                                Bi_Blur_img = Bi_blur(img315,(filen+"img315"+extension),Out_Dir)
                                noiseadd(img315,"s&p",0.3,Out_Dir,(filen+"img315"+extension))
                                noiseadd(img315,"pepper",0.2,Out_Dir,(filen+"img315"+extension))'''
                                #noiseadd(img315,"salt",0.01,Out_Dir,(filen+"img315"+extension))
                               # if Img_Quality >= 200:
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                noiseadd(image,"s&p",0.3,Out_Dir,filename)
                                noiseadd(image,"pepper",0.2,Out_Dir,filename)
                                noiseadd(image,"salt",0.01,Out_Dir,filename)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    elif ((count_files >76)and(count_files <=105)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                #Img_Quality = laplacian(image,filename)
                                #if Img_Quality <= 200:
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                Me_blur_img = Me_blur(image,filename,Out_Dir)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                median_img = median(image,filename,Out_Dir)
                                Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                imgg = Image.open(filepath)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")
                except Exception:
                    pass
    elif ((count_files >105) and (count_files <=150)):
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                            #print(extension )
                            # Check if the file is an image
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                shutil.copy2(filepath, Out_Dir)
                                image = cv2.imread(filepath) # reads the image
                                #Img_Quality = laplacian(image,filename)
                                #if Img_Quality <= 200:
                                #Me_blur_img = Me_blur(image,filename,Out_Dir)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                #median_img = median(image,filename,Out_Dir)
                                #Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                #Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                imgg = Image.open(filepath)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                    print("Image Augumentation Successfull")    
                except Exception:
                    pass
        #else ((count_files >150) and (count_files <=200)):
    else:
            for img in files:
                try:
                    Img_Gen_Dir = (str(ip))
                    Out_Dir = (str(output_path)+"/"+str(dir)+"/")
                    isExist = os.path.exists(Out_Dir)
                    if not isExist:
                        os.makedirs(Out_Dir)
                    Next_Dir = str(op)
                    List_Dir = (str(main_path)+"/"+str(dir)+"/")
                    #data_rotation = data_roation(Img_Gen_Dir,Out_Dir,45,List_Dir)
                    #data_flip_img = data_flip(Next_Dir,Out_Dir)
                    #data_flip(Next_Dir,Out_Dir)
                    #for root, _, files in os.walk(Out_Dir):
                    #for file in files:
                            #print(file)
                            # Get the filepath
                    filepath = os.path.join(List_Dir, img)
                    print(filepath)
                            # Get the filename
                    filename = os.path.basename(filepath)
                    print(filename)
                            # Get the extension
                    extension = os.path.splitext(filepath)[1]
                    if extension in [".jpg", ".jpeg", ".png"]:
                                #Load the image
                                #image = mpimg.imread(filepath)
                                image = cv2.imread(filepath) # reads the image
                                shutil.copy2(filepath, Out_Dir)
                                #Img_Quality = laplacian(image,filename)
                                #if Img_Quality <= 200:
                                #Me_blur_img = Me_blur(image,filename,Out_Dir)
                                img45=dt_rotate(image,Out_Dir,45,filename)
                                img315=dt_rotate(image,Out_Dir,315,filename)
                                G_blur_img = G_blur(image,filename,Out_Dir)
                                #median_img = median(image,filename,Out_Dir)
                                #Avg_Blur_img = Avg_blur(image,filename,Out_Dir)
                                #Bi_Blur_img = Bi_blur(image,filename,Out_Dir)
                                #data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                                imgg = Image.open(filepath)
                                half_brightness(imgg,Out_Dir,filename)
                                double_brightness(imgg,Out_Dir,filename)
                                #contrast(imgg,Out_Dir,filename)
                            #else:
                             #   data_bright_img = data_bright(Next_Dir,Out_Dir,[0.3,1])
                    #data_bright_img = data_bright(Img_Gen_Dir,Out_Dir,[0.3,1])
                                gray_img = img_gray(image,filename,Out_Dir)

                except Exception:
                    pass