import unittest
import sys

sys.path.append("/")
from Task_first import unique_names


class TestMentorNames(unittest.TestCase):
    def test_unique_mentor_names(self):
        result = unique_names.get_unique_mentor_names(unique_names.mentors)
        expected = "Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
