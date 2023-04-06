
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


-- NB: does no validation of string: assumed to be only '0' - '9'
local function spanProduct(s)
    local product = 1  -- multiplicitive identity
    local ASCII_0 = 48  -- string.byte('0') -> 48

    -- convert each char in 's' to int value, multiply product by that
    for i = 1, #s do
        val_i = string.byte(s:sub(i, i)) - ASCII_0
        if val_i == 0 then
            return 0
        else
            product = product * val_i
        end
    end

    return product
end


-- args: config: table w/ keys: 
--  'digits': str - the list of digits to multiply
--  'span': int - how many digits to take at a time
return function(config)
    local digits_s = config['digits']
    local span = config['span']


    local last_index = #digits - span
    max = 0
    for i = 1, last_index do
        val = spanProduct(digits_s:sub(i, i + span))
        if val > max then
            max = val end
    end

    return max
end

