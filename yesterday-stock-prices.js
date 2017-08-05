var getMaxProfit = function(list) {
    return (function(list) {
        if (list.length === 1) {
            return 0;
        }
        return list.slice(2).reduce(function(r, item) {
            r['diff'] = Math.max(r['diff'], (item - r['min']));
            r['min'] = Math.min(item, r['min']);
            return r;
        }, { diff: (list[1]-list[0]), min: list[0] })['diff'];
    })(list);
};

var assertEquals = function(a, b) {
    console.log(
        (a !== b) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
    );
};

// unit tests
(function() {
    var stockPricesYesterday = [10];
    assertEquals(0, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [10, 7, 5, 8, 11, 9];
    assertEquals(6, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [11, 10, 12, 1, 9, 8];
    assertEquals(8, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [11, 10, 12, 1, 9, 8, 15];
    assertEquals(14, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [5, 4, 3, 2, 1];
    assertEquals(-1, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [6, 4, 3, 2, 1];
    assertEquals(-1, getMaxProfit(stockPricesYesterday));
})();

(function() {
    var stockPricesYesterday = [6, 7, 11, 1, 2, 4];
    assertEquals(5, getMaxProfit(stockPricesYesterday));
})();

/*
 Suppose we could access yesterday's stock prices as an array, where:

 The indices are the time in minutes past trade opening time, which was 9:30am local time.
 The values are the price in dollars of Apple stock at that time.
 So if the stock cost $500 at 10:30am, stockPricesYesterday[60] = 500.

 Write an efficient function that takes stockPricesYesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

 For example:
 int[] stockPricesYesterday = new int[]{10, 7, 5, 8, 11, 9};
 getMaxProfit(stockPricesYesterday);
 // returns 6 (buying for $5 and selling for $11)

 No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).
*/