import os
import shutil
import unittest
from bot_task_commands import add_task_db, get_all_tasks_db
from db_man import init_db

class TestShowTask(unittest.TestCase):
    def setUp(self):
        if os.path.exists(os.environ.get("DB_PATH")):
            shutil.rmtree(os.environ.get("DB_PATH"), ignore_errors=True)
        init_db()

    def test_show_tasks(self):
        add_task_db(111,222, "job2do")
        tasks = get_all_tasks_db()
        self.assertIn("❌", tasks)

    def tearDown(self):
        db_path = os.environ.get("DB_PATH")
        if db_path and os.path.exists(db_path):
            shutil.rmtree(db_path, ignore_errors=True)

if __name__ == "__main__":
    unittest.main()