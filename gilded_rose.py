# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
    
    def get_items(self):
        """Return list of all item names"""
        return [item.name for item in self.items]

    def get_quality(self, item_name):
        """Return quality of specified item"""
        for item in self.items:
            if item.name == item_name:
                return item.quality
        return None

    def update_quality(self):
        """Main method to update quality of all items"""
        for item in self.items:
            self._update_sell_in(item)
            
            if item.name == "Sulfuras":
                continue
            elif item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes":
                self._update_backstage_passes(item)
            elif item.name == "Conjured Item":
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)

            self._enforce_quality_bounds(item)

    def _update_sell_in(self, item):
        """Decrease sell_in for all items"""
        item.sell_in -= 1

    def _update_aged_brie(self, item):
        """Handle Aged Brie quality updates"""
        if item.quality < 49:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 49:
                item.quality += 1

    def _update_backstage_passes(self, item):
        """Handle Backstage passes quality updates"""
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self._increase_quality(item, 3)
        elif item.sell_in < 10:
            self._increase_quality(item, 2)
        else:
            self._increase_quality(item, 1)

    def _update_conjured_item(self, item):
        """Handle Conjured items quality updates"""
        quality_decrease = 2
        if item.sell_in < 0:
            quality_decrease = 4
        self._decrease_quality(item, quality_decrease)

    def _update_normal_item(self, item):
        """Handle normal items quality updates"""
        quality_decrease = 1
        if item.sell_in < 0:
            quality_decrease = 2
        self._decrease_quality(item, quality_decrease)

    def _increase_quality(self, item, amount):
        """Helper method to increase quality with bounds checking"""
        if item.name != "Sulfuras":
            item.quality = min(49, item.quality + amount)

    def _decrease_quality(self, item, amount):
        """Helper method to decrease quality with bounds checking"""
        if item.name != "Sulfuras":
            item.quality = max(0, item.quality - amount)

    def _enforce_quality_bounds(self, item):
        """Ensure quality stays within bounds except for Sulfuras"""
        if item.name != "Sulfuras":
            item.quality = min(49, max(0, item.quality))
