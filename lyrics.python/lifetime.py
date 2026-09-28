import sys
import time

print("\n"),
      
lyrics = [
    ("Oh, you were a good dream", 0.4),
    ("Smoke and ashes from these letters I'm burning", 4.4),
    ("No fairytale ending if there was no beginning", 9.2),
    ("Is it even worth it to reminisce?", 15.0),
    ("How do you grieve for a love that did not even exist?", 19.0),
    ("Was there a lifetime waiting for us?", 26.5),
    ("In a world where I was yours?", 30.5),
    ("Was it the wrong time, what if we tried?", 36.5),
    ("Giving in a little more?", 40.5),
    ("To the warmth we had before?", 44.0)
]

def type_out(text, char_delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print() 

def run_lyrics():
    print("--- Starting Lyrics ---\n")
    start_point = time.time()
    
    for i in range(len(lyrics)):
        text, start_time = lyrics[i]
        
        
        while time.time() - start_point < start_time:
            time.sleep(0.01)
        
        
        type_out(text)

if __name__ == "__main__":
    run_lyrics()