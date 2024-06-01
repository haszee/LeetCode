/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArray = []
    arr.forEach((element, index) => {
        newArray[index] = fn(element, index);
    });
    // for (var n=0;n<arr.length;n++){
    //     newArray[n] = fn(arr[n], n);
        
    return newArray;
};