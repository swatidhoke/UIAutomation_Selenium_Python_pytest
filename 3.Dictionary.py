 
#Python Dictnary :
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
  
  
