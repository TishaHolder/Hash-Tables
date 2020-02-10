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
        self.storage = [None] * capacity #storage list with size = capacity and each element initialized to None

    #A hashing function takes a key and returns an index into the underlying array.
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        #Turn the key into a list of bytes by calling key.encode(). 
        #.encode() is a string method that converts a string into its corresponding bytes, 
        # a list-like object with the numerical representation of each character in the string.
        
        #key_bytes = key.encode()
        #key_bytes = hash(key)

        #Turn the bytes object into a hash code by calling sum() on key_bytes. Save the result 
        # from that into a variable called hash_code.
        #hash_code = sum(key_bytes)

        #return hash_code
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
        array_index = self._hash_mod(self._hash(key))

        # Our first step in implementing a collision strategy.
        # After finding the array_index, we want to do a check of the content that’s currently at 
        # self.storage[array_index].
        # In order to avoid overwriting the wrong key, check the existing value in the array at 
        # self.storage[array_index]. Save this into current_array_value.
        current_array_value = self.storage[array_index]

        #if there are no contents at current_array_value, we want to store the key and the value instead 
        # of just the key if current_array_value is equal to None. 
        # Instead of just saving value, save [key, value] to the array.
        if current_array_value is None:
            self.storage[array_index] = [key, value]
            return

        #If current_array_value already has contents, check if the saved key is different from the key 
        # we are currently processing. If the keys are the same, overwrite the array value.
        if current_array_value[0] == key:
            self.storage[array_index] = [key,value]
            return        

        # If the keys are different, we’re going to implement linked list chaining
        # current_array_value currently holds different key
        return


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
        array_index = self._hash_mod(self._hash(key))

        #after finding the array index, we want to check to make sure that the index corresponds to the key 
        # we’re looking for. Save the array value at our compressed hash code into possible_return_value.
        possible_return_value = self.storage[array_index]

        #Instead of just returning the array’s contents at that index, check if possible_return_value is None. 
        #If so, return None.
        if possible_return_value is None:
            return None
        else:
        #If possible_return_value is not None, check if the first element in possible_return_value (index 0) 
        # is the same as key. If so, return possible_return_value[1], the value.
            if possible_return_value[0] == key:
                return possible_return_value[1]

        # possible_return_value holds different key
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
