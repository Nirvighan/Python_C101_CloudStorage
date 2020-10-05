import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')

        dbx.files_upload(f.read(),file_to)



def main():
    access_token = "3r652F1gy6QAAAAAAAAAAXPSMVagVaDPkYVvDWbjOEJZtuf3P1gZDEfdAPilPTCz"
    transferData = TransferData(access_token)
    
    file_from = input("ENTER THE FILE PATH TO TRANSFER :")
    file_to = input("ENTER THE FULL PATH TO UPLOAD TO DROPBOX :" )

    transferData.uploadFile(file_from,file_to)

    print("YOUR FILE HAS EEN MOVED TO THE DROPBOX")


main()