class SongService:

    def __init__(self, sid, l, sname):
        self.__songid = sid
        self.__lyrics = l
        self.__singername = sname

    def __str__(self):
        return f" Id :{self.__songid} \n Lyrics: {self.__lyrics} \n Songname:{self.__singername}"

    def set_songid(self, sid):
        self.__songid = sid

    def set_lyrics(self, l):
        self.__lyrics = l

    def set_singername(self, sname):
        self.__singername = sname

    def get_sid(self):
        return self.__sid

    def get_lyrics(self):
        return self.__lyrics

    def get_singername(self):
        return self.__singername


if __name__ == "__main__":
    s = SongService(11, "memories bring back ", "Memories")
    print(s)
