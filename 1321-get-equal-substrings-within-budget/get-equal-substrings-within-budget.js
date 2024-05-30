/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function (s, t, maxCost) {
    // const ascii_num = {
    //     "a": 65,
    //     "b": 66,
    //     "c": 67,
    //     "d": 68,
    //     "e": 69,
    //     "f": 70,
    //     "g": 71,
    //     "h": 72,
    //     "i": 73,
    //     "j": 74,
    //     "k": 75,
    //     "l": 76,
    //     "m": 77,
    //     "n": 78,
    //     "o": 79,
    //     "p": 80,
    //     "q": 81,
    //     "r": 82,
    //     "s": 83,
    //     "t": 84,
    //     "u": 85,
    //     "v": 86,
    //     "w": 87,
    //     "x": 88,
    //     "y": 89,
    //     "z": 90
    // };

    var maxLen = 0;

    var start = 0;

    var currCost = 0;

    for (var i = 0; i < s.length; i++) {
        
        currCost += Math.abs(t.charCodeAt(i) - s.charCodeAt(i));

        while (currCost > maxCost) {

            currCost -= Math.abs(t.charCodeAt(start) - s.charCodeAt(start));
            start++;
        }
        
        maxLen = Math.max(maxLen,i-start+1);

    }

    return maxLen;
};