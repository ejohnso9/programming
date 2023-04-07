
-- DESCRIPTION
--   Exercism problem on the Lua track: Largest Series Product
--   https://exercism.org/tracks/lua/exercises/largest-series-product
--
-- DISCUSSION
--   There are a number of ways code could be optimized to run faster.
--   There is also something to be said for simple, straightforward code
--   with an elegant design. Faster code that is optimized is generally
--   more complex code. The question is "Is it worth it?"
--
--   In this case, since I am going to have to walk through a list of
--   digits in string form and convert to ints, probably the only
--   optimization worth making is noting if one of them is 0 and then
--   using 0 for the product.


local ASCII_0 = string.byte('0')  -- -> 48
local ASCII_9 = string.byte('9')  -- -> 57


-- NB: does no validation of string: assumed to be only '0' - '9'
local function spanProduct(s)
    local product = 1  -- multiplicitive identity

    -- print(string.format("s is: '%s'", s))

    -- convert each char in 's' to int value, multiply product by that
    for i = 1, #s do
        val_i = string.byte(s:sub(i, i)) - ASCII_0
        if val_i == 0 then
            return 0
        else
            product = product * val_i
        end
    end

    -- print(string.format("product is: %s\n", product))

    return product
end


local function isAllDigits(s)
    local ascii = 0
    for i = 1, #s do
        ascii = string.byte(s:sub(i, i))
        if ascii < ASCII_0 or ascii > ASCII_9 then
            return false end
    end

    return true
end



-- args_t: table w/ keys: 
--   'digits': str - the list of digits to multiply
--   'span': int - how many digits to take at a time
local function largest_product(args_t)
    local digits_s = args_t['digits']
    local span = args_t['span']  -- int
    local max = 0

    -- degenerate case handling
    if span == 0 and #digits_s > 0 then
        return 1
    elseif span > #digits_s then
        error("span larger than digits")
    elseif #digits_s == 0 and span > 0 then
        error("no digits and non-zero span")
    elseif span < 0 then
        error("negative span")
    elseif not isAllDigits(digits_s) then
        error("found chars outside '0' - '9'")
    end

    -- inputs validated, compute the product
    for i = 1, #digits_s - span + 1 do
        val = spanProduct(digits_s:sub(i, i + span - 1))
        if val > max then
            max = val end
    end

    return max
end


return largest_product  -- function

