import os, sys
from time import sleep
import pandas as pd



# Rename large amount of pdf files based on transco file rename_excel.xlsx



try : 


    # 1 - Read the csv OU excel and put data into a dataframe (un tableau) 
    DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    excel_file_path = DIRECTORY + r"\Rename_folder\rename_excel.xlsx"
    df = pd.read_excel(excel_file_path)  


    # 2 - Créer des listes de file_name à partir du tableau
    old_names = df['old_name'].tolist()
    new_names = df['new_name'].tolist()



    # 3 - Loop over the elements in list to change each names
    path = DIRECTORY + "/Rename_folder/Renamed/"
    for x in range(len(old_names)) :

        try : 
            path_old_name = path + old_names[x] 
            path_nex_name = path + new_names[x] 

            os.rename(path_old_name, path_nex_name)
            print('ok ', new_names[x])


        except Exception as e : 
            print(e)
            print(f"Problem with file : {old_names[x]} --> {new_names[x]}")
            sys.exit()



    print(f"Script finished. \n{len(old_names)} filenames updated.")



except Exception as e :
    print(e) 
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    message = str(exc_type) + ". Line : " + str(exc_tb.tb_lineno)
    print(message, "\n")
    sys.exit()