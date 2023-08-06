#!/usr/bin/env lua
-- file: diamond.lua


-- helper func to convert 'A' to 1, 'B' to 2, etc
local function charIndex(c)
    return string.byte(c:upper()) - string.byte('A') + 1
end


-- construct one line, given the letter (char 'c')
local function makeLine(c, halfLength)
    local t = {}  -- list-building buffer (table)

    -- build the right-hand half of the string (center and RH part)
    local target_i = charIndex(c)
    for i = 1, halfLength do
        if i == target_i then
            t[i] = c
        else
            t[i] = ' '
        end
    end

    local rh_str = table.concat(t)

    -- LH side is RH side (strictly) reversed
    -- NB: still works for strings of length 1 b/c the
    --     substring will be '' (empty string)
    return string.reverse(rh_str:sub(2)) .. rh_str .. '\n'
end


-- build the diamond multi-line string
local function makeDiamond(c)
    local lines_t = {}  -- list of lines in the diamond
    local c_i = charIndex(c)  -- A: 1, B: 2, ..., Z: 26

    -- diamond top (+ center line)
    -- make a line for 'A' up to whatever 'c' is
    for i = 1, c_i do
        local c2 = string.char(string.byte('A') + i - 1)
        lines_t[i] = makeLine(c2, c_i)
    end

    -- reflect top-half of diamond to make bottom half
    for i = c_i - 1, 1, -1 do
        lines_t[c_i + i] = lines_t[c_i - i]
    end

    return table.concat(lines_t)  -- one multi-line string
end


return makeDiamond

--EOF

