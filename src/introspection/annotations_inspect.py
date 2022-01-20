# this is an example function with annotations
def num_vowels(text: str) -> int:
    return sum(1 if c.lower() in 'aeiouy' else 0 for c in text)

# examples of introspection this function
import inspect
sig = inspect.signature(num_vowels)

print(sig.parameters['text'])
print(sig.parameters['text'].annotation)
print(sig)
print(sig.return_annotation)
print(num_vowels.__annotations__)
