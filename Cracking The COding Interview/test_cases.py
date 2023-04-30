import checkPermutation
import isUnique
import uRLify


def test_checkPermutation():
    assert checkPermutation.checkPermutation("Hello", "olleH") == bool(True)


def test_isUnique():
    assert isUnique.isUnique("olleH") == bool(False)


def test_urlify():
    assert uRLify.urlify("John The Master  ") == "John%20The%20Master"
