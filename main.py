# load csv file from C:/Users/nilst/Downloads/bw.csv
import csv
with open('C:/Users/nilst/Downloads/bwexp.csv', newline='') as csvfile:
    passwords = csv.reader(csvfile, delimiter=',', quotechar='|')
    print(passwords)
    for row in passwords:
        print("Folder: "+row[0]+" Favorite: "+row[1]+" Type: " +
              row[2]+" name: "+row[3]+"notes"+row[4]+"field"+row[5])

        # folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
