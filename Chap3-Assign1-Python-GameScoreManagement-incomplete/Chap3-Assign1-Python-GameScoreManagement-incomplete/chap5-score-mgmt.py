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
        for entry in self._entries:
            if entry.get_name() == player_name:
                return entry.get_score()
        else:
            return -1
    
    def average_max_scores(self):
        sum = 0
        for entry in self._entries:
            sum += entry.get_score()
        return sum / self._max_entries

    def find_min_max_scores(self):
        scores = set()
        for entry in self._entries():
            scores.add(entry.get_score())
        min_score, max_score = min(scores), max(scores)
        return min_score, max_score


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
