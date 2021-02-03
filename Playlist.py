from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    def add_song(self, title):
        new_song = Song(title)
        new_song.set_next_song(self.__first_song)
        # new_song.__next_song = self.__first_song
        self.__first_song = new_song

    def find_song(self, title):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            if current_node.get_title() == title:
                return counter
            else:
                counter += 1
                current_node = current_node.get_next_song()
        return -1

    def remove_song(self, title):
        current_node = self.__first_song
        temp_node = None

        if self.__first_song.get_title() == title:
            self.__first_song = self.__first_song.get_next_song()
            print('Item Removed')
            return

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

    def length(self):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            counter += 1
            current_node = current_node.get_next_song()
        return counter

    def print_songs(self):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            print(f"{counter + 1}. {current_node.get_title()}")
            counter += 1
            current_node = current_node.get_next_song()
