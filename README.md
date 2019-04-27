# TCGen

Test cases generator generator tool. The first sentence has no typo.
Given a set of strings tries to find a pattern and create a code that produce random sample for such pattern.
It is highly focused for test cases in competitive programming problems but can be used/extended beyond this scope.


## Roadmap

+ Make Python package (Installation and usage guide)
+ CLI
    Read from standard input one json file
    Read json from file
    Read folder containing .in

    Output to stdout (or to folder with -o)

+ Benchmark on codeforces.
+ Auto detect used separators.
+ Read description of the problem to find extra constraints on the input.