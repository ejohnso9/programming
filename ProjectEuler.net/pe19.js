/*
file: pe19.js (JavaScript)

DESCRIPTION
    ProjectEuler.net Problem #19: Square Digit Chains
    http://projecteuler.net/problem=19

GENERAL APPROACH for JS
    Just defining some functions then text pasted into Chrome console.

PROBLEM APPROACH
    can construct Date objects in the form:
        new Date('2019-05-21 12:00:00 MDT')
    calling .getDay() on that returns 0 for Sunday, 1 for Monday.

    Just iterate the years and months, construct the string for the
    first of the month, check whether 1st was Sunday, count them.

COMMENTS

HISTORY
    2019May21 ejohnso9 created
*/
function pe19() {
    var count = 0;

    // How many Sunday on the first of the month in 20th Century?
    for (yr = 1901; yr <= 2000; yr++) {
        for (mo = 1; mo <= 12; mo++) {
            dt = new Date(`${yr}-${mo}-01 12:00:00 MST`);
            if (dt.getDay() == 0) {
                count += 1;
                //console.log(`[${count}] ${dt}`);
            }
        }
    }

    return count;
}
pe19(); // 171
