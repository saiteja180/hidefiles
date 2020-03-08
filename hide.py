import os
import subprocess
import sys
import getopt
from zipfile import ZipFile

def create_zip_file(dirname, zipfilename, filter):
    # create a zip file
    with ZipFile(zipfilename, 'w') as zip:
        for foldername, subfolders, filenames in os.walk(dirname):
            for file in filenames:
                if filter(file):
                    filepath = os.path.join(foldername, file)
                    print(filepath)
                    zip.write(filepath)

def main(argv):
    # declare variables
    dirname,zipfilename ,filetypes,sourceimage, destinationfile= ('',)*5

    try:
        opts, args = getopt.getopt(argv, "hd:z:l:s:c:", ["dDirectory=", "zFile=", "lTypes=","sSourceimage=","cDestinationfile="])

    except getopt.GetoptError:
        print('hide.py -d <directory name> -z <zip file name> -l <comma separated file types> eg:-jpg,jpeg,txt -s <source image name> -c <destinaion image name>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('hide.py -d <directory name> -z <zip file name> -l <comma separated file types eg:-jpg,jpeg,txt > -s <source image name> -c <destinaion image name>')
            print('eg:- hide.py -d C:\FolderName -z zipfilename.zip -l py,jpg -s source.jpg -c destination.jpg')
            sys.exit()
        elif opt in ("-d", "--dDirectory"):
            dirname = arg
        elif opt in ("-z", "--zFile"):
            zipfilename = arg
        elif opt in ("-l", "--lTypes"):
            filetypes = arg
        elif opt in ("-s", "--sSourceimage"):
            sourceimage = arg
        elif opt in ("-c", "--cDestinationfile="):
            destinationfile = arg

    types = filetypes.split(',')

    print("file types:- ", types)
    print("directory name:- ", dirname)
    print("zip file name:- ", zipfilename)
    print("source image file:-", sourceimage)
    print("destination image file:- ",destinationfile)

    # get absolute path  use '..' inside os.path.abspath('') to traverse back to parent  eg:- os.path.abspath('../..')
    p = os.path.abspath('')
    # create filter for files
    fileterfiles = lambda name: [i for i in types if i in name.split('.')]
    create_zip_file(dirname, zipfilename, fileterfiles)

    # cmd command to hide zip file under image file
    command = "copy /b"+ " " +sourceimage+ " "+"+"+zipfilename+" " + destinationfile
    result = subprocess.getoutput("cd" + " " + p + " &&  " + command)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])
