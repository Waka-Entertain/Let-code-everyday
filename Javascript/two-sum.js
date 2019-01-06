/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var lookup = {};
    var res = [];
    nums.some((v, i) => {
        if (lookup[target - v]) {
            res = [lookup[target - v], i];
            return true;
        } else {
            lookup[v] = i;
            return false;
        }
    });
    return res;
};

