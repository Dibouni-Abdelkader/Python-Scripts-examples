def changTo(path,source,dest):
    import os
    os.chdir(path)
    for file in os.listdir('.'):
        if file.endswith('.' + source):
            os.rename(file, file[:-3] + '.' + dest)
            print(file)
            

        
