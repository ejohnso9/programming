
-- orig code
--[[
return function(which)

end
--]]


-- API by example:
--    makeString('B', 2) => ' B'
--    makeString('B', 5) => ' B   '
--    makeString('C', 5) => '  C  '
--    makeString('D', 4) => '   D'
local function makeHalfString(c, length)
    t = {}
    -- convert 'c' to numeric 1-based index
    target_i = string.byte(c:upper()) - string.byte('A') + 1
    for i = 1, length do
        if i == target_i then
            t[i] = c
        else
            t[i] = ' '
        end
    end

    return table.concat(t, '')
end


local function makeDiamond(c_arg)
    lines_t = {}
    byte_A = string.byte('A')
    c_i = string.byte(c_arg:upper()) - byte_A + 1  -- 1 for 'A', 2 for 'B', etc.
    n = 2 * c_i - 1  -- width of the widest line

    for i = 1, c_i do
        c = string.char(byte_A + i - 1)
        s2 = makeHalfString(c, c_i)
        s1 = string.reverse(s2:sub(2))
        --lines_t[i] = string.format('"%s"', s1..s2)
        lines_t[i] = s1 .. s2
    end

    for i = c_i - 1, 1, -1 do
        lines_t[c_i + i] = lines_t[c_i - i]
    end

    return table.concat(lines_t, '\n')
end


-- works! (in VS CODE: ctrl-F5) -- result: 65
-- print(string.byte('A'))
--[[
s = makeHalfString('B', 5)
print(" 123456789")
print(string.format('"%s"', s))
--]]

print(makeDiamond('B'))


return makeDiamond

--EOF
