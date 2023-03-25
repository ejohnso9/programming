-- Exercism, Lua Track, Problem #1
-- https://exercism.org/tracks/lua/exercises/hello-world/
-- Author: Erik Johnson
-- Date: 2023Mar11
-- DEV NOTES
-- to submit:
--  $ exercism submit ./hello-world.lua

-- Table to be returned by the hello-world module.
local hello_world = {}


function hello_world.hello()
    return 'Hello, World!'
end

return hello_world

