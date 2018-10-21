/**
 * @Author: Andy Hu <andy.hu>
 * @Date:   2018-10-21T23:51:32+08:00
 * @Email:  andy.hu@ringcentral.com
 * @Project: Fiji
 * @Last modified by:   andy.hu
 * @Last modified time: 2018-10-21T23:51:43+08:00
 * @Copyright: © RingCentral. All rights reserve
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
  let currentCursor = 0;
  let len = nums.length;
  if (len == 1) {
    return 0;
  }
  let maxLength = nums[currentCursor];
  let jumps = 0;
  while (currentCursor + maxLength + 1 < len) {
    const interval = nums
      .slice(currentCursor + 1, currentCursor + 1 + maxLength)
      .map((item, index) => item + index);
    const max = Math.max(...interval);
    cursor = interval.lastIndexOf(max);
    currentCursor += cursor + 1;
    maxLength = nums[currentCursor];
    jumps++;
  }
  return jumps + 1;
};
