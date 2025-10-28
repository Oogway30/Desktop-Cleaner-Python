import os
def Sort(location):
    os.chdir(location)
    files = os.listdir()
    fileExtensions = []
    for i in files:
        if len(os.path.splitext(i)[1]):
            fileExtensions.append(os.path.splitext(i)[1][1:].upper())
        else:
            continue


    for i in set(files):
        if len(os.path.splitext(i)[1]):
            os.rename(f"{location}/{i}",f"{location}/{os.path.splitext(i)[1][1:].upper()}/{i}")
        else:
            continue
    print("Done sorting!")
