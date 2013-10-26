"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "2 + 2", "answer": 4,
            "explanation": "2+2"},
        {
            "input": "2 * 2", "answer": 4,
            "explanation": "2*2"},
        {
            "input": "2 + 2 * 2", "answer": 8,
            "explanation": "2*(2+2)"},
        {
            "input": "1 - 2 - 3", "answer": 0,
            "explanation": "3-2-1"},
        {
            "input": "3 - 2 - 1", "answer": -4,
            "explanation": "1-2-3"},
        {
            "input": "4 / 8", "answer": 2,
            "explanation": "8/4"},
        {
            "input": "2 / 5", "answer": 2,
            "explanation": "5/2=floor(2.5)"},
        {
            "input": "0 / 10", "answer": 0,
            "explanation": "10*0"},
        {
            "input": "1+1*1+1", "answer": 4,
            "explanation": "(1+1)*(1+1)"},
        {
            "input": "(3*2)+(4*2)", "answer": 36,
            "explanation": "3*(2+4)*2"},
        {
            "input": "asd4 + 86() )+( a56d :)", "answer": 146,
            "explanation": "4+86+56"},
        {
            "input": "4 + 8 / 6 * 3 - 33", "answer": 15,
            "explanation": "(33-3)*6/(8+4)"},
        {
            "input": "3 - 3 / 10", "answer": 0,
            "explanation": "10/(3-3)=10*0"},
        {
            "input": "4 / 2 * 2 + ((3 - 3) / 15)", "answer": 3,
            "explanation": "((15/(3-3+2))*2)/4=floor(3.75)"},
        {
            "input": "((2 - 4) - (6 / 8)) + (4 * 6)", "answer": 0,
            "explanation": "6*(4+8)/(6-4-2)=72*0"},
        {
            "input": "0 / 0", "answer": 0,
            "explanation": "0*0"},

    ],
    "Extra": [
        {"input": "abcdefghe5", "answer": 5,
            "explanation": "5"},
        {"input": "289+123", "answer": 412,
            "explanation": "289+123"},
        {"input": "2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2", "answer": 1048576,
            "explanation": "2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2"},
        {"input": "[1, 2, 3,]", "answer": 123,
            "explanation": "123"},
        {"input": "[1, '+', '1']", "answer": 2,
            "explanation": "1+1"},
        {"input": "3 + 3", "answer": 6,
            "explanation": "3+3"},
        {"input": "33 - 66 - 99", "answer": 0,
            "explanation": "99-66-33"},
        {"input": "asdsdadsas2dsada+3dsadsa", "answer": 5,
            "explanation": "2+3"},
        {"input": "2/2/2/16", "answer": 2,
            "explanation": "((16/2)/2)/2"}
    ]
}
