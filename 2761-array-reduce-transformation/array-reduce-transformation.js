/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let x = init;
    nums.length===0 ? init : nums.forEach((element) => x = fn(x,element))
    return x
};