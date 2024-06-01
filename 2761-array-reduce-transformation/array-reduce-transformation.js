/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let x = init;
    // nums.length===0 ? init : nums.forEach((element) => x = fn(x,element))
    if (nums.length === 0) init;

    for (var i=0;i<nums.length;i++) x = fn(x,nums[i]);

    return x;
};