function isPal(x) {
    if (x.toString() == x.toString().split("").reverse().join("")) {
        return true;
    }   
    else {
        return false
    }
}

var nums = []
loop1:
    for (a=998; a!=0; a--) {
loop2:  
    for (b=999; b!=a-1; b--) {
        if (isPal(a*b)) {
            nums.push(a*b)
            break loop2;
        }
    }
}

function Max(numArray) {
    return Math.max.apply(null, numArray);
  }

console.log(Max(nums))

