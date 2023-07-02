rules = {
    "ROOT": [["S"]],
    "S": [
        ["NP", "VP"],
        ["NP","VP","PP"]
    ],
    "NP": [
        ["det", "NP3"]
    ],
    "NP3": [
        ["adj", "NP3"],
        ["noun"],
        ["noun", "PP"]
    ],
    "VP": [
        ["verb"]
    ],
    "PP": [
        ["prepos", "NP2"]
    ],
    "NP2":[
        ["det","NP3"]
    ],
    "det": {"that", "this", "a", "the", "those", "my", "your", "his", "her"," its", "our", " their"},
    "adj":{"young", "old", "new", "big", "small"},
    "noun": {"man", "women", "money", "house", "table", "stars", "ears", "world", "india", "me", "student", "class", "i" ,"he", "she", "it", "chair"},
    "verb": {"book", "include", "prefer", "saw", "hello","sat"},
    "aux": {"does"},
    "prepos": {"from", "to", "on", "near", "through", "with","in"}
}
f = open("anhviet.txt",mode = 'r', encoding='utf-8')
data = f.read()
if(data == '*'):
    if

f.close()