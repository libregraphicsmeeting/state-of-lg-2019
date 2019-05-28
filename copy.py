from shutil import copyfile

f = open("slides.list")
i = 2
for line in f.readlines():
    dst = "presentation/%04d" % i + ".png"
    print(dst)
    copyfile(line.rstrip(), dst)
    i = i + 1
    
