#!/usr/local/bin/lua
-- file: isogram.lua

-- DESCRIPTION
--     Exercism problem: 'isogram', Lua track
--
-- AUTHOR:
--     Erik Johnson
--
-- HISTORY
--  2023Mar24 Finally figured out module has to return defined function.
--  2023Mar23 Having problems with test suite complaining such as:
--              attempt to call a boolean value (upvalue 'is_isogram')
--  2023Mar22 Created.
    

-- Syntax here is a bit surprising.
-- The module returns the defined function to the test environment.
-- ej: Looks like if you want to return directly, the function has
--      to be anonymous. Else you can define:
--
--  function is_isogram(word)  -- return that from bottom of module.
return function(word)
    word = word:lower()
    local count_t = {}  -- internal table data: count of 'word' letters
    for i = 1, #word do
        c = word:sub(i, i)

        -- nevermind non-letter characters
        if c < 'a' or c > 'z' then
            goto continue end

        -- NB: can bail on first detected repeat
        if count_t[c] then  -- if new letter: count_t[c] is nil (falsy)
            return false
        else
            count_t[c] = 1
        end

        -- since Lua doesn't have a real continue stmt :(
        ::continue::
    end

    return true
end

-- return is_isogram

-- EOF

