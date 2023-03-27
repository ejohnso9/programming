#!/usr/local/bin/lua

-- DESCRIPTION
--      https://exercism.org/tracks/lua/exercises/hamming
--
-- AUTHOR
--      Erik Johnson
--
-- HISTORY
--      2023Mar25 Created.


-- the table this module returns to 'busted'
local Hamming = {}

function Hamming.compute(a, b)

    -- distance only defined for same-length strings
    if #a ~= #b then
        return -1 end

    local count = 0
    for i = 1, #a do
        if a:sub(i, i) ~= b:sub(i, i) then
            count = count + 1 end
    end

    return count
end

return Hamming

-- EOF

