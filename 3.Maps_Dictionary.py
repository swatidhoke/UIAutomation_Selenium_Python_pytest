

# Top 10 Most Used Built-in Dictionary Functions in Python:

# 1. dict.keys() - Returns a view object displaying a list of all the keys in the dictionary.
#    Example: {'a': 1, 'b': 2}.keys() returns dict_keys(['a', 'b']).
#
# 2. dict.values() - Returns a view object displaying a list of all the values in the dictionary.
#    Example: {'a': 1, 'b': 2}.values() returns dict_values([1, 2]).
#
# 3. dict.items() - Returns a view object displaying a list of dictionary's key-value tuple pairs.
#    Example: {'a': 1, 'b': 2}.items() returns dict_items([('a', 1), ('b', 2)]).
#
# 4. dict.get(key, default=None) - Returns the value for the specified key if the key is in the dictionary.
#    If the key is not found, returns the default value.
#    Example: {'a': 1}.get('b', 0) returns 0.
#
# 5. dict.update(other_dict) - Updates the dictionary with the key-value pairs from another dictionary or
#    from an iterable of key-value pairs.
#    Example: {'a': 1}.update({'b': 2}) results in {'a': 1, 'b': 2}.
#
# 6. dict.pop(key, default=None) - Removes the specified key and returns its value. If the key is not found,
#    returns the default value (or raises a KeyError if default is not provided).
#    Example: {'a': 1, 'b': 2}.pop('a') returns 1 and results in {'b': 2}.
#
# 7. dict.popitem() - Removes and returns a (key, value) pair as a tuple. Pairs are returned in LIFO
#    (last-in, first-out) order.
#    Example: {'a': 1, 'b': 2}.popitem() returns ('b', 2).
#
# 8. dict.clear() - Removes all items from the dictionary.
#    Example: {'a': 1, 'b': 2}.clear() results in {}.
#
# 9. dict.copy() - Returns a shallow copy of the dictionary.
#    Example: {'a': 1}.copy() returns {'a': 1}.
#
# 10. dict.setdefault(key, default=None) - Returns the value for the specified key. If the key does not exist,
#     inserts the key with the specified default value.
#     Example: {'a': 1}.setdefault('b', 2) returns 2 and results in {'a': 1, 'b': 2}.

#1-->Python Dictionary Programme to flatten a dictonary:
import collections;
def dict_basic(test_input):
    #Add items
    test_input["Key3"] ={1: "new1", 2: "new2"}
    #Update items
    test_input["Key3"] ={1: "updated_new1", 2: "new2"}
    for k, v in test_input.items():
        print(k, v )      
    #Delete items
    del  test_input["Key2"]   

    #Update dict
    test_input.update({"Key4" : {1: "updated_new1", 2: "updated_new2"}});
    
    #Print input dict
    print(test_input) 

# 2--> flatten a dict
import copy
def flatten_dictionary(dictionary):
  
  flattenedDict = {}
    
    def helper(curDict, keyName):
    
    for key in curDict.keys():
      if isinstance(curDict[key], str):
        
        if keyName == "":
          flattenedDict[key] = curDict[key]
        elif key == "":
          flattenedDict[keyName] = curDict[key]
        else:
          flattenedDict[keyName + "." + key] = curDict[key]
      else:
        
        if keyName == "":
          helper(curDict[key], key)
        elif key == "":
          helper(curDict[key], keyName)
        else:
          helper(curDict[key], keyName + "." + key)
  
  helper(dictionary, "")
  
  return flattenedDict

#3-->Count number of words in a line or a file
def count_biggest_repeated():
  counts ={}
  file ="my name is swati and my kids name is shorya my vikram his father"

  words= file.split()

  for word in words:
      counts[word] = counts.get(word,0)+1

  #find the item repeated the most
  bigcount = None
  bigword = None
  for word,count in counts.items():
      if bigcount is None or count > bigcount:
              bigword=word; bigcount=count;
  return(bigword, bigcount)

 ##### Test cases
test_dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
dict_basic(test_dict)
flatten_dictionarytest_dict()
  
  
