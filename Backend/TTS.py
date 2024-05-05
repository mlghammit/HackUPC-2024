import networkx as nx
from gtts import gTTS
import pygame

def initialize_graph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=1) #Node start to stop
    G.add_edge('B', 'C', weight=2) 
    G.add_edge('B', 'D', weight=4)
    G.add_edge('C', 'D', weight=1)
    G.add_edge('C', 'E', weight=3)
    G.add_edge('D', 'E', weight=1)
    return G

def find_path(graph, start, end):
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    return path

def generate_voice_command(direction):
    tts = gTTS(text=direction, lang='en')
    tts.save("direction.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("direction.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # wait for the audio to finish playing
        pygame.time.Clock().tick(10)

def main():
    G = initialize_graph()
    start = 'A' # Node start
    end = 'E' # Node stop
    path = find_path(G, start, end)

    # Generate directions based on the path
    for i in range(len(path) - 1):
        direction = f"Go from {path[i]} to {path[i+1]}"
        print(direction)  # Optionally print the direction
        generate_voice_command(direction)

if __name__ == "__main__":
    main()
