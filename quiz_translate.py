
from googletrans import Translator
import csv
import sys 
import shutil
import os
import urllib.request

translator = Translator()

absolute_path_csv = ''.join(sys.argv[1:])
copy_file_label = "(copy)"
test_conn_host = "https://google.com"

original_q_list = []
translated_q_list = []

def isConnected(host):
    try:
        urllib.request.urlopen(host)
        return True
    except Exception:
        return False

def translateQ(words,lang):
    if isConnected(test_conn_host):
        translated_text = translator.translate(words,dest=lang).text
        return translated_text

def choseLanguage():
    print("[+]Insert language for translation in ISO 639-1 format -> Example:")
    print("[+]Italian -> it")
    print("[+]English -> en")
    print("[+]German -> de")
    print("[+]ecc..\n")
    lang = str(input("[+]The language you want to select is: "))
    return lang

def getNewPath(path):
    get_csv_file = os.path.basename(path)
    get_csv_file_name = os.path.splitext(get_csv_file)[0]
    new_csv_name = get_csv_file_name + copy_file_label + ".csv"
    curr_path_location = os.getcwd()

    new_csv_file_dest = curr_path_location + "/" + new_csv_name
    return new_csv_file_dest
    
def main():
    try:
        lang = choseLanguage()

        with open(absolute_path_csv, 'r', encoding='utf-8') as orig_csv:
            original_csv_reader = csv.reader(orig_csv)

            for row in original_csv_reader:
                original_q_list.append(row[1])
            
        print(original_q_list)
        print("\n")
        print("[*] I am translating the questions...\n")
        print("\n"*2)

        for question in original_q_list:
            question_to_translate = translateQ(question,lang)
            translated_q_list.append(question_to_translate)

        print(translated_q_list)
        print("\n"*2)
        
        new_csv_file_dest = getNewPath(absolute_path_csv)

        if not os.path.isfile(new_csv_file_dest):
            shutil.copyfile(absolute_path_csv,new_csv_file_dest)
        else:
            print("[-] I can't create a new csv file for translations because it already exists in the same directory!")
            print("[-] The File will be overwritten!")

        print("[*] I Proceed with the remaining operations...\n")
        
        try:
            file_txt_in = open(new_csv_file_dest, 'r', encoding='utf-8')
            r = file_txt_in.read()

            for elem, rep in zip(original_q_list, translated_q_list):
                r = r.replace(elem,rep)
            
            file_txt_out = open(new_csv_file_dest, 'w', encoding='utf-8')
            file_txt_out.write(r)
            
            file_txt_out.close()
        except OSError:
            print("[-] Could not read and/or write the csv-copy file, Retry..")
            sys.exit(0)
        
        print("[+] Operations successfully completed!")
        print("[+] Look at the new csv-copy file to see the results ;)")
        sys.exit(0)

    except KeyboardInterrupt:
        print("[-] CRTL+C => aborting the script")
        sys.exit(0)

if __name__ == '__main__':
    main()


