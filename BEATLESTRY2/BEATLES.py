import os
import sys

def main():
    filePath = ""
    albumInput = 0
    ifAlbumTen = 0
    album = ""
    albumList = []
    songInput = 0
    songList = []
    song = ""
    end = "NOTEMPTY"

    filePath = "./public/TheBeatlesAnnotations2/chordlab/TheBeatles"

    space()

    print("AlBUMS: ")

    albumList = displayAlbums(filePath)
    albumInput = getAlbumInput()

    if albumInput == 10:
        ifAlbumTen = ifTen()
    if ifAlbumTen == 1:
        albumInput = 101
    elif ifAlbumTen == 2:
        albumInput = 102

    album = getFullAlbumName(albumInput,albumList,filePath)
    songList,filePath = displaySongs(filePath, album)
    songInput = getSongInput(songList)
    song,filePath = getFullSongName(songInput,songList,filePath)
    space()

    getSongData(song,album)

    while end != "":
        end = input("PRESS ENTER TO RESTART")

    os.execl(sys.executable, sys.executable, *sys.argv)


def space():
    for i in range(15):
        print()

def getSongData(song,album):
    songList = []
    fileList = set()
    dataList = []
    filePath = ""
    for i in range(3):
        if i == 0:
            filePath = "./public/TheBeatlesAnnotations2/chordlab/TheBeatles"
        elif i == 1:
            filePath = "./public/TheBeatlesAnnotations2/keylab/TheBeatles"
        else:
            filePath = "./public/TheBeatlesAnnotations2/seglab/TheBeatles"

        filePath+=("/" + album )

        songList = os.listdir(filePath)

        for file in songList:
            if file.startswith(song):
                fileList.add(file)

        for line in fileList:
            if line.endswith(".lab"):
                data = open(filePath +"/" + line,"r")
                dataList.append(data)

    for d in dataList:
        print(song + " DATA: ")
        print()
        for line in d:
            print(line)
        print()
        print()

def getFullSongName(songInput,songList,filePath):
    songInput = songInput
    songList = songList
    song = ""
    fp = filePath
    song = songList[songInput-1]
    fp += "/" + song
    return song,fp

def getSongInput(songList):
    songInput = ""
    songInputInt = -1
    print()
    while songInputInt < 1 or songInputInt > len(songList):
        try:
            print("PRESS ENTER TO GO BACK TO ALBUM LIST OR")
            songInput = input("ENTER SONG NUMBER TO SEARCH SONG DATA: ")

            if songInput == "":
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                songInputInt = int(songInput)
        except:
            print("ERROR PLEASE TRY AGAIN")

    for i in range(7):
        print()
    return songInputInt

def displaySongs(fp, album):

    filePath = ""
    filePath+= fp
    filePath+= ("/" + str(album))
    fileList = os.listdir(filePath)
    fileList.sort()
    songSet = set()
    songList = []

    for song in fileList:
        song = song[:-4]
        songSet.add(song)

    for song in songSet:
        songList.append(song)
        print()
    songList.sort()

    print("ALBUM: " + album)
    print()
    print("TRACKLIST:")
    for song in songList:
        print(song)
    return songList,filePath

def getFullAlbumName(albumInput,albumList,fp):
    albumList = []
    albumList.sort()
    albumIndex = 0
    album = ""

    if albumInput < 10:
        albumIndex = (albumInput - 1)
    elif albumInput == 101:
        albumIndex = 9
    elif albumInput == 102:
        albumIndex = 10
    else:
        albumIndex = albumInput

    albumList = os.listdir(fp)
    albumList.sort()

    del albumList[0]
    album = albumList[albumIndex]

    return album

def displayAlbums(fp):
    albumList = []
    albumList = os.listdir(fp)
    albumList.sort()
    del albumList[0]
    for album in albumList:
        if (album == "10CD1_-_The_Beatles"):
            album += " (AKA The White Album Side 1)"
        elif(album == "10CD2_-_The_Beatles"):
            album += " (AKA The White Album Side 2)"
        print(album)
    print()

def getAlbumInput():
    num = -1
    while num < 1 or num > 12:
        try:
            num = int(input("ENTER THE NUMBER OF THE ALBUM YOU WOULD LIKE TO SEARCH: "))
            if(num < 1 or num > 12):
                print("NUMBER ENTERED DOES NOT CORRESPOND TO AN ALBUM")
        except:
            print("INPUT WAS NOT VALID PLEASE RETRY")
    return num

def ifTen():
    ifTen = -1  # place holder

    while ifTen != 1 and ifTen != 2:
        try:
            ifTen = int(input("ENTER 1 FOR CD1 OR 2 FOR CD2: "))
            if (ifTen != 1 and ifTen != 2):
                print("NUMBER ENTERED WAS NEITHER 1 OR 2")
        except:
            print("INPUT WAS NOT VALID PLEASE RETRY")
    return ifTen

main()
