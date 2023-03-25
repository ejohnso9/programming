
-- Author: Erik Johnson
--   Date: 2023Mar11
-- Exercism, Lua Track, 'Leap' Problem:
--  https://exercism.org/tracks/lua/exercises/leap


local leap_year = function(year)
    if year % 400 == 0 then
        return true
    elseif year % 100 == 0 then
        return false
    else
        return year % 4 == 0
    end
end

return leap_year

