"""
In computing, a hash table is a data structure that implements an associative array abstract data type, 
a structure that can map keys to values. A hash table uses a hash function to compute an index, also called 
a hash code, into an array of buckets or slots, from which the desired value can be found
"""

"""
A hash map with a linked list separate chaining strategy follows a similar flow to a regular hash map. 
The user wants to assign a value to a key in the map. The hash map takes the 
key and transforms it into a hash code. The hash code is then converted into an index to an array using the 
modulus operation. If the value of the array at the hash function’s returned index is empty, a new linked 
list is created with the value as the first element of the linked list. If a linked list already exists at 
the address, append the value to the linked list given.

"""

"""
Hash tables are efficient key-value stores. They are capable of assigning and retrieving data in the fastest way 
possible for a data structure. This is because the underlying data structure that they use is an array. 
A value is stored at an array index determined by plugging the key into a hash function.

****In Python we don’t have an array data structure that uses a contiguous block of memory. We are going 
to simulate an array by creating a list and keeping track of the size of the list with an additional 
integer variable. This will allow us to design something that resembles a hash table. 

"""

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

    #uses python's built in hash function to convert the given key into any integer
    #The underscore prefix is meant as a hint to another programmer that a variable or method starting with 
    # a single underscore is intended for internal use.
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
    indices for our list we need a compression function. A compression function uses modular arithmetic 
    to calculate an array index for a hash map when given a hash code.
    """
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        #modulize the hash by the size of the list
        #to get a number between 0 and the capacity of the list - 1
        return self._hash(key) % self.capacity

    """
    Save the value to the hash table’s list or array at the index determined by plugging 
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
        # self.storage[list_index]. Save this into current_list_value.
        current_list_value = self.storage[list_index]

        #if there are no contents or current_list_value is equal to none, 
        #If the value of the list at the hash function’s returned index is empty, a new 
        # linked list is created with the value as the first element of the linked list.
        if current_list_value is None:
            self.storage[list_index] = LinkedPair(key, value)
            return

        #If current_list_value already has contents, check if the saved key is different from the key 
        # we are currently processing. If the keys are the same, overwrite the list value.       
        if current_list_value.key == key:
            self.storage[list_index] = LinkedPair(key, value)            
            return     
                
        #If a linked list already exists at the address, append the value to the linked list.
        #also known as linked list chaining 

        #set the current_list_value to current_node while traversing the inner linked list
        #for readability sake
        current_node = current_list_value

        while current_node:
                #if the current node key in the "inner linked list" is the same as the key we are
                #currently processing, overwrite the node value
                if current_node.key == key:
                    current_node = LinkedPair(key, value)
                    break
                #if the next node in the "inner linked list" is None, append the value to the linked list
                #and set the next pointer of the current node to the new node (LinkedPair)
                if current_node.next is None: 
                    current_node.next = LinkedPair(key, value)
                #update the current_node pointer to the next node
                current_node = current_node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        #plug the key into _hash_mod to generate an index to insert the value
        list_index = self._hash_mod(key)

        # After finding the list_index, we want to retrieve the content that’s currently at 
        # self.storage[list_index].        
        current_list_value = self.storage[list_index]

        #If the value of the list at the hash function’s returned index is empty, return None
        if current_list_value is None:            
            return None

        #If the key at the hash function’s returned index matches the provided key
        if current_list_value.key == key:
            #place the value to be removed in a temp variable before the pointers are removed
            removed = current_list_value
            #removes current_list_value's pointer to the next node before it is removed
            self.storage[list_index] = current_list_value.next
            #return the value for the given key
            return removed.value
            
        
        #if the current_list_value is not None or doesn't match the key
        #set the current_list_value.next to current_node while traversing the inner linked list
        #for readability sake        
        current_node = current_list_value.next
        
        while current_node is not None:
            #if the current_node matches the key
            if current_node.key == key:
                #place the value to be removed in a temp variable before the pointers are removed
                removed = current_node
                #removes current_list_value next pointer to current_node.next before it is removed
                current_list_value.next = current_node.next
                #return the value of the removed node
                return removed.value                  
            
            #set the current_list_value to point to the current_node
            current_list_value = current_node

            #set the current_node to the next node in the inner list      
            current_node = current_node.next

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
        # we’re looking for. Save the list value at our compressed hash code into current_list_value.
        current_list_value = self.storage[list_index]

        #Instead of just returning the array’s contents at that index, check if possible_return_value is None. 
        #If so, return None.
        if current_list_value is None:
            return None
        else:
       
            #if the current_list_value is not None or doesn't match the key
            #set the current_list_value.next to current_node while traversing the inner linked list
            #for readability sake        
            current_node = current_list_value
            
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next      

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2

        self.storage = [None] * self.capacity

        for item in old_storage:         

            #change the name to node when traversing a singly linked list
            node = item

            while node is not None:
                self.insert(node.key, node.value)
                node = node.next   
               
            



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
