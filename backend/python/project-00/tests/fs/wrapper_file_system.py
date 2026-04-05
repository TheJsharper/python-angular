import unittest
import os
import sys
import tempfile
import unittest.mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from fs.wrapper_file_system import WrapperFileSystem


class WrapperFileSystemTestCase(unittest.TestCase):
    def setUp(self):
        self.wrapper_file_system = WrapperFileSystem(open)
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_path = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_read_file(self):
        with open(self.temp_file_path, "w", encoding="utf-8") as file:
            file.write("Hello, World!")

        content = self.wrapper_file_system.read_file(self.temp_file_path)
        self.assertEqual(content, "Hello, World!")

    def test_write_file(self):
        self.wrapper_file_system.write_file(self.temp_file_path, "Written content")

        with open(self.temp_file_path, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "Written content")

    def test_write_file_overwrite(self):
        with open(self.temp_file_path, "w", encoding="utf-8") as file:
            file.write("Old content")

        self.wrapper_file_system.write_file(self.temp_file_path, "New content")

        with open(self.temp_file_path, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "New content")

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.wrapper_file_system.read_file("nonexistent_file.txt")

    @unittest.mock.patch("os.remove")
    def test_delete_file(self, mock_remove):
        self.wrapper_file_system.delete_file(self.temp_file_path)
        mock_remove.assert_called_once_with(self.temp_file_path)

    @unittest.mock.patch("os.remove")
    def test_delete_nonexistent_file(self, mock_remove):
        mock_remove.side_effect = FileNotFoundError("File not found.")
        with self.assertRaises(FileNotFoundError) as context:
            self.wrapper_file_system.delete_file("nonexistent_file.txt")
        self.assertEqual(str(context.exception), "File not found.")

    def test_delete_file_os_error(self):
        with open(self.temp_file_path, "w", encoding="utf-8") as file:
            file.write("Content to delete")

        with unittest.mock.patch("os.remove") as mock_remove:
            mock_remove.side_effect = OSError("Permission denied.")
            with self.assertRaises(OSError) as context:
                self.wrapper_file_system.delete_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Permission denied.")

    def test_write_file_io_error(self):
        with unittest.mock.patch("builtins.open", side_effect=IOError("Disk full.")):
            with self.assertRaises(IOError) as context:
                self.wrapper_file_system.write_file(self.temp_file_path, "Content")
            self.assertEqual(str(context.exception), "Disk full.")

    def test_read_file_io_error(self):
        with unittest.mock.patch("builtins.open", side_effect=IOError("Disk full.")):
            with self.assertRaises(IOError) as context:
                self.wrapper_file_system.read_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Disk full.")

    def test_write_file_permission_error(self):
        with unittest.mock.patch(
            "builtins.open", side_effect=PermissionError("Permission denied.")
        ):
            with self.assertRaises(PermissionError) as context:
                self.wrapper_file_system.write_file(self.temp_file_path, "Content")
            self.assertEqual(str(context.exception), "Permission denied.")

    def test_read_file_permission_error(self):
        with unittest.mock.patch(
            "builtins.open", side_effect=PermissionError("Permission denied.")
        ):
            with self.assertRaises(PermissionError) as context:
                self.wrapper_file_system.read_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Permission denied.")

    def test_delete_file_permission_error(self):
        with unittest.mock.patch(
            "os.remove", side_effect=PermissionError("Permission denied.")
        ):
            with self.assertRaises(PermissionError) as context:
                self.wrapper_file_system.delete_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Permission denied.")

    def test_delete_file_os_error(self):
        with open(self.temp_file_path, "w", encoding="utf-8") as file:
            file.write("Content to delete")

        with unittest.mock.patch("os.remove") as mock_remove:
            mock_remove.side_effect = OSError("Permission denied.")
            with self.assertRaises(OSError) as context:
                self.wrapper_file_system.delete_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Permission denied.")

    def test_write_file_io_error(self):
        with unittest.mock.patch("builtins.open", side_effect=IOError("Disk full.")):
            with self.assertRaises(IOError) as context:
                self.wrapper_file_system.write_file(self.temp_file_path, "Content")
            self.assertEqual(str(context.exception), "Disk full.")

    def test_read_file_io_error(self):
        with unittest.mock.patch("builtins.open", side_effect=IOError("Disk full.")):
            with self.assertRaises(IOError) as context:
                self.wrapper_file_system.read_file(self.temp_file_path)
            self.assertEqual(str(context.exception), "Disk full.")

    @unittest.mock.patch("builtins.open", side_effect=IOError("Disk full."))
    def test_read_file_io_error(self, mock_open):
        with self.assertRaises(IOError) as context:
            self.wrapper_file_system.read_file(self.temp_file_path)
        self.assertEqual(str(context.exception), "Disk full.")
        self.assertEqual(mock_open.call_count, 1)


if __name__ == "__main__":
    unittest.main()
