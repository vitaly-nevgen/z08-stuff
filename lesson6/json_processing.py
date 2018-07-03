import json

f = open('quiz_json.json')
quiz = json.load(f)
print("Before file changes: ", quiz)

feed = {"results": {"sport": {"q1": {"result1": True, "result2": False, "result3": True}},
        "math": {"q1": {"result1": False}, "q2": {"result1": False}}}}

quiz.update(feed)

with open('quiz_json.json', 'w') as file:
    json.dump(quiz, file, indent=4)

print("After file changes: ", quiz)