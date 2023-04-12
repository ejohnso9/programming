-module(case_stmt).
-export([foo/1]).

%% example of case-statment
%% 2022Sep26 
%% REMEMBER: atoms start with lowercase str, vars with UC!
foo(N) ->
    %% converting int to atom to demonstrate case statement
    RV = case N of
        1 -> one;
        2 -> two;
        3 -> three  % NB: cannot leave ';' on last clause!
        %% trying to call this w/ other values left to error naturally
    end,  %% NB: value of the case *is* the RETURN VALUE!

    io:format("RV is: ~w~n", [RV]),

    RV.


%% pg 39 of "Introducing Erlang", Simon St. Laurent gives this example
%% (pedagogic example to make explicit the possibility of guards on the
%% case clauses):
%%
%% fall_velocity(Planemo, Distance) ->
%%   Gravity = case Planemo of
%%     earth when Distance >= 0 -> 9.8;
%%     moon when Distance >= 0 -> 1.6;
%%     earth when Distance >= 0 -> 3.71
%%   end,  # NB: line ending of ',': func def is not over!
%%   
%%   math:sqrt(2 * Gravity * Distance).
%%
%% NB: The guard would be better employed on the function itself:
%%     fall_velocity(Planemo, Distance) when Distance >= 0 ->
%%     ...


 %%% EOF
 
