
import redis



class Redis_DB:

     def __init__(self):
        try:
            self.r = redis.Redis(host='localhost', port=6379, db=0)
            print ('-----  Establishing connection to redis db  ----')
            print ('Ping to redis sb:' , self.r.ping())
            print ('Status : Connected!')
        except Exception as ex:
            print ('Error:', ex)
            exit('Failed to connect, terminating.')

     def close(self):
        return self.r.close()
   
     def add_word(self, word):
        
        w_list = 'Dictionary'         
        self.r.rpush(w_list,word)
        length = self.r.llen(w_list)
        out = self.r.lrange(w_list, 0, length)
        print ('----- Printing complete dictionary ----')
        print(out)

     def autocomplete_query(self, prefix):
         print ('----- Executing autocomplete query ----')
         word_list = self.r.lrange('Dictionary' , 0, -1) 
         matches = []
         prefix = prefix.encode()
         for word in word_list: 
             if word.lower().startswith(prefix): 
                 matches.append(word) 
         print ('possible range of words: ', matches)
         return matches 


def main():

    red = Redis_DB()
    
    # create dictionary of words    
    red.add_word('mmmm')
    
    # find autocomplete query
    red.autocomplete_query('a')

    #Cleanup Connection
    red.close()


if __name__ == "__main__":
    main()


