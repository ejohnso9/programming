-module(if_stmt).
-export([foo/1]).

%% example of if-statment
%% 2022Sep26 Working.
%% REMEBER: atoms start with lowercase str, vars with UC!
foo(N) ->
    Sym = if
        N == 1 -> one;
        N == 2 -> two;
        N == 3 -> three;
        true -> none
    end,
    %% io:format("Sym is: ~w~n", [Sym]),
    Sym.  %% symbol returned (in addition to print)

 %%% EOF
 
