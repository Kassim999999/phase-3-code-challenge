import pytest
from lib.models.author import Author

def test_save_and_find_author():
    author = Author(name="Test Author")
    author.save()

    found = Author.find_by_id(author.id)
    assert found.name == "Test Author"
