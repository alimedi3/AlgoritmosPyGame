import pygame

class Node:
    def __init__(self, pos, id, color, rect=None):
        self.pos = pos
        self.id = id
        self.color = color
        self.rect = rect
    
    def update_rect(self, rect):
        self.rect = rect
    
    def within(self, pos):
        if pos[0] >= self.rect[0] and pos[0] <= self.rect[0]+self.rect[2] and pos[1] >= self.rect[1] and pos[1] <= self.rect[1]+self.rect[3]:
            return True
        else:
            return False

class Edge:
    def __init__(self, node_id1, node_id2, color, start_pos, end_pos, rect=None):
        self.nodeid1 = node_id1
        self.nodeid2 = node_id2
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.rect = rect
    
    def update_rect(self, rect):
        self.rect = rect

    def within(self, pos):
        if pos[0] >= self.rect[0] and pos[0] <= self.rect[0]+self.rect[2] and pos[1] >= self.rect[1] and pos[1] <= self.rect[1]+self.rect[3]:
            return True
        else:
            return False
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1080, 600
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._running = True
        self._nodeing = False
        self._red = (255,0,0)
        self._purple = (255,0,255)
        self._node_radius = 10
        self._edgeing = False
        self._edgeid1 = None
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 1073742050:
                self._nodeing = True
        if event.type == pygame.KEYUP:
            if event.key == 1073742050:
                self._nodeing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self._nodeing == True:
                nodes.append(Node(event.pos,len(nodes),self._red))
            elif event.button == 1 and self._nodeing == False and self._edgeing == False:
                for node in nodes:
                    if node.within(event.pos) == True:
                        self._edgeid1 = node.id
                        self._edgeing = True
            elif event.button == 1 and self._nodeing == False and self._edgeing == True:
                for node in nodes:
                    if node.within(event.pos) == True:
                        self._edgeing = False
                        edges.append(Edge(self._edgeid1,node.id,self._purple,nodes[self._edgeid1].pos,node.pos))
                        

    def on_loop(self):
        for edge in edges:
            rect = pygame.draw.line(self._display_surf,edge.color,edge.start_pos,edge.end_pos)
            edge.update_rect(rect)
        for node in nodes:
            rect = pygame.draw.circle(self._display_surf,node.color,node.pos,self._node_radius)
            node.update_rect(rect)

    def on_render(self):
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    nodes = []
    edges = []
    theApp.on_execute()