/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var x = -1;
    return function() {
        x++;
        return n + x;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */