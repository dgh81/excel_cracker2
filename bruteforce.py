import win32com.client
import time
import timeit

excel = win32com.client.Dispatch("Excel.Application")

excel_file = r'C:\Users\Bruger\OneDrive\Desktop\excelpassword\file_password.xlsx'

password_file = r'C:\Users\Bruger\OneDrive\Desktop\excelpassword\password_16.txt'

password_list = []

def brute_it():
    try:
        with open(password_file, 'r', encoding='utf-8') as pwd:
            passwords = pwd.readlines()
            for password in passwords:
                password_list.append(password.replace('\n', ''))
    except:
        print("error")

    i = 0
    for password in password_list:
        try:
            wb = excel.Workbooks.Open(excel_file, False, True, None, password)
            print(password)
            wb.Unprotect(password)
            print("successful password: " + password)
            excel.DisplayAlerts = False
            excel.Quit()
            time.sleep(1)
            break
        except:
            # print(i)
            i += 1
            continue


# brute_it()

print('bruteit: ', timeit.timeit(brute_it, number=1), ' seconds')