import unittest
import testaus.fileread.fileread as fileread

# Test that returns "File not found" if file is not found
class TestFileNotFound(unittest.TestCase):
    def test_file_not_found(self):
        file_name = "file_not_found.txt"
        expected_result = "File not found"
        line_number = 2
        result = fileread.file_read(file_name, line_number)
        self.assertEqual(result, expected_result)


# Test that returns "Empty file" if file is empty
class TestEmptyFile(unittest.TestCase):
    def test_empty_file(self):
        file_name = "empty_file.txt"
        expected_result = "Empty file"
        line_number = 2
        result = fileread.file_read(file_name, line_number)
        self.assertEqual(result, expected_result)


# Test that returns "IndexError" if line number is out of range
class TestIndexError(unittest.TestCase):
    def test_index_error(self):
        file_name = "test_file.txt"
        line_number = 100
        expected_result = "IndexError"
        result = fileread.file_read(file_name, line_number)
        self.assertEqual(result, expected_result)


# Test that returns the line as a string
class TestFileRead(unittest.TestCase):
    def test_file_read(self):
        file_name = "test_file.txt"
        line_number = 2
        expected_result = "This is line 2\n"
        result = fileread.file_read(file_name, line_number)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
