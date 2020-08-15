import boto3

class HtmlDocument:
    #that lets you initialize some HTML for a new document.
    def __init__(self,content):
        self.content = content
        

class HtmlManager:
    #that defines functions that let you create a new HTML document, 
    # and save the document to your files.
    # write-html.py

    def __init__(self, station):
        self.document = None
        self.station = station

    def create_html(self):
        
        message = f"""<html>
        <head>NEW HTML FILE</head>
        <body><p>YOUR STATION IS: {self.station}</p>
        <p> To S3 I go. </p>
        </body>
        </html>"""
        doc = HtmlDocument(message)
        self.document = doc
        print(doc)

        
    def save_html_file(self):
        f = open('station.html','w')
        f.write(self.document.content)
        f.close()


class AWSmanager:
    def __init__(self):
        pass
    def save_to_s3(self):
        s3 = boto3.client('s3')
        boto3.client('s3').upload_file('station.html', 'lmtd-class', 'raymond.html')

#manager = HtmlManager(station)
#manager.create_html()
#manager.save_html_file()
aws = AWSmanager()
aws.save_to_s3()

