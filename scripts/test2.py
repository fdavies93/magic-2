def test_3():
    pass

def on_mount(**kwargs):
    print("Mounted from test2 successfully.")

__register__ = [test_3, on_mount]