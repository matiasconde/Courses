## 3. Function Closures ##

def add(a, b):
    return a + b

def partial(function, *args):
    parent_args = args
    def inner(*inner_args):
        return function(*(parent_args+inner_args))
    return inner

add_two = partial(add,2)

print(add_two(7))
    

## 4. Python Decorators ##


def catch_error(function):
    def inner(*args):
        try:
            return function(*args)
        except Exception as e:
            return e
    return inner

@catch_error
def throws_error():
    raise Exception('Throws Error')
    
print(throws_error())        
        

## 5. Method Decorators ##

class Pipeline:
    def __init__(self):
        self.tasks = []
    
    def task(self):
        def inner(f):
            self.tasks.append(f)
            return f
        return inner
        
pipeline = Pipeline()

@pipeline.task()
def first_task(x):
    return x + 1

print(pipeline.tasks)

    
        

## 6. Decorator Arguments ##

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
                idx = self.tasks.index(depends_on)+1
        def inner(f):
            self.tasks.insert(idx,f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1
@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2
@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.tasks)

## 7. Running the Pipeline ##

def compose(*fs):
    return reduce(compose2, fs)

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner

    def run(self,input_):
        output = input_
        for task in self.tasks:
            output = task(output)
        return output
            
pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.run(20))

## 8. Challenge: Making Static Tasks Dynamic ##

import io

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner
    
    def run(self,input_):       
        output = input_
        for task in self.tasks:
            output = task(output)
        return output

"""
def parse_log(log):
    for line in log:
        split_line = line.split()
        remote_addr = split_line[0]
        time_local = parse_time(split_line[3] + " " + split_line[4])
        request_type = strip_quotes(split_line[5])
        request_path = split_line[6]
        status = split_line[8]
        body_bytes_sent = split_line[9]
        http_referrer = strip_quotes(split_line[10])
        http_user_agent = strip_quotes(" ".join(split_line[11:]))
        yield (
            remote_addr, time_local, request_type, request_path,
            status, body_bytes_sent, http_referrer, http_user_agent
        )

def build_csv(lines, header=None, file=None):
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.seek(0)
    return file

def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index('request_type')

    uniques = {}
    for line in reader:

        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return ((k, v) for k,v in uniques.items())
    
    
 # NOW RUN ALL OF That
        
log = open('example_log.txt')
parsed = parse_log(log)
csv_file = build_csv(
    parsed,
    header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
    ],
    # Using file-like object instead of `temporary.csv`.
    file=io.StringIO()
 )
uniques = count_unique_request(csv_file)
summarized_csv = build_csv(
    uniques,
    header=['request_type', 'count'],
    # Using file-like object instead of `summarized.csv`.
    file=io.StringIO()
 )
print(summarized_csv.readlines())
    """

pipeline = Pipeline()

@pipeline.task()
def parse_logs(logs):
    return parse_log(logs)


@pipeline.task(depends_on=parse_logs)
def build_raw_csv(lines):
    return build_csv(lines, header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
    ],
    file=io.StringIO())

@pipeline.task(depends_on=build_raw_csv)
def count_uniques(csv_file):
    return count_unique_request(csv_file)

@pipeline.task(depends_on=count_uniques)
def summarize_csv(lines):
    return build_csv(lines, header=['request_type', 'count'], file=io.StringIO())

log = open('example_log.txt')
summarized_file = pipeline.run(log)
print(summarized_file.readlines())