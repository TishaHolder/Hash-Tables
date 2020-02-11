# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table

        #storage list with size = capacity and each element initialized to None
        #this is where we will store all of the data
        self.storage = [None] * capacity 

    #A hashing function takes a key and returns an index into the underlying array.
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        
        #use python's build in hash method
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    """
    Hashing functions return a wide range of integers. In order to transform these values into useful 
    indices for our array we need a compression function. A compression function uses modular arithmetic 
    to calculate an array index for a hash map when given a hash code.
    """
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        #modulize the hash by the size of the linked list
        return self._hash(key) % self.capacity

    """
    Save the value to the map’s array at the index determined by plugging 
    the key into the _hash() method and plugging the hash code into the _hash_mod() method.
    """
    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        #plug the key into _hash_mod to generate an index to insert the value
        list_index = self._hash_mod(key)

        # Our first step in implementing a collision strategy.
        # After finding the list_index, we want to do a check of the content that’s currently at 
        # self.storage[list_index].
        # In order to avoid overwriting the wrong key, check the existing value in the list at 
        # self.storage[list_index]. Save this into current_node.
        current_node = self.storage[list_index]

        #if there are no contents or current_node is equal to none, 
        # we want to store the key and the value instead of just the key. 
        # Instead of just saving value, save (key, value) to the list.
        if current_node is None:
            self.storage[list_index] = LinkedPair(key, value)
            return

        #If current_node_value already has contents, check if the saved key is different from the key 
        # we are currently processing. If the keys are the same, overwrite the list value.
        if current_node.key == key:
            self.storage[list_index] = LinkedPair(key, value)
            return        

        # If the keys are different or (current_node) holds a different key, 
        # we’re going to implement linked list chaining        
        while True:
                #if the current node in the "inner linked list" is None, add the key, value pair
                if current_node.next is None: 
                    current_node.next = LinkedPair(key, value)
                #if the current node key in the "inner linked list" is the same as the key we are
                #currently processing, overwrite the node value
                if current_node.key == key:
                    current_node.next = LinkedPair(key, value)
                    break
                current_node = current_node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass

    """
    calculate the array index in the same way insert does and then retrieve and return the value 
    at that index.
    """
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #plug the key into _hash_mod to generate an index to retrieve the value from
        list_index = self._hash_mod(self._hash(key))

        #after finding the list index, we want to check to make sure that the index corresponds to the key 
        # we’re looking for. Save the list value at our compressed hash code into possible_return_node.
        possible_return_node = self.storage[list_index]

        #Instead of just returning the array’s contents at that index, check if possible_return_value is None. 
        #If so, return None.
        if possible_return_node is None:
            return None
        else:
        #If possible_return_node is not None, check if the first element in possible_return_node 
        # is the same as key. If so, return possible_return_node.value, the value.
            while True:
                if possible_return_node.key == key:
                    return possible_return_node.value
                possible_return_node = possible_return_node.next

        # possible_return_value holds different key
        print("ERROR")
        return



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
