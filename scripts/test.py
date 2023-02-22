def test_1(**kwargs):
    print(kwargs["text"])

__register__ = {
    "hello": test_1,
}