import unittest


def connect_db():
    print("[Connect to DB]")

def refused_db(db):
    print(f"[Loses db connection: {db}]")

class User:
    username = ""
    active = False

    def __init__(self, db, name):
        self.username = name

    def set_active(self):
        self.active = True

class TestUser(unittest.TestCase):

    # Test case 1
    def test_user_not_active(self):
        db = connect_db()
        user = User(db, "Verdi")
        self.assertFalse(user.active) # default masih belum aktif
        refused_db(db)

    def test_user_active(self):
        db = connect_db()
        user = User(db, "Verdiansyah")
        user.set_active() # meaktifkan
        self.assertTrue(user.active)
        refused_db(db)


if __name__ == '__main__':
    unittest.main()
