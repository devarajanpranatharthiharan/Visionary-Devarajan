import os
import shutil

def input_path():
    path = input("Enter the folder path")
    allfiles= os.listdir(path)
    return(path,allfiles)

def file_types (path):
    Images = [".jpg", ".png", ".jpeg", ".gif"]
    Documents = [ ".pdf", ".docx", ".txt", ".xlsx"]
    Videos = [ ".mp4", ".mkv", ".avi"]
    Audio = [".mp3", ".wav"]
    Executables =[ ".exe", ".bat", ".msi"]
    Archives = [".zip", ".rar", ".7z"]
#os.makedirs("Images")
#os.makedirs(path +"/"+"Images")
    return(Images,Documents,Videos,Audio,Executables,Archives)

def folder_check(path):
    if os.path.exists(path +"/"+"Images"):
        print("Image Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Images")
    if os.path.exists(path+"/"+"Videos"):
        print("Videos Folder Already Exists")
    else:
        os.makedirs (path+"/"+"Videos")
    if os.path.exists(path +"/"+"Documents"):
        print("Documents Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Documents")   
    if os.path.exists(path +"/"+"Audio"):
        print("Audio Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Audio")
    if os.path.exists(path +"/"+"Executables"):
        print("Executables Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Executables")   
    if os.path.exists(path +"/"+"Archives"):
        print("Archives Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Archives")    
    if os.path.exists(path +"/"+"Others"):
        print("Others Folder Already Exists")
    else:
        os.makedirs(path+"/"+"Others")                                
    
# # elif os.makedirs(path +"/"+"Images"):
# #     print("Image Folder Already Exists")    
# elif os.path.exists(path+"/"+"Videos"):
#     print("Videos Folder Already Exists")
# elif os.path.exists(path+"/"+"Documents"):
#     print("Documents Folder Already Exists")  
# elif os.path.exists(path+"/"+"Audio"):
#     print("Audio Folder Already Exists")
# elif os.path.exists(path+"/"+"Executables"): 
#     print("Executables Folder Already Exists")   
# elif os.path.exists(path+"/"+"Archives"): 
#     print("Archives Folder Already Exists") 
# elif os.path.exists(path+"/"+"Others"): 
#     print("Others Folder Already Exists")         
# else:
#     os.makedirs(path+"/"+"Images")
    
#     os.makedirs (path+"/"+"Documents")
#     os.makedirs (path+"/"+"Audio")
#     os.makedirs (path+"/"+"Executables")
#     os.makedirs (path+"/"+"Archives")
#     os.makedirs (path+"/"+"Others")

def allfiles (path,Images,Documents,Videos,Audio,Executables,Archives):
    print(allfiles)
    for files in allfiles:
        filename,extension=os.path.splitext(files)
        print(filename,extension)
        if extension in Images:
            Source = os.path.join(path, files)
            Destination= os.path.join(path,"Images",files)
            # shutil.move(path+"/"+files,path+"/"+Images)
            shutil.move(Source,Destination)
        elif extension in Documents:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Documents",files)
            shutil.move(Source,Destination)
        elif extension in Videos:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Videos",files)
            shutil.move(Source,Destination)    
        elif extension in Audio:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Audio",files)
            shutil.move(Source,Destination) 
        elif extension in Executables:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Executables",files)
            shutil.move(Source,Destination) 
        elif extension in Archives:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Archives",files)
            shutil.move(Source,Destination)
        else:
            Source = os.path.join(path,files)
            Destination = os.path.join(path,"Others",files)
            shutil.move(Source,Destination)     

    def filesperation ():
        path,allfiles = input_path()
        folders = folder_check()
    filesperation()    


    
        
    
    #   elif b in Documents:
    #     shutil.move(path+"/"+"Documents", os.path.join(path,"Documents",files))  
    #   elif b in Videos:
    #     shutil.move(path+"/"+"Videos",os.path.join(path,"Videos",files))
    #   elif b in Audio:
    #     shutil.move (path+"/"+"Audio",os.path.join(path,"Audio",files))
    #   elif b in Executables:
    #     shutil.move (path+"/"+"Executables",os,path.join(path, "Executables",files))
    #   elif b in Archives:
    #     shutil.move (path+"/"+"Archives",os,path.join(path, "Archives",files))
    #   else:
    #         shutil.move (path+"/"+"Others",os,path.join(path, "Others",files))




        
        


        



    




# if os.path.exists(path):
#     print("Path Exists")
#     allfiles= os.listdir(path)
#     print(allfiles)
#     Images = [".jpg", ".png", ".jpeg", ".gif"]
#     Documents = [ ".pdf", ".docx", ".txt", ".xlsx"]
#     Videos = [ ".mp4", ".mkv", ".avi"]
#     Audio = [".mp3", ".wav"]
#     Executables =[ ".exe", ".bat", ".msi"]
#     Archives = [".zip", ".rar", ".7z"]
#     for file in allfiles:
#         a,b=os.path.splitext(file)    
#         print(a,b)
# else:
#     print("No Location found")
