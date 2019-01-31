## 2. Intro to DAGs ##

cycle = [4,6,7]


## 3. The DAG Class ##

class DAG:
    def __init__(self):
        self.graph = {}
    
    def add(self, node, to=None):
        if node not in self.graph:
            if to:
                self.graph[node] = [to]
                if to not in self.graph:
                    self.graph[to] = []
            else: 
                self.graph[node] = []
        else: 
            if to: 
                self.graph[node].append(to)
                if to not in self.graph:
                    self.graph[to] = []
               

                
dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
print(dag.graph)


## 5. Finding Number of In Degrees ##

class DAG(BaseDAG):
    def in_degrees(self):
        pass

dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
in_degrees = dag.in_degrees()
class DAG(BaseDAG):
    def in_degrees(self):
        in_degrees = {}
        for node in self.graph:
            if node not in in_degrees:
                in_degrees[node] = 0
            for pointed in self.graph[node]:
                if pointed not in in_degrees:
                    in_degrees[pointed] = 0
                in_degrees[pointed] += 1
        return in_degrees

dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
in_degrees = dag.in_degrees()

## 6. Challenge: Sorting Dependencies ##

from collections import deque

class DAG(BaseDAG):
    def sort(self):
        in_degrees = self.in_degrees()
        searched = []
        to_visit = deque()
        
        for node in in_degrees:
            if in_degrees[node] == 0: 
                to_visit.append(node)
        
        while to_visit:
            node = to_visit.popleft()
            for pointed in self.graph[node]:
                in_degrees[pointed] -= 1
                if in_degrees[pointed] == 0: 
                    to_visit.append(pointed)
            searched.append(node)
        return searched
                   
          
dag = DAG()

dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(4,5)
dag.add(6, 7)

dependencies = dag.sort()
print(dependencies)

## 7. Enhance the Add Method ##

class DAG(BaseDAG):
    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)
        if len(self.sort()) != len(self.graph):
            raise Exception("new cycle created")

dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
#Add a pointer from 7 to 4, causing a cycle.
dag.add(7, 4)

## 8. Adding DAG to the Pipeline ##

class Pipeline:
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            pass
        return inner

pipeline = Pipeline()

def first():
    return 20

def second(x):
    return x * 2

def third(x):
    return x // 3

def fourth(x):
    return x // 4
class Pipeline:
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner

pipeline = Pipeline()
@pipeline.task()
def first():
    return 20

@pipeline.task(depends_on=first)
def second(x):
    return x * 2

@pipeline.task(depends_on=second)
def third(x):
    return x // 3

@pipeline.task(depends_on=second)
def fourth(x):
    return x // 4

print(pipeline.tasks.graph)

## 9. Challenge: Running the Pipeline ##

class Pipeline:
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner
    
    def run(self):
        completed = {}
        sorted_tasks = self.tasks.sort()
        for task in sorted_tasks:
            for node in self.tasks.graph:
                if task in self.tasks.graph[node]:
                    input_ = completed[node]
                    output = task(input_)
                    completed[task] = output
            if task not in completed:
                completed[task] = task()
         
        return completed
    
pipeline = Pipeline()

@pipeline.task()
def first():
    return 20

@pipeline.task(depends_on=first)
def second(x):
    return x * 2

@pipeline.task(depends_on=second)
def third(x):
    return x // 3

@pipeline.task(depends_on=second)
def fourth(x):
    return x // 4

outputs = pipeline.run()