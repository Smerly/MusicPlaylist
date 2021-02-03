from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

    def add_song(self, title):
        new_song = Song(title)
        new_song.set_next_song(self.__first_song)
        # new_song.__next_song = self.__first_song
        self.__first_song = new_song

    # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

    def find_song(self, title, song):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            if current_node.get_title() == title:
                return counter
            else:
                counter += 1
                current_node = current_node.get_next_song()
        return -1

        # if title in self.songs:
        #     return self.songs.get_title()
        # else:
        #     return -1

        # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed.

    def remove_song(self, title):
        current_node = self.__first_song
        temp_node = None

        while current_node != None:

            if current_node.get_title() == title:
                temp_node = current_node
                current_node = current_node.get_next_song()
                temp_node.set_next_song(current_node.get_next_song())
            return True
        return False

        #  -----

        # print(current_node.__next_song)
        # return True
        # ^
        # temp_node = current_node
        # current_node = current_node.get_next_song()
        # else:
        #     counter += 1
        #     current_node = current_node.get_next_song()

        # find the song that you want to remove
        # assign the previous song next to the next, next song

    # TODO: Create a method called length, which returns the number of songs in the playlist.

    def length(self):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            counter += 1
            current_node = current_node.get_next_song()
        return counter

    # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

    # Example:
    # 1. Song Title 1
    # 2. Song Title 2
    # 3. Song Title 3

    def print_songs(self):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            print(f"{counter + 1}. {current_node.get_title()}")
            counter = counter + 1
            current_node = current_node.get_next_song()
