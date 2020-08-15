import sys
from sendStatToHTML import HtmlManager
from sendStatToHTML import AWSmanager
major_stations = {"NYG": "Grand Central",
"NYP" : "New York Penn Station",
"125" : "Harlem - 125th Street", 
"153" : "Yankees - E. 153rd Street", 
"FRD" : "Fordham", 
"NRO" : "New Rochelle", 
"PCX" : "Port Chester",
"GCH" : "Greenwich",
"STM" : "Stamford", 
"NCN" : "New Canaan", 
"SNW" : "South Norwalk",
"DBY" : "Danbury",
"BRP" : "Bridgeport",
"WBR" : "Waterbury",
"NHV" : "New Haven Union Station",
"STS" : "New Haven - State St.",
"OSB" : "Old Saybrook",
"NLC" : "New London",
"HFD" : "Hartford",
"SPG" : "Springfield"}

class Menu:
  def __init__(self, major_stations):
    self.stations = major_stations
    self.showMenu()
    
  
  def showMenu(self):
    code = input("Please enter a station code for a MAJOR New Haven Line station.\n")
    while code not in self.stations:
        print("ERROR: Not in Database or is not a major/terminal station")
        code = input("")
    print(f"Sending station {self.stations[code]} to timetable making department.")
    self.manager = HtmlManager(self.stations[code])
    self.manager.create_html()
    self.manager.save_html_file()
    self.aws = AWSmanager()
    self.aws.save_to_s3()
    self.aws.listBucketFile("lmtd-class")
    
   

    