import mc


generator = mc.StringGenerator(samples=["hello world", "world of cuties"])
result = generator.generate_phrase(
    attempts=25, validator=mc.validators.words_count(minimal=3, maximal=4)
)
print(result)
# e.g. >>> "hello world of cuties"
