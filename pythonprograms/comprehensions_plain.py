

print("LIST COMPREHENSION EXAMPLES")
print("=" * 80)

# 1) Squares of 1..10
squares = [n*n for n in range(1, 11)]
print("Squares 1..10:", squares)

# 2) Even numbers up to 20
evens = [n for n in range(21) if n % 2 == 0]
print("Evens up to 20:", evens)

# 3) Trim and lowercase words
raw = ["  Python  ", " DATA  ", "   science"]
cleaned = [w.strip().lower() for w in raw]
print(" Cleaned words:", cleaned)

# 4) Flatten 2D list
grid = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [x for row in grid for x in row]
print("4) Flattened:", flat)

# 5) Cartesian product pairs where i < j
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
print("Pairs i<j (0..3):", pairs)


print("\n" + "=" * 80)
print("TUPLE 'COMPREHENSION' EXAMPLES (5) -> using tuple(...) over a generator")
print("=" * 80)
# Note: Python has generator expressions in parentheses; wrap with tuple(...) to create a tuple.

# 1) Cubes of 1..10
cubes = tuple(n**3 for n in range(1, 11))
print("1) Cubes 1..10:", cubes)

# 2) First letters of words
words = ["alpha", "beta", "gamma", "delta"]
initials = tuple(w[0] for w in words)
print("First letters:", initials)

# 3) Rounded values from floats
nums = [3.1415, 2.7182, 1.6180]
rounded = tuple(round(x, 2) for x in nums)
print("Rounded:", rounded)

# 4) Unique sorted vowels from text
text = "Comprehensions are concise and powerful!"
vowels = set(ch.lower() for ch in text if ch.lower() in "aeiou")
vowel_tuple = tuple(sorted(vowels))
print("4) Unique vowels:", vowel_tuple)



print("DICTIONARY COMPREHENSION EXAMPLES (5)")
print("=" * 80)

# 1) Number -> square mapping (1..5)
squares_map = {n: n*n for n in range(1, 6)}
print("1) n->n^2:", squares_map)

# 2) Word -> length (skip empty after strip)
words2 = [" data", "ai ", "  ", "python", "ml"]
lengths = {w.strip(): len(w.strip()) for w in words2 if w.strip()}
print("word->len:", lengths)

# 3) Invert a mapping (values become keys) when values are unique
country_to_code = {"India": "IN", "United States": "US", "Japan": "JP"}
code_to_country = {v: k for k, v in country_to_code.items()}
print("Inverted mapping:", code_to_country)

# 4) Count character frequency (only alphabetic, case-insensitive)
text2 = "Better Code, Faster Learning!"
freq = {ch: text2.lower().count(ch) for ch in set(text2.lower()) if ch.isalpha()}
print("Char frequency:", freq)

# 5) Merge two lists into a dict with condition
keys = ["k1", "k2", "k3", "k4"]
values = [10, None, 30, 0]
merged = {k: v for k, v in zip(keys, values) if v}
print("Merged (skip falsy values):", merged)
