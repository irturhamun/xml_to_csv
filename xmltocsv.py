import xml.etree.ElementTree as ET
import PySimpleGUI as sg
import csv
import tkinter
layout = [  [sg.Text('Insert XML File to Convert into CSV')],
            [sg.Text('Insert XML file', size = (15,1)),sg.InputText(), sg.FileBrowse()],
            [sg.Output(size=(80, 20))],
            [sg.OK(), sg.Cancel()]]
window = sg.Window('XML to CSV', layout)
while True:
# file = 'C:\\Users\\irmansyah.turhamun\\PycharmProjects\\untitled1\\Production - Digital Taxonomy.Current.V275.xml'
    event, values = window.Read()
    file = values[0]
    tree = ET.parse(file)
    root = tree.getroot()
    dump = []
    print(len(dump))
    f = open('dump.csv', 'w')
    w = csv.writer(f)
    for element1 in root.findall ('./TSel_Channel_Taxonomy/UXP_Context_ID'):
        print (element1.text)
        path0 = './TSel_Channel_Taxonomy/Next_Level_Next_Menu_Level'
        path1 = '/UXP_Context_ID'
        patha = path0 + path1
        ml2 = []
        for index in root.iterfind(patha):
            ml2.append(index.text)
        for index1 in range(len(ml2)):
            path0 = './TSel_Channel_Taxonomy/Next_Level_Next_Menu_Level['
            path1 = ']/Next_Level_Next_Menu_Level/UXP_Context_ID'
            path2 = ']/UXP_Context_ID'
            path3 = ']/Next_Level_Product_Offer_Level/UXP_Context_ID'
            path4 = ']/Next_Level_Next_Menu_Level['
            path5 = ']/Next_Level_Next_Menu_Level['
            path6 = ']/Next_Level_Product_Offer_Level['
            path7 = ']/Product_Offer_ID'
            z = index1 + 1
            c = str(z)
            pathh = path0 + c + path2
            pathi = path0 + c + path1
            ml3 = []
            for indexa in root.iterfind(pathh):
                print("|-->\t", indexa.text)
            for index2 in root.iterfind (pathi):
                ml3.append(index2.text)
            for index3 in range (len(ml3)):
                y = index3 + 1
                d = str(y)
                ml4 = []
                pathj = path0 + c + path4 + d + path3
                pathk = path0 + c + path5 + d + path2
                for index2 in root.iterfind(pathk):
                    print("|\t|-->\t", index2.text)
                for index3 in root.iterfind(pathj):
                    # print("|\t|\t|-->\t", index3.text)
                    ml4.append(index3.text)
                for index4 in range (len(ml4)):
                    x = index4 + 1
                    e = str(x)
                    pathl = path0 + c + path5 + d + path6 + e + path7
                    pathm = path0 + c + path5 + d + path6 + e + path2
                    for index5 in root.iterfind(pathm):
                        print("|\t|\t|-->\t", index5.text)
                    for index6 in root.iterfind(pathl):
                        print("|\t|\t|\t|-->\t", index6.text)
                    w.writerow([element1.text , indexa.text , index2.text , index5.text , str(index6.text)])
    from pandas.io.parsers import read_csv
    data = read_csv('dump.csv')
    filtered_data = data.dropna(axis='columns', how='all')
    output = 'clean_dump.csv'
    filtered_data.to_csv(output)
    data
    filtered_data = data.dropna(axis='columns', how='all')
    filtered_data

    import fileinput
    import sys
    import os
    inputFileName = output
    outputFileName =  file + ".csv"
    with open(outputFileName, "w") as outfile:
        for line in fileinput.input(
            [inputFileName],
            inplace=False):
            if fileinput.isfirstline():
                outfile.write('SN,ML1,ML2,ML3,ML4,Business_ID\n')
            else:
                outfile.write(line)
    print("File Output =",outputFileName)
    if event in (None, 'Cancel'):
        break

window.Close()