# Unit Testing

# Saat Anda membangun aplikasi menggunakan Python dan aplikasi yang dikembangkan semakin kompleks, dependensi akan muncul. Artinya, satu atau lebih fungsi digunakan oleh fungsi lain. Bahkan, ketika kita mulai membangun aplikasi dengan rekan kita, kita membuat fungsi yang digunakan oleh rekan, ataupun sebaliknya.

# Pada saat membuat fungsi baru ataupun mengubah fungsi yang sudah ada, tentunya perlu dipastikan bahwa fungsionalitas aplikasi yang sebelumnya tidak terganggu dengan adanya perubahan baru tersebut. Bagaimana jika fungsionalitas bukan hanya lima atau sepuluh, tetapi lebih dari itu? Tentu menyulitkan sekali untuk mengeceknya satu per satu setiap kita melakukan perubahan.

# Di sinilah kita butuh pengujian (test) untuk fungsi-fungsi tersebut. Pengujian sebenarnya dapat dibedakan menjadi dua tipe, yaitu manual dan otomatis.

# 1. Manual testing adalah proses pengujian yang dilakukan oleh seseorang yang ditunjuk sebagai tester atau bahkan developer lainnya.
# 2. Testing otomatis merupakan hal yang sebaliknya. Ini adalah pengujian yang dilakukan secara otomatis terhadap kode-kode yang kita bangun berdasarkan rencana pengujian (test plan).

# Penerapan Testing
import unittest


class TestString(unittest.TestCase):
    def test_string(self):
        self.assertEqual("www.dicoding.com".strip("c.mow"), "dicoding")

    def test_isalnum(self):
        self.assertTrue("C0d1ng".isalnum())
        self.assertFalse("C0d!ng".isalnum())

    def test_index(self):
        s = "dicoding"
        self.assertEqual(s.index("coding"), 2)
        # Check s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index("decode")

if __name__ == "main":
    unittest.main()