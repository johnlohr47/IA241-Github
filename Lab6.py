'''
lab6
for loop, range functions
'''

#3.1
for i in range(6):
    if i !=3:
        print(i)
        
#3.2
result = 1
for i in range(1,6):
    result = result * i
    
print(result)

#3.3
result = 0
for i in range(1,6):
    result = result + i

print(result)

#3.4
result = 1
for i in range(3,9):
    result = result * i

print(result)

#3.5
result1 = 1
for i in range(8,0,-1):
    result1 = result1 * i

result2 = 1
for i in range(3,0,-1):
    result2 = result2 * i
answer= result1/result2

print(answer)

#3.6
result = 0
for word in 'this is my 6th string'.split():
    result = result +1
    
print(result)

#3.7
result = 0 
my_tweet = { "favorite_count":1138, "lang": "en", "coordinates": (-75, 40), "entities": {"hashtags": ["Preds", "Pens", "SingIntoSpring"]} } 
for entities in my_tweet['entities']['hashtags']:
    result = result + 1
print(result)