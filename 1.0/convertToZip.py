import os
import io
import zipfile



def rename(dir_file_path):
    old_dir_file_path = dir_file_path
    zip_dir_file_path = dir_file_path.replace("xlsm", "zip")
    
    # print(old_dir_file_path, new_dir_file_path)

    os.rename(old_dir_file_path, zip_dir_file_path)

    # with zipfile.ZipFile(new_dir_file_path) as zf:
    #     # with open(zf, 'rb') as f:
    #     #     print(f.read())

    #     with io.TextIOWrapper(zf.open("xl/vbaProject.bin"), 'rb') as f:
    #         print(f.read())
    new_zip_dir_file_path = dir_file_path.replace(".xlsm", "2.zip")

    with zipfile.ZipFile(zip_dir_file_path, 'a') as inzip, zipfile.ZipFile(new_zip_dir_file_path, "w") as outzip:
        # Iterate the input files
        for inzipinfo in inzip.infolist():
            # Read input file
            with inzip.open(inzipinfo) as infile:
                if inzipinfo.filename == "xl/vbaProject.bin":
                    content = infile.read()
                    print(content)
                    # Modify the content of the file by replacing a string
                    print(content.find(b"DPB"))
                    content = content.replace(b"DPB", b"DPX")
                    # inzipinfo.filename.
                    outzip.writestr(inzipinfo.filename, content)
                    break
                    # Write conte
                    # outzip.writestr(inzipinfo.filename, content)
                else: # Other file, dont want to modify => just copy it
                    content = infile.read()
                    outzip.writestr(inzipinfo.filename, content)
                    # print('inzipinfo:', inzipinfo)
                    pass