from LinkedList.linkedlist import LinkedList


class HashTable(object):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_val = self.hash(key, len(self.slots))

        if not self.slots[hash_val]:
            self.slots[hash_val] = key
            self.data[hash_val] = value
        elif self.slots[hash_val] == key:
            self.data[hash_val] = value
        else:
            next_slot = self.rehash(hash_val, len(self.slots))
            while self.slots[next_slot] and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if not self.slots[next_slot]:
                self.slots[next_slot] = key
                self.data[next_slot] = value
            else:
                self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))

        position = start_slot
        found = False
        stop = False
        data = None

        while self.slots[position] and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == start_slot:
                    stop = True
        return data

    def hash(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 3) % size

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


class HashTableUsingLL(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.linked_list = LinkedList()

    def _put(self, key, value):
        _hash = self._hash(key)

        if self.slots[_hash] is not None:
            head = self.slots[_hash]

        else:
            head = self.linked_list.head

        self.slots[_hash] = self.linked_list.insert(head, "%s || %s || %s" % (key, _hash, value))

    def _get(self, key):
        _hash = self._hash(key)

        if self.slots[_hash] is None:
            raise Exception('No key is present')

        head = self.slots[_hash]
        value = self.linked_list.contains(head, "%s || %s" % (key, _hash))

        if not value:
            raise Exception('Error in retrieval')

        return value.split('||')[2].strip()

    def _hash(self, key):
        return key % self.size

    def __setitem__(self, key, value):
        self._put(key, value)

    def __getitem__(self, key):
        return self._get(key)