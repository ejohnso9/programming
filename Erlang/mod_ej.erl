% my first Erlang module
-module(mod_ej).
-export([foo/1, bar/2]).

% func params need to start w/ uppercase!
foo(X) -> 2 * X + 1.

bar(X, Y) -> X + Y.

