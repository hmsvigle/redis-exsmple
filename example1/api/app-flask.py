
import redis
from flask import Flask, request, jsonify

app = Flask(__name__)

try:
    r = redis.Redis(host='redisdb', port=6379, db=0)
    print ('-----  Establishing connection to redis db  ----')
    print ('Ping to redis sb:' , r.ping())
    print ('Status : Connected!')
    #return r.ping()
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')

def close():
    return r.close()

@app.route('/add_word/word=<word>')   
def add_word(word):
        if request.method == 'GET' :
            w_list = 'Dictionary'         
            r.rpush(w_list,word)
            length = r.llen(w_list)
            out = r.lrange(w_list, 0, length)
            print ('----- Printing complete dictionary ----')
            #print(out)
            return 'Word %s has been added to dictionary.' % word
        else:
            #print ('Page not found')
            return 'Page not found'
#        return 'the word %s added to dictionary' % word

@app.route('/autocomplete/query=<prefix>')   
def autocomplete_query(prefix):
         #print ('----- Executing autocomplete query ----')
         word_list = r.lrange('Dictionary' , 0, -1) 
         matches = []
         prefix = prefix.encode()
         for word in word_list: 
             if word.lower().startswith(prefix): 
                 matches.append(word) 
         return jsonify(decode(matches))

def decode(l):
    if isinstance(l, list):
        return [decode(x) for x in l]
    else:
        return l.decode('utf-8')
         

if __name__ == "__main__":
    app.run('localhost',5000)


