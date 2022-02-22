from msilib.schema import RemoveFile
import os
import shutil
import time
def main():
    dfc=0
    dic=0
    path="C:\Users\user\Desktop\Whitehatjr\PROJECT-98"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>=getfileorfolderage(rootfolder):
                removefolder(rootfolder)
                dfc+=1
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if seconds>=getfileorfolderage(folderpath):
                        removefolder(folderpath)
                        dfc+=1 
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if seconds>=getfileorfolderage(filepath):
                        RemoveFile(filepath)
                        dic+=1  
    else:
        print("Path Not Found")
    print("Total Folders Deleted=",dfc)
    print("Total Files Delted=",dic)   
def removefolder(path):
    if not shutil.rmtree(path):
        print("DELETED")
    else:
        print("UnAble To Delete")
def removefile(path):
    if not os.remove(path):
        print("DELETED")
    else:
        print("Unable To Delete")
def getfileorfolderage(path):
    ct=os.stat(path).st_ctime
    return ct
main()    

