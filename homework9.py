from collections import namedtuple
from itertools import accumulate
from itertools import islice
from itertools import starmap
from itertools import takewhile


Item = namedtuple("Item", "item, weight, value")

items = {("map", 9, 150), ("compass", 13, 35), ("water", 153, 200),
         ("sandwich", 50, 160), ("glucose", 15, 60), ("tin", 68, 45),
         ("banana", 27, 60), ("apple", 39, 40), ("cheese", 23, 30),
         ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
         ("T-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
         ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
         ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
         ("socks", 4, 50), ("book", 30, 10)}

items_to_get = islice(
    sorted(starmap(Item, items), key=lambda x: x.value / x.weight,
           reverse=True), len(list(takewhile(lambda x: x < 400, accumulate(
            [x.weight for x in
             sorted(starmap(Item, items), key=lambda x: x.value / x.weight,
                    reverse=True)])))))

if __name__ == "__main__":
    for item in items_to_get:
        print("{} - {}".format(item.item, item.value))
