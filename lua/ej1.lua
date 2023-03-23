#!/usr/bin/env lua
-- file: ej1.lua
--
-- DESCRIPTION
--     Exercism problem, Lua track
-- AUTHOR:
--     Erik Johnson
function is_whatever(word)
    local t = {}  -- internal table data: count of 'word' letters
    for i = 1, #word do
        c = word:sub(i, i)
        if t[c] then
            t[c] = t[c] + 1
        else
            t[c] = 1
        end
    end

    -- dump
    --[[
    for i, v in pairs(t) do
        print(i, v)
    end
    --]]

    -- check: are there any repeats?
    for i, v in pairs(t) do
        if v ~= 1 then
            return false
        end
    end

    return true
end


-- call the function
word = "abcdefghijkl"
rv = is_whatever(word)
print(string.format(
    'is_whatever("%s") is: %s', word, rv))

