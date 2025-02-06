# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)
        print("run1")
    
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)
        print("run2")
    
    # following test is syntax test:

    def test_get_quality_method_exists(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        self.assertTrue(hasattr(gilded_rose, 'get_quality'), "FAIL: get_quality method not found")

    # following 3 tests are logical tests:

    def test_quality_never_greater_than_50(self):
        items = [Item("Aged Brie", 3, 49.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLess(items[0].quality, 50, "FAIL: Expected quality to be >= 0")
    
    def test_quality_never_negative(self):
        items = [Item("food", 4, 0.8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "FAIL: Expected quality to be > 0")

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8, "Conjured items should degrade 2x faster")
    

if __name__ == '__main__':
    unittest.main()
