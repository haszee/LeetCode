/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    for (var n=0;n<arr.length;n++){
        arr[n] = fn(arr[n], n);
    };

    return arr;
};