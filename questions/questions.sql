INSERT INTO general (question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty, topic_1, topic_2) VALUES
('What is the output of print(2 ** 3)?', '8', '6', '9', '5', 1, 1, NULL),
('Which of the following is a valid variable name in Python?', 'my_variable', '2variable', 'my-variable', 'class', 1, 1, NULL),
('What function is used to get input from the user in Python?', 'input()', 'get()', 'read()', 'scan()', 1, 1, NULL),
('Which keyword is used to define a function in Python?', 'def', 'func', 'define', 'method', 1, 1, NULL),
('What will print(len("Python")) output?', '6', '5', '7', 'Error', 1, 1, NULL),

('What is the result of 10 // 3 in Python?', '3', '3.33', '4', 'Error', 2, 1, NULL),
('Which of these data types is immutable in Python?', 'tuple', 'list', 'dictionary', 'set', 2, 1, NULL),
('How do you open a file in write mode?', 'open("file.txt", "w")', 'open("file.txt", "r")', 'open("file.txt", "a")', 'open("file.txt", "wb")', 2, 1, NULL),
('What does the "continue" statement do in a loop?', 'Skips the current iteration', 'Exits the loop', 'Pauses execution', 'Restarts the loop', 2, 1, NULL),
('Which module is used for working with JSON data in Python?', 'json', 'pickle', 'os', 'csv', 2, 1, NULL),

('What is the output of bool([])?', 'False', 'True', 'None', 'Error', 3, 1, NULL),
('Which method is used to remove an item from a dictionary?', 'pop()', 'remove()', 'delete()', 'discard()', 3, 1, NULL),
('What is the time complexity of searching for an element in a set?', 'O(1)', 'O(n)', 'O(log n)', 'O(n^2)', 3, 1, NULL),
('How do you sort a list in descending order?', 'sorted(my_list, reverse=True)', 'my_list.sort(descending=True)', 'my_list.sorted(reverse=True)', 'sort(my_list, desc=True)', 3, 1, NULL),
('Which function is used to get the memory address of an object?', 'id()', 'address()', 'memory()', 'ptr()', 3, 1, NULL),

('What will be the output of print({1, 2, 3} & {2, 3, 4})?', '{2, 3}', '{1, 2, 3, 4}', '{1, 4}', 'Error', 5, 1, NULL),
('Which of the following is a correct way to create a NumPy array?', 'np.array([1, 2, 3])', 'numpy.list([1, 2, 3])', 'array.numpy([1, 2, 3])', 'numpy.create([1, 2, 3])', 5, 1, NULL),
('What does the zip() function return?', 'An iterator of tuples', 'A list of tuples', 'A dictionary', 'A set', 5, 1, NULL),
('Which of these functions can be used to check if an object is an instance of a class?', 'isinstance()', 'issubclass()', 'type()', 'checkclass()', 5, 1, NULL),
('How can you measure the execution time of a Python script?', 'Using time.time() or timeit', 'Using sys.clock()', 'Using datetime.now()', 'Using timer()', 5, 1, NULL),

('What is the result of print(sorted([3, 1, 4], key=lambda x: -x))?', '[4, 3, 1]', '[1, 3, 4]', '[3, 1, 4]', 'Error', 5, 1, NULL),
('How do you create a dictionary comprehension?', '{k: v for k, v in iterable}', '[k: v for k, v in iterable]', '{(k, v) for k, v in iterable}', 'dict(k: v for k, v in iterable)', 5, 1, NULL),
('Which method in Pandas is used to drop missing values?', 'dropna()', 'remove()', 'delete()', 'clean()', 5, 1, NULL),
('How do you perform element-wise multiplication on two NumPy arrays?', 'array1 * array2', 'array1.dot(array2)', 'multiply(array1, array2)', 'elementwise(array1, array2)', 5, 1, NULL),
('Which of these decorators is used to define a static method?', '@staticmethod', '@classmethod', '@property', '@abstractmethod', 5, 1, NULL);

INSERT INTO general (question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty, topic_1, topic_2) VALUES
-- Difficulty 1 (Beginner)
('What is the correct way to start a comment in Python?', '# This is a comment', '// This is a comment', '/* This is a comment */', '-- This is a comment', 1, 1, NULL),
('Which function is used to find the length of a string?', 'len()', 'length()', 'size()', 'count()', 1, 1, NULL),
('What will print(type(42)) output?', '<class ''int''>', '<class ''float''>', '<class ''str''>', '<class ''bool''>', 1, 1, NULL),
('Which keyword is used to create a loop that executes while a condition is true?', 'while', 'for', 'loop', 'repeat', 1, 1, NULL),
('What is the output of print(3 * "Hello")?', 'HelloHelloHello', 'Hello3', '3Hello', 'Error', 1, 1, NULL),
('Which of the following is not a valid Python data type?', 'character', 'integer', 'boolean', 'string', 1, 1, NULL),
('What is the default return value of a function that does not return anything?', 'None', '0', 'False', 'Empty string', 1, 1, NULL),
('Which operator is used to check equality in Python?', '==', '=', '!=', '===', 1, 1, NULL),
('Which function converts a string to an integer?', 'int()', 'str()', 'float()', 'bool()', 1, 1, NULL),
('What will be the output of print(10 % 3)?', '1', '3', '0', '10', 1, 1, NULL),

-- Difficulty 2 (Easy)
('What will be the output of print(bool([]))?', 'False', 'True', 'None', 'Error', 2, 1, NULL),
('How do you check the data type of a variable?', 'type(variable)', 'datatype(variable)', 'checktype(variable)', 'typeof(variable)', 2, 1, NULL),
('Which method is used to remove the last item from a list?', 'pop()', 'remove()', 'del()', 'discard()', 2, 1, NULL),
('How do you write an infinite loop in Python?', 'while True:', 'for i in range():', 'loop:', 'while 1==2:', 2, 1, NULL),
('Which built-in function returns the absolute value of a number?', 'abs()', 'round()', 'floor()', 'ceil()', 2, 1, NULL),
('How do you combine two lists in Python?', 'list1 + list2', 'combine(list1, list2)', 'merge(list1, list2)', 'list1.append(list2)', 2, 1, NULL),
('What is the output of print("python".capitalize())?', 'Python', 'PYTHON', 'python', 'P', 2, 1, NULL),
('Which symbol is used for single-line comments in Python?', '#', '//', '--', '/* */', 2, 1, NULL),
('How do you remove leading and trailing spaces from a string?', 'strip()', 'trim()', 'cut()', 'remove()', 2, 1, NULL),
('What does the enumerate() function do?', 'Adds an index to an iterable', 'Sorts a list', 'Converts a string to a list', 'Reverses a list', 2, 1, NULL),

-- Difficulty 3 (Intermediate)
('What is the time complexity of appending an element to a list in Python?', 'O(1)', 'O(n)', 'O(log n)', 'O(n^2)', 3, 1, NULL),
('Which of the following is not a Python keyword?', 'switch', 'yield', 'with', 'pass', 3, 1, NULL),
('What does the zip() function do?', 'Combines multiple iterables into tuples', 'Compresses a file', 'Joins strings', 'Sorts a list', 3, 1, NULL),
('Which of the following data structures allows duplicate values?', 'list', 'set', 'dictionary', 'tuple', 3, 1, NULL),
('Which method is used to check if a key exists in a dictionary?', 'in', 'exists()', 'contains()', 'has_key()', 3, 1, NULL),
('What will be the output of print({1, 2, 3} | {3, 4, 5})?', '{1, 2, 3, 4, 5}', '{3}', '{1, 2, 5}', 'Error', 3, 1, NULL),
('Which function is used to iterate over both index and value in a list?', 'enumerate()', 'range()', 'zip()', 'map()', 3, 1, NULL),
('What is the output of print("10".zfill(4))?', '0010', '0100', '1000', 'Error', 3, 1, NULL),
('Which operator is used for unpacking in Python?', '*', '&', '@', '$', 3, 1, NULL),
('What is the default value of the end parameter in print()?', 'newline (''\\n'')', 'space (" ")', 'dot (".")', 'None', 3, 1, NULL),

-- Difficulty 5 (Advanced)
('What is the output of print(sorted({3: "a", 1: "b", 2: "c"}))?', '[1, 2, 3]', '["a", "b", "c"]', '[3, 1, 2]', 'Error', 5, 1, NULL),
('What does the __slots__ attribute do in a class?', 'Limits the attributes that an instance can have', 'Deletes unused attributes', 'Defines private variables', 'Enforces data types', 5, 1, NULL),
('What does the "@" symbol do in Python?', 'Defines a decorator', 'Performs matrix multiplication', 'Creates a pointer', 'Declares a lambda function', 5, 1, NULL),
('Which of the following is true for Python’s Global Interpreter Lock (GIL)?', 'It allows only one thread to execute at a time', 'It improves multithreading performance', 'It applies to multiprocessing', 'It is present in all Python implementations', 5, 1, NULL),
('How does Python handle integer overflow?', 'Automatically converts to long integers', 'Throws an OverflowError', 'Wraps around like C', 'Converts to float', 5, 1, NULL),
('Which of the following is used to define an abstract method?', '@abstractmethod', '@classmethod', '@staticmethod', '@final', 5, 1, NULL),
('What is the output of print({1, 2, 3} & {2, 3, 4})?', '{2, 3}', '{1, 2, 3, 4}', '{1, 4}', 'Error', 5, 1, NULL),
('Which method in Pandas is used to fill missing values?', 'fillna()', 'replace()', 'impute()', 'fill()', 5, 1, NULL),
('Which library is used for working with regular expressions in Python?', 're', 'regex', 'regexp', 'string', 5, 1, NULL),
('What is the difference between deep copy and shallow copy?', 'Deep copy creates independent copies', 'Shallow copy copies references only', 'Shallow copy duplicates objects completely', 'They are the same', 5, 1, NULL);
