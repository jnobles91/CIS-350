class GameEntry:
    def __init__(self, name="", score=0):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score


class Scores:
    def __init__(self, max_entries=10):
        self._max_entries = max_entries
        self._entries = []

    def add(self, entry):
        if len(self._entries) < self._max_entries:
            self._entries.append(entry)
        elif entry.get_score() > self._entries[-1].get_score():
            self._entries[-1] = entry

    def remove(self, index):
        if index < 0 or index >= len(self._entries):
            raise IndexError("Invalid index")
        removed_entry = self._entries.pop(index)
        return removed_entry

    def get_game_entries(self):
        return self._entries

    def print_scores(self):
        for entry in self._entries:
            print(f"{entry.get_name()} : {entry.get_score()}")

    def num_ent(self):
        return len(self._entries)
    
    def search_score(self, player_name):
        for entry in self._entries: #iterate through the list till we find a name matching the one we're looking for
            if entry.get_name() == player_name: 
                return entry.get_score() #return the score if we find it
        else:
            return -1 #return -1 if we don't find that player
    
    def average_max_scores(self):
        sum = 0 #create a running sum of all the scores
        if len(self._entries) > 0: #check to make sure there are entries
            for entry in self._entries: #iterate through the list adding the scores up
                sum += entry.get_score()
            return sum / len(self._entries) #return the average
        else:
            return -1 #return -1 if there are no scores

    def find_min_max_scores(self):
        if len(self._entries) > 0: #check to make sure there are scores
            scores = set() #create a set to store all of the unique scores
            for entry in self._entries:
                scores.add(entry.get_score()) #add the score of each entry to the set
            min_score, max_score = min(scores), max(scores) #find the minimum and maximum 
            return min_score, max_score
        else:
            return -1,-1 #return an error if there are no scores


def insertion_sort(entries, ascending=True):
    num_entries = len(entries)
    for i in range(1, num_entries):
        key = entries[i]
        j = i - 1
        if ascending:
            # Sort in ascending order
            while j >= 0 and entries[j].get_score() > key.get_score():
                entries[j + 1] = entries[j]
                j -= 1
        else:
            # Sort in descending order
            while j >= 0 and entries[j].get_score() < key.get_score():
                entries[j + 1] = entries[j]
                j -= 1
        entries[j + 1] = key


if __name__ == "__main__":
    mike = GameEntry("Mike", 1105)
    rob = GameEntry("Rob", 750)
    paul = GameEntry("Paul", 720)
    anna = GameEntry("Anna", 660)
    rose = GameEntry("Rose", 590)
    jack = GameEntry("Jack", 510)
    jill = GameEntry("Jill", 740)

    BAM = Scores(10)
    BAM.add(mike)
    BAM.add(rob)
    BAM.add(paul)
    BAM.add(anna)
    BAM.add(rose)
    BAM.add(jack)
    BAM.add(jill)

    #Testing functions I added
    #search score
    print(BAM.search_score("Mike")) #expect 1105
    print(BAM.search_score("Zelda")) #expect -1
    print(BAM.average_max_scores()) #expect 725
    print(BAM.find_min_max_scores()) #expect 510, 1105

    #testing on empty set
    Empty_Scores = Scores(10)
    print(Empty_Scores.search_score("Mike")) #expect 1105
    print(Empty_Scores.search_score("Zelda")) #expect -1
    print(Empty_Scores.average_max_scores()) #expect 725
    print(Empty_Scores.find_min_max_scores()) #expect 510, 1105




    print("Num of Entries:", BAM.num_ent())
    BAM.print_scores()

    # Testing removal of an entry
    BAM.remove(3)  # Remove the entry at index 3 (Anna)
    print("After removing entry at index 3:")
    BAM.print_scores()

    entries = BAM.get_game_entries()
    insertion_sort(entries, ascending=True)
    print("Sorted Entries in Ascending Order:")

    for entry in entries:
        if entry.get_name():
            print(f"{entry.get_name()} : {entry.get_score()}")
