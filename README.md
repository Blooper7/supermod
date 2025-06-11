# Supermod
Supermod is a higher version of the modulo operator for modular arithmetic.

Basically, I defined original modulo like so:
> Given two integers A and B, how many times do we add A to itself until we can't fit any more completely? Now return the space we have left

Essentially, as you'll see in the python file, we start with a multiplier set to zero, then check if `A*multiplier` is less than B. When `A*multiplier+1` is greater than B, we return `B-(A*multiplier)`

---

This is where the supermodulo comes in.

Supermodulo is defined instead as an incrementing exponent times A. So when A<sup>exponent+1</sup>>B, return B-A<sup>exponent</sup>
